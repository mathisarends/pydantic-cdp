"""Generated client library from CDP specification"""
# Domain: Performance Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import EnableParams, GetmetricsResult, SettimedomainParams


class PerformanceClient:
    """CDP Performance domain client."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def disable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Disable collecting and reporting metrics."""
        result = await self._client.send_raw(
            method="Performance.disable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def enable(
        self, params: "EnableParams | None" = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Enable collecting and reporting metrics."""
        result = await self._client.send_raw(
            method="Performance.enable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_time_domain(
        self, params: "SettimedomainParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets time domain to use for collecting and reporting duration metrics.
        Note that this must be called before enabling metrics collection. Calling
        this method while metrics collection is enabled returns an error."""
        result = await self._client.send_raw(
            method="Performance.setTimeDomain",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_metrics(
        self, params: None = None, session_id: str | None = None
    ) -> "GetmetricsResult":
        """Retrieve current values of run-time metrics."""
        result = await self._client.send_raw(
            method="Performance.getMetrics",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetmetricsResult.model_validate(result)
