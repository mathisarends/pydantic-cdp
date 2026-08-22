import logging

from cdpify.logging import _WebSocketLogFilter, configure_websocket_logging


def _make_record(name: str, message: str) -> logging.LogRecord:
    return logging.LogRecord(
        name=name,
        level=logging.DEBUG,
        pathname=__file__,
        lineno=1,
        msg=message,
        args=(),
        exc_info=None,
    )


def test_filter_ignores_non_websocket_logs() -> None:
    log_filter = _WebSocketLogFilter()
    record = _make_record("other.logger", "anything")

    assert log_filter.filter(record) is True
    assert record.name == "other.logger"


def test_filter_formats_ping_pong_latency(monkeypatch) -> None:
    log_filter = _WebSocketLogFilter()
    monkeypatch.setattr("cdpify.logging.time.time", lambda: 100.0)
    assert log_filter.filter(_make_record("websockets.client", "> PING ab cd")) is False

    monkeypatch.setattr("cdpify.logging.time.time", lambda: 100.05)
    pong = _make_record("websockets.client", "< PONG ab cd")
    assert log_filter.filter(pong) is True
    assert pong.msg == "✔ PING (50.0ms)"


def test_filter_suppresses_noise_and_formats_state() -> None:
    log_filter = _WebSocketLogFilter()

    assert (
        log_filter.filter(_make_record("websockets.client", "keepalive ping")) is False
    )

    open_state = _make_record("websockets.client", "= connection is OPEN")
    assert log_filter.filter(open_state) is True
    assert open_state.msg == "✅ WebSocket connected"


def test_configure_websocket_logging_is_idempotent() -> None:
    ws_logger = logging.getLogger("websockets.client")
    original_filters = list(ws_logger.filters)
    ws_logger.filters = []
    try:
        configure_websocket_logging()
        configure_websocket_logging()
        custom_filters = [
            f for f in ws_logger.filters if isinstance(f, _WebSocketLogFilter)
        ]
        assert len(custom_filters) == 1
    finally:
        ws_logger.filters = original_filters
