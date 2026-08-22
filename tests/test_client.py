import asyncio
import json
from dataclasses import dataclass
from unittest.mock import AsyncMock

import pytest

from cdpify.client import CDPClient
from cdpify.events import RawCDPEvent
from cdpify.exceptions import (
    CDPCommandException,
    CDPConnectionException,
    CDPTimeoutException,
)
from cdpify.shared.models import CDPEvent


class _FakeWebSocket:
    def __init__(self) -> None:
        self.sent_messages: list[str] = []
        self.closed = False

    async def send(self, payload: str) -> None:
        self.sent_messages.append(payload)

    async def close(self) -> None:
        self.closed = True


@dataclass
class _EventModel(CDPEvent):
    value: int


def test_domain_clients_are_cached() -> None:
    client = CDPClient("ws://example")
    properties = [
        "accessibility",
        "animation",
        "audits",
        "browser",
        "cache_storage",
        "cast",
        "console",
        "css",
        "debugger",
        "device_orientation",
        "dom",
        "dom_debugger",
        "dom_snapshot",
        "dom_storage",
        "emulation",
        "event_breakpoints",
        "fetch",
        "heap_profiler",
        "indexed_db",
        "input",
        "io",
        "layer_tree",
        "log",
        "media",
        "memory",
        "network",
        "overlay",
        "page",
        "performance",
        "profiler",
        "runtime",
        "schema",
        "security",
        "service_worker",
        "storage",
        "system_info",
        "target",
        "tethering",
        "tracing",
        "web_audio",
        "web_authn",
    ]

    for name in properties:
        first = getattr(client, name)
        second = getattr(client, name)
        assert first is second


@pytest.mark.asyncio
async def test_handle_response_sets_result_and_command_error() -> None:
    client = CDPClient("ws://example")
    ok_future = client._create_pending_request(1)
    err_future = client._create_pending_request(2)

    await client._handle_response({"id": 1, "result": {"ok": True}})
    await client._handle_response({"id": 2, "error": {"code": 9, "message": "failed"}})

    assert await ok_future == {"ok": True}
    with pytest.raises(CDPCommandException):
        await err_future


@pytest.mark.asyncio
async def test_handle_event_dispatches_payload_and_session_metadata() -> None:
    client = CDPClient("ws://example")
    client._events.dispatch = AsyncMock(return_value=True)  # type: ignore[method-assign]

    await client._handle_event(
        {
            "method": "Runtime.consoleAPICalled",
            "params": {"value": 1},
            "sessionId": "S1",
        }
    )

    client._events.dispatch.assert_awaited_once_with(  # type: ignore[attr-defined]
        "Runtime.consoleAPICalled",
        RawCDPEvent(params={"value": 1}, session_id="S1"),
    )


@pytest.mark.asyncio
async def test_listen_yields_typed_events_and_unregisters_handler() -> None:
    client = CDPClient("ws://example")
    stream = client.listen("Test.event", _EventModel, timeout=1.0)

    next_event_task = asyncio.create_task(anext(stream))
    await asyncio.sleep(0)
    await client._handle_event(
        {
            "method": "Test.event",
            "params": {"value": 7},
            "sessionId": "S1",
        }
    )
    event = await next_event_task

    assert event.value == 7
    assert event.cdp_session_id == "S1"

    await stream.aclose()
    assert "Test.event" in client._events._specific_handlers
    assert client._events._specific_handlers["Test.event"] == []


@pytest.mark.asyncio
async def test_send_serializes_payload_as_json() -> None:
    client = CDPClient("ws://example")
    client._ws = _FakeWebSocket()  # type: ignore[assignment]

    await client._send(
        3,
        "Page.enable",
        {"id": 3, "method": "Page.enable", "params": {}},
    )

    assert client._ws.sent_messages == [
        json.dumps({"id": 3, "method": "Page.enable", "params": {}})
    ]


@pytest.mark.asyncio
async def test_await_response_raises_timeout_exception() -> None:
    client = CDPClient("ws://example")
    unresolved: asyncio.Future[dict[str, object]] = asyncio.Future()

    with pytest.raises(CDPTimeoutException):
        await client._await_response(1, "Page.enable", unresolved, timeout=0.001)


@pytest.mark.asyncio
async def test_send_raw_requires_connection() -> None:
    client = CDPClient("ws://example")

    with pytest.raises(CDPConnectionException):
        await client.send_raw("Runtime.enable")


@pytest.mark.asyncio
async def test_send_raw_removes_pending_request_after_failure() -> None:
    client = CDPClient("ws://example")
    client._ws = _FakeWebSocket()  # type: ignore[assignment]
    client._send = AsyncMock()  # type: ignore[method-assign]
    client._await_response = AsyncMock(side_effect=CDPTimeoutException("timeout"))  # type: ignore[method-assign]

    with pytest.raises(CDPTimeoutException):
        await client.send_raw("Runtime.enable")

    assert client._pending_requests == {}


@pytest.mark.asyncio
async def test_disconnect_cancels_pending_requests_and_closes_websocket() -> None:
    client = CDPClient("ws://example")
    ws = _FakeWebSocket()
    client._ws = ws  # type: ignore[assignment]
    pending = client._create_pending_request(1)
    client._message_loop_task = asyncio.create_task(asyncio.sleep(10))

    await client.disconnect()

    assert ws.closed is True
    assert client._ws is None
    with pytest.raises(CDPConnectionException):
        await pending


@pytest.mark.asyncio
async def test_process_message_warns_for_unknown_payload(
    caplog: pytest.LogCaptureFixture,
) -> None:
    client = CDPClient("ws://example")

    with caplog.at_level("WARNING"):
        await client._process_message(json.dumps({"foo": "bar"}))

    assert "Unknown CDP message format" in caplog.text
