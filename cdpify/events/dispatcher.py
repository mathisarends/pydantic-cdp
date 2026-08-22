import logging
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Any

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class RawCDPEvent:
    params: dict[str, Any]
    session_id: str | None = None


_EventHandler = Callable[[RawCDPEvent], Awaitable[None]]


class EventDispatcher:
    def __init__(self) -> None:
        self._specific_handlers: dict[str, list[_EventHandler]] = {}
        self._wildcard_handlers: list[_EventHandler] = []

    def add_handler(self, event_name: str | None, handler: _EventHandler) -> None:
        if event_name is None:
            self._wildcard_handlers.append(handler)
        else:
            self._specific_handlers.setdefault(event_name, []).append(handler)

    def remove_handler(self, event_name: str | None, handler: _EventHandler) -> None:
        if event_name is None:
            if handler in self._wildcard_handlers:
                self._wildcard_handlers.remove(handler)
        else:
            handlers = self._specific_handlers.get(event_name, [])
            if handler in handlers:
                handlers.remove(handler)

    async def dispatch(self, method: str, event: RawCDPEvent) -> bool:
        any_handled = False

        for handler in self._specific_handlers.get(method, []):
            if await _invoke_handler(handler, event):
                any_handled = True

        for handler in self._wildcard_handlers:
            if await _invoke_handler(handler, event):
                any_handled = True

        return any_handled


async def _invoke_handler(handler: _EventHandler, event: RawCDPEvent) -> bool:
    try:
        await handler(event)
        return True
    except Exception as e:
        logger.exception(f"Event handler error: {e}")
        return False
