from abc import ABC, abstractmethod
from typing import Any


class CDPCommandSender(ABC):
    @abstractmethod
    async def send_raw(
        self,
        method: str,
        params: dict[str, Any] | None = None,
        session_id: str | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any]:
        """Send a raw CDP command and return its result payload."""
