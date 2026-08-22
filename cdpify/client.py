import asyncio
import logging
from collections.abc import AsyncIterator
from typing import Any, Self

from cdpify.codec import decode_cdp
from cdpify.domains import Browser, CDPDomains, Target
from cdpify.events import EventDispatcher, RawCDPEvent
from cdpify.transport import Transport, TransportEvent

logger = logging.getLogger(__name__)


class Client(CDPDomains):
    def __init__(
        self,
        url: str | None = None,
        *,
        transport: Transport | None = None,
        additional_headers: dict[str, str] | None = None,
        max_frame_size: int = 100 * 1024 * 1024,
        default_timeout: float = 30.0,
    ) -> None:
        if transport is not None and url is not None:
            raise TypeError("Pass either url or transport, not both")
        if transport is None:
            if url is None:
                raise TypeError("Client requires either url or transport")
            transport = _create_websocket_transport(
                url,
                additional_headers=additional_headers,
                max_frame_size=max_frame_size,
                default_timeout=default_timeout,
            )

        self._transport = transport
        self._events = EventDispatcher()
        self._event_loop_task: asyncio.Task[None] | None = None
        super().__init__(transport)

    @property
    def transport(self) -> Transport:
        return self._transport

    @property
    def is_connected(self) -> bool:
        return self._transport.is_connected

    async def __aenter__(self) -> Self:
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.disconnect()

    async def connect(self) -> None:
        await self._transport.connect()
        self._event_loop_task = asyncio.create_task(self._run_event_loop())

    async def disconnect(self) -> None:
        await self._stop_event_loop()
        await self._transport.disconnect()

    async def execute(
        self,
        method: str,
        params: dict[str, Any] | None = None,
        session_id: str | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any]:
        return await self._transport.execute(
            method=method,
            params=params,
            session_id=session_id,
            timeout=timeout,
        )

    async def listen[T](
        self,
        event_name: str,
        event_type: type[T],
        timeout: float | None = None,
    ) -> AsyncIterator[T]:
        queue: asyncio.Queue[T] = asyncio.Queue()

        async def handler(event: RawCDPEvent) -> None:
            typed_event = decode_cdp(
                event_type,
                event.params,
                cdp_session_id=event.session_id,
            )
            await queue.put(typed_event)

        try:
            self._events.add_handler(event_name, handler)
            while True:
                yield await asyncio.wait_for(queue.get(), timeout=timeout)
        finally:
            self._events.remove_handler(event_name, handler)

    async def _run_event_loop(self) -> None:
        try:
            async for event in self._transport.events():
                await self._dispatch_event(event)
        except asyncio.CancelledError:
            raise
        except Exception:
            logger.exception("Transport event loop error")

    async def _dispatch_event(self, event: TransportEvent) -> None:
        raw_event = RawCDPEvent(
            params=event.params,
            session_id=event.session_id,
        )
        logger.debug("Event: %s", event.method)
        handled = await self._events.dispatch(event.method, raw_event)
        if not handled:
            logger.debug("Unhandled event: %s", event.method)

    async def _stop_event_loop(self) -> None:
        task = self._event_loop_task
        if task and not task.done():
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
        self._event_loop_task = None


class ActiveSessionCDPClient(CDPDomains):
    """CDP client view that routes commands to the active target session."""

    def __init__(self, root_client: Client) -> None:
        self._root_client = root_client
        self._session_transport = _SessionTransport(root_client.transport)
        super().__init__(self._session_transport)

    @property
    def session_id(self) -> str | None:
        return self._session_transport.session_id

    @property
    def browser(self) -> Browser:
        return self._root_client.browser

    @property
    def target(self) -> Target:
        return self._root_client.target

    def switch_to(self, session_id: str | None) -> None:
        self._session_transport.session_id = session_id

    async def listen[T](
        self,
        event_name: str,
        event_type: type[T],
        timeout: float | None = None,
    ) -> AsyncIterator[T]:
        async for event in self._root_client.listen(
            event_name=event_name,
            event_type=event_type,
            timeout=timeout,
        ):
            yield event

    async def execute(
        self,
        method: str,
        params: dict[str, Any] | None = None,
        session_id: str | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any]:
        return await self._session_transport.execute(
            method=method,
            params=params,
            session_id=session_id,
            timeout=timeout,
        )


class _SessionTransport:
    def __init__(self, transport: Transport) -> None:
        self._transport = transport
        self.session_id: str | None = None

    @property
    def is_connected(self) -> bool:
        return self._transport.is_connected

    async def connect(self) -> None:
        await self._transport.connect()

    async def disconnect(self) -> None:
        await self._transport.disconnect()

    async def execute(
        self,
        method: str,
        params: dict[str, Any] | None = None,
        session_id: str | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any]:
        return await self._transport.execute(
            method=method,
            params=params,
            session_id=session_id if session_id is not None else self.session_id,
            timeout=timeout,
        )

    def events(self) -> AsyncIterator[TransportEvent]:
        return self._transport.events()


def _create_websocket_transport(
    url: str,
    *,
    additional_headers: dict[str, str] | None,
    max_frame_size: int,
    default_timeout: float,
) -> Transport:
    try:
        from cdpify.transports.websocket import WebSocketTransport
    except ModuleNotFoundError as error:
        if error.name == "websockets":
            raise RuntimeError(
                "The default WebSocket transport requires cdpify[websocket]"
            ) from error
        raise

    return WebSocketTransport(
        url,
        additional_headers=additional_headers,
        max_frame_size=max_frame_size,
        default_timeout=default_timeout,
    )
