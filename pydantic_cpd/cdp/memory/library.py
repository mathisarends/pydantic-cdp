"""Generated client library from CDP specification"""
# Domain: Memory Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        GetalltimesamplingprofileResult,
        GetbrowsersamplingprofileResult,
        GetdomcountersResult,
        GetdomcountersforleakdetectionResult,
        GetsamplingprofileResult,
        SetpressurenotificationssuppressedParams,
        SimulatepressurenotificationParams,
        StartsamplingParams,
    )


class MemoryClient:
    """CDP Memory domain client."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def get_d_o_m_counters(
        self, params: None = None, session_id: str | None = None
    ) -> "GetdomcountersResult":
        """Retruns current DOM object counters."""
        result = await self._client.send_raw(
            method="Memory.getDOMCounters",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetdomcountersResult.model_validate(result)

    async def get_d_o_m_counters_for_leak_detection(
        self, params: None = None, session_id: str | None = None
    ) -> "GetdomcountersforleakdetectionResult":
        """Retruns DOM object counters after preparing renderer for leak detection."""
        result = await self._client.send_raw(
            method="Memory.getDOMCountersForLeakDetection",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetdomcountersforleakdetectionResult.model_validate(result)

    async def prepare_for_leak_detection(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Prepares for leak detection by terminating workers, stopping spellcheckers,
        dropping non-essential internal caches, running garbage collections, etc."""
        result = await self._client.send_raw(
            method="Memory.prepareForLeakDetection",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def forcibly_purge_java_script_memory(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Simulate OomIntervention by purging V8 memory."""
        result = await self._client.send_raw(
            method="Memory.forciblyPurgeJavaScriptMemory",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_pressure_notifications_suppressed(
        self,
        params: "SetpressurenotificationssuppressedParams",
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Enable/disable suppressing memory pressure notifications in all processes."""
        result = await self._client.send_raw(
            method="Memory.setPressureNotificationsSuppressed",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def simulate_pressure_notification(
        self,
        params: "SimulatepressurenotificationParams",
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Simulate a memory pressure notification in all processes."""
        result = await self._client.send_raw(
            method="Memory.simulatePressureNotification",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def start_sampling(
        self, params: "StartsamplingParams | None" = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Start collecting native memory profile."""
        result = await self._client.send_raw(
            method="Memory.startSampling",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def stop_sampling(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Stop collecting native memory profile."""
        result = await self._client.send_raw(
            method="Memory.stopSampling",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_all_time_sampling_profile(
        self, params: None = None, session_id: str | None = None
    ) -> "GetalltimesamplingprofileResult":
        """Retrieve native memory allocations profile
        collected since renderer process startup."""
        result = await self._client.send_raw(
            method="Memory.getAllTimeSamplingProfile",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetalltimesamplingprofileResult.model_validate(result)

    async def get_browser_sampling_profile(
        self, params: None = None, session_id: str | None = None
    ) -> "GetbrowsersamplingprofileResult":
        """Retrieve native memory allocations profile
        collected since browser process startup."""
        result = await self._client.send_raw(
            method="Memory.getBrowserSamplingProfile",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetbrowsersamplingprofileResult.model_validate(result)

    async def get_sampling_profile(
        self, params: None = None, session_id: str | None = None
    ) -> "GetsamplingprofileResult":
        """Retrieve native memory allocations profile collected since last
        `startSampling` call."""
        result = await self._client.send_raw(
            method="Memory.getSamplingProfile",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetsamplingprofileResult.model_validate(result)
