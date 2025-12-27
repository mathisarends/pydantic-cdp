"""Generated client library from CDP specification"""
# Domain: Log Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import StartviolationsreportParams


class LogClient:
    """Provides access to log entries."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def clear(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Clears the log."""
        result = await self._client.send_raw(
            method="Log.clear",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def disable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Disables log domain, prevents further log entries from being reported to the client."""
        result = await self._client.send_raw(
            method="Log.disable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def enable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables log domain, sends the entries collected so far to the client by means of the
        `entryAdded` notification."""
        result = await self._client.send_raw(
            method="Log.enable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def start_violations_report(
        self, params: "StartviolationsreportParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """start violation reporting."""
        result = await self._client.send_raw(
            method="Log.startViolationsReport",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def stop_violations_report(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Stop violation reporting."""
        result = await self._client.send_raw(
            method="Log.stopViolationsReport",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result
