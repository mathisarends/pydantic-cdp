"""Generated client library from CDP specification"""
# Domain: Profiler Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        GetbesteffortcoverageResult,
        SetsamplingintervalParams,
        StartprecisecoverageParams,
        StartprecisecoverageResult,
        StopResult,
        TakeprecisecoverageResult,
    )


class ProfilerClient:
    """CDP Profiler domain client."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def disable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="Profiler.disable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def enable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="Profiler.enable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_best_effort_coverage(
        self, params: None = None, session_id: str | None = None
    ) -> "GetbesteffortcoverageResult":
        """Collect coverage data for the current isolate. The coverage data may be incomplete due to
        garbage collection."""
        result = await self._client.send_raw(
            method="Profiler.getBestEffortCoverage",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetbesteffortcoverageResult.model_validate(result)

    async def set_sampling_interval(
        self, params: "SetsamplingintervalParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Changes CPU profiler sampling interval. Must be called before CPU profiles recording started."""
        result = await self._client.send_raw(
            method="Profiler.setSamplingInterval",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def start(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="Profiler.start",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def start_precise_coverage(
        self,
        params: "StartprecisecoverageParams | None" = None,
        session_id: str | None = None,
    ) -> "StartprecisecoverageResult":
        """Enable precise code coverage. Coverage data for JavaScript executed before enabling precise code
        coverage may be incomplete. Enabling prevents running optimized code and resets execution
        counters."""
        result = await self._client.send_raw(
            method="Profiler.startPreciseCoverage",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return StartprecisecoverageResult.model_validate(result)

    async def stop(
        self, params: None = None, session_id: str | None = None
    ) -> "StopResult":
        result = await self._client.send_raw(
            method="Profiler.stop",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return StopResult.model_validate(result)

    async def stop_precise_coverage(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Disable precise code coverage. Disabling releases unnecessary execution count records and allows
        executing optimized code."""
        result = await self._client.send_raw(
            method="Profiler.stopPreciseCoverage",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def take_precise_coverage(
        self, params: None = None, session_id: str | None = None
    ) -> "TakeprecisecoverageResult":
        """Collect coverage data for the current isolate, and resets execution counters. Precise code
        coverage needs to have started."""
        result = await self._client.send_raw(
            method="Profiler.takePreciseCoverage",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return TakeprecisecoverageResult.model_validate(result)
