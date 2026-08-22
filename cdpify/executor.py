from typing import Any, Protocol

from cdpify.transport import Transport


class CommandExecutor(Protocol):
    """Execute CDP commands within an already selected routing context."""

    async def execute(
        self,
        method: str,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any]: ...


class BoundCommandExecutor:
    """Bind command execution to the root connection or one CDP session."""

    def __init__(self, transport: Transport, session_id: str | None = None) -> None:
        self._transport = transport
        self._session_id = session_id

    @property
    def session_id(self) -> str | None:
        return self._session_id

    async def execute(
        self,
        method: str,
        params: dict[str, Any] | None = None,
        timeout: float | None = None,
    ) -> dict[str, Any]:
        return await self._transport.execute(
            method=method,
            params=params,
            session_id=self._session_id,
            timeout=timeout,
        )
