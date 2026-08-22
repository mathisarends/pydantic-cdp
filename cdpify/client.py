import asyncio
import json
import logging
from collections.abc import AsyncIterator
from typing import Any, Self

import websockets
from websockets.asyncio.client import ClientConnection, connect

from cdpify.domains import Browser, CDPDomains, Target
from cdpify.events import EventDispatcher, RawCDPEvent
from cdpify.exceptions import (
    CDPCommandException,
    CDPConnectionException,
    CDPTimeoutException,
)
from cdpify.shared.models import CDPEvent

logger = logging.getLogger(__name__)


class Client(CDPDomains):
    def __init__(
        self,
        url: str,
        *,
        additional_headers: dict[str, str] | None = None,
        max_frame_size: int = 100 * 1024 * 1024,
        default_timeout: float = 30.0,
    ) -> None:
        self.url: str = url
        self._additional_headers: dict[str, str] | None = additional_headers
        self._max_frame_size: int = max_frame_size
        self._default_timeout: float = default_timeout

        self._ws: ClientConnection | None = None
        self._next_message_id: int = 0
        self._pending_requests: dict[int, asyncio.Future[dict[str, Any]]] = {}
        self._message_loop_task: asyncio.Task[None] | None = None
        self._events: EventDispatcher = EventDispatcher()
        self._is_shutting_down: bool = False

    @property
    def is_connected(self) -> bool:
        return self._ws is not None

    async def __aenter__(self) -> Self:
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.disconnect()

    async def connect(self) -> None:
        if self._ws is not None:
            raise CDPConnectionException("Already connected")

        logger.info(f"Connecting to {self.url}")

        try:
            self._ws = await connect(
                self.url,
                max_size=self._max_frame_size,
                additional_headers=self._additional_headers,
            )
            self._is_shutting_down = False
            self._message_loop_task = asyncio.create_task(self._run_message_loop())
            logger.info("Connected")
        except Exception as e:
            raise CDPConnectionException(f"Connection failed: {e}") from e

    async def _run_message_loop(self) -> None:
        try:
            async for raw_message in self._ws:
                if self._is_shutting_down:
                    break
                await self._process_message(raw_message)
        except websockets.exceptions.ConnectionClosed:
            logger.info("Connection closed")
        except asyncio.CancelledError:
            logger.debug("Message loop cancelled")
            raise
        except Exception:
            logger.exception("Message loop error")
        finally:
            if not self._is_shutting_down:
                await self.disconnect()

    async def _process_message(self, raw: str) -> None:
        msg = json.loads(raw)

        if self._is_cdp_response(msg):
            await self._handle_response(msg)
        elif self._is_cdp_event(msg):
            await self._handle_event(msg)
        else:
            logger.warning(f"Unknown CDP message format: {msg}")

    def _is_cdp_response(self, msg: dict[str, Any]) -> bool:
        """CDP responses contain an 'id' field"""
        return "id" in msg

    def _is_cdp_event(self, msg: dict[str, Any]) -> bool:
        """CDP events contain a 'method' field"""
        return "method" in msg

    async def _handle_response(self, msg: dict[str, Any]) -> None:
        msg_id = msg["id"]
        future = self._pending_requests.get(msg_id)

        if not future or future.done():
            return

        if "error" in msg:
            future.set_exception(CDPCommandException(msg["error"]))
        else:
            future.set_result(msg.get("result", {}))

    async def _handle_event(self, msg: dict[str, Any]) -> None:
        method = msg["method"]
        event = RawCDPEvent(
            params=dict(msg.get("params", {})),
            session_id=msg.get("sessionId"),
        )

        logger.debug(f"Event: {method}")
        handled = await self._events.dispatch(method, event)

        if not handled:
            logger.debug(f"Unhandled event: {method}")

    async def disconnect(self) -> None:
        if self._is_shutting_down:
            return

        self._is_shutting_down = True
        logger.info("Disconnecting...")

        await self._stop_message_loop()
        self._cancel_pending_requests()
        await self._close_websocket()

        logger.info("Disconnected")

    async def _stop_message_loop(self) -> None:
        if self._message_loop_task and not self._message_loop_task.done():
            self._message_loop_task.cancel()
            try:
                await self._message_loop_task
            except asyncio.CancelledError:
                pass

    def _cancel_pending_requests(self) -> None:
        error = CDPConnectionException("Disconnected")
        for future in self._pending_requests.values():
            if not future.done():
                future.set_exception(error)
        self._pending_requests.clear()

    async def _close_websocket(self) -> None:
        if self._ws:
            try:
                await self._ws.close()
            except Exception as e:
                logger.debug(f"Websocket close error: {e}")
            finally:
                self._ws = None

    async def listen[T: CDPEvent](
        self, event_name: str, event_type: type[T], timeout: float | None = None
    ) -> AsyncIterator[T]:
        queue: asyncio.Queue[T] = asyncio.Queue()

        async def handler(event: RawCDPEvent) -> None:
            typed_event = event_type.from_cdp(
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

    async def send_raw(
        self,
        method: str,
        params: dict[str, Any] | None = None,
        session_id: str | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any]:
        if not self.is_connected:
            raise CDPConnectionException("Not connected")

        timeout = timeout or self._default_timeout
        msg_id = self._next_message_id
        self._next_message_id += 1

        message = self._build_message(msg_id, method, params, session_id)
        future = self._create_pending_request(msg_id)

        try:
            await self._send(msg_id, method, message)
            return await self._await_response(msg_id, method, future, timeout)
        finally:
            self._pending_requests.pop(msg_id, None)

    def _build_message(
        self,
        msg_id: int,
        method: str,
        params: dict[str, Any] | None,
        session_id: str | None,
    ) -> dict[str, Any]:
        message = {"id": msg_id, "method": method, "params": params or {}}
        if session_id:
            message["sessionId"] = session_id
        return message

    def _create_pending_request(self, msg_id: int) -> asyncio.Future[dict[str, Any]]:
        future: asyncio.Future[dict[str, Any]] = asyncio.Future()
        self._pending_requests[msg_id] = future
        return future

    async def _send(self, msg_id: int, method: str, message: dict[str, Any]) -> None:
        logger.debug(f"→ #{msg_id}: {method}")
        await self._ws.send(json.dumps(message))

    async def _await_response(
        self, msg_id: int, method: str, future: asyncio.Future, timeout: float
    ) -> dict[str, Any]:
        try:
            result = await asyncio.wait_for(future, timeout=timeout)
            logger.debug(f"← #{msg_id}: OK")
            return result
        except asyncio.TimeoutError:
            raise CDPTimeoutException(f"{method} timed out after {timeout}s") from None


class ActiveSessionCDPClient(CDPDomains):
    """CDP client view that routes commands to the active target session."""

    def __init__(self, root_client: Client) -> None:
        self._root_client = root_client
        self._session_id: str | None = None

    @property
    def session_id(self) -> str | None:
        return self._session_id

    # Browser and Target are browser-scoped domains. Delegate them to the root
    # client so their commands are not routed through the active target session.
    @property
    def browser(self) -> Browser:
        return self._root_client.browser

    @property
    def target(self) -> Target:
        return self._root_client.target

    def switch_to(self, session_id: str | None) -> None:
        self._session_id = session_id

    async def listen[T: CDPEvent](
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

    async def send_raw(
        self,
        method: str,
        params: dict[str, Any] | None = None,
        session_id: str | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any]:
        return await self._root_client.send_raw(
            method=method,
            params=params,
            session_id=session_id if session_id is not None else self._session_id,
            timeout=timeout,
        )
