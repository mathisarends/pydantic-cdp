from collections.abc import AsyncIterator
from dataclasses import dataclass, field
from unittest.mock import AsyncMock, MagicMock

import pytest

from cdpify import ActiveSessionCDPClient, Client
from cdpify.transport import TransportEvent


@dataclass(kw_only=True, slots=True)
class _Event:
    value: int = field(metadata={"cdp_name": "value"})
    cdp_session_id: str | None = field(
        default=None,
        metadata={"cdp": False},
    )


class _Transport:
    def __init__(self) -> None:
        self.is_connected = True
        self.execute = AsyncMock(return_value={})

    async def connect(self) -> None: ...

    async def disconnect(self) -> None: ...

    def events(self) -> AsyncIterator[TransportEvent]:
        async def empty_stream() -> AsyncIterator[TransportEvent]:
            if False:
                yield TransportEvent("", {})

        return empty_stream()


@pytest.mark.asyncio
async def test_routes_commands_to_active_session() -> None:
    transport = _Transport()
    root_client = Client(transport=transport)  # type: ignore[arg-type]
    client = ActiveSessionCDPClient(root_client)

    client.switch_to("session-2")
    await client.page.enable()

    transport.execute.assert_awaited_once_with(
        method="Page.enable",
        params={},
        session_id="session-2",
        timeout=None,
    )


@pytest.mark.asyncio
async def test_explicit_session_overrides_active_session() -> None:
    transport = _Transport()
    root_client = Client(transport=transport)  # type: ignore[arg-type]
    client = ActiveSessionCDPClient(root_client)
    client.switch_to("active-session")

    await client.execute("Runtime.evaluate", session_id="explicit-session")

    transport.execute.assert_awaited_once_with(
        method="Runtime.evaluate",
        params=None,
        session_id="explicit-session",
        timeout=None,
    )


def test_uses_root_browser_and_target_domains() -> None:
    root_client = Client(transport=_Transport())  # type: ignore[arg-type]
    client = ActiveSessionCDPClient(root_client)

    assert client.browser is root_client.browser
    assert client.target is root_client.target


@pytest.mark.asyncio
async def test_delegates_event_listening_to_root_client() -> None:
    expected = _Event(value=1, cdp_session_id="session-2")

    async def event_stream():
        yield expected

    root_client = Client(transport=_Transport())  # type: ignore[arg-type]
    root_client.listen = MagicMock(return_value=event_stream())  # type: ignore[method-assign]
    client = ActiveSessionCDPClient(root_client)

    event = await anext(client.listen("Test.event", _Event, timeout=1.0))

    assert event is expected
    root_client.listen.assert_called_once_with(
        event_name="Test.event",
        event_type=_Event,
        timeout=1.0,
    )
