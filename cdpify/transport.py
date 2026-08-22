from collections.abc import AsyncIterator
from dataclasses import dataclass
from typing import Any, Protocol


@dataclass(frozen=True, slots=True)
class TransportEvent:
    method: str
    params: dict[str, Any]
    session_id: str | None = None


class Transport(Protocol):
    @property
    def is_connected(self) -> bool: ...

    async def connect(self) -> None: ...

    async def disconnect(self) -> None: ...

    async def execute(
        self,
        method: str,
        params: dict[str, Any] | None = None,
        session_id: str | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any]: ...

    def events(self) -> AsyncIterator[TransportEvent]: ...
