from dataclasses import dataclass, field
from unittest.mock import AsyncMock, MagicMock

import pytest

from cdpify import ActiveSessionCDPClient, Client


@dataclass(kw_only=True, slots=True)
class _Event:
    value: int = field(metadata={"cdp_name": "value"})
    cdp_session_id: str | None = field(
        default=None,
        metadata={"cdp": False},
    )


@pytest.mark.asyncio
async def test_routes_commands_to_active_session() -> None:
    root_client = MagicMock(spec=Client)
    root_client.send_raw = AsyncMock(return_value={})
    client = ActiveSessionCDPClient(root_client)

    client.switch_to("session-2")
    await client.page.enable()

    root_client.send_raw.assert_awaited_once_with(
        method="Page.enable",
        params={},
        session_id="session-2",
        timeout=None,
    )


@pytest.mark.asyncio
async def test_explicit_session_overrides_active_session() -> None:
    root_client = MagicMock(spec=Client)
    root_client.send_raw = AsyncMock(return_value={})
    client = ActiveSessionCDPClient(root_client)
    client.switch_to("active-session")

    await client.send_raw("Runtime.evaluate", session_id="explicit-session")

    root_client.send_raw.assert_awaited_once_with(
        method="Runtime.evaluate",
        params=None,
        session_id="explicit-session",
        timeout=None,
    )


def test_uses_root_browser_and_target_domains() -> None:
    root_client = MagicMock(spec=Client)
    client = ActiveSessionCDPClient(root_client)

    assert client.browser is root_client.browser
    assert client.target is root_client.target


@pytest.mark.asyncio
async def test_delegates_event_listening_to_root_client() -> None:
    expected = _Event(value=1, cdp_session_id="session-2")

    async def event_stream():
        yield expected

    root_client = MagicMock(spec=Client)
    root_client.listen.return_value = event_stream()
    client = ActiveSessionCDPClient(root_client)

    event = await anext(client.listen("Test.event", _Event, timeout=1.0))

    assert event is expected
    root_client.listen.assert_called_once_with(
        event_name="Test.event",
        event_type=_Event,
        timeout=1.0,
    )
