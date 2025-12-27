"""Generated client library from CDP specification"""
# Domain: HeapProfiler Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        AddinspectedheapobjectParams,
        GetheapobjectidParams,
        GetheapobjectidResult,
        GetobjectbyheapobjectidParams,
        GetobjectbyheapobjectidResult,
        GetsamplingprofileResult,
        StartsamplingParams,
        StarttrackingheapobjectsParams,
        StopsamplingResult,
        StoptrackingheapobjectsParams,
        TakeheapsnapshotParams,
    )


class HeapProfilerClient:
    """CDP HeapProfiler domain client."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def add_inspected_heap_object(
        self, params: "AddinspectedheapobjectParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables console to refer to the node with given id via $x (see Command Line API for more details
        $x functions)."""
        result = await self._client.send_raw(
            method="HeapProfiler.addInspectedHeapObject",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def collect_garbage(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="HeapProfiler.collectGarbage",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def disable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="HeapProfiler.disable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def enable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="HeapProfiler.enable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_heap_object_id(
        self, params: "GetheapobjectidParams", session_id: str | None = None
    ) -> "GetheapobjectidResult":
        result = await self._client.send_raw(
            method="HeapProfiler.getHeapObjectId",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetheapobjectidResult.model_validate(result)

    async def get_object_by_heap_object_id(
        self, params: "GetobjectbyheapobjectidParams", session_id: str | None = None
    ) -> "GetobjectbyheapobjectidResult":
        result = await self._client.send_raw(
            method="HeapProfiler.getObjectByHeapObjectId",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetobjectbyheapobjectidResult.model_validate(result)

    async def get_sampling_profile(
        self, params: None = None, session_id: str | None = None
    ) -> "GetsamplingprofileResult":
        result = await self._client.send_raw(
            method="HeapProfiler.getSamplingProfile",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetsamplingprofileResult.model_validate(result)

    async def start_sampling(
        self, params: "StartsamplingParams | None" = None, session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="HeapProfiler.startSampling",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def start_tracking_heap_objects(
        self,
        params: "StarttrackingheapobjectsParams | None" = None,
        session_id: str | None = None,
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="HeapProfiler.startTrackingHeapObjects",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def stop_sampling(
        self, params: None = None, session_id: str | None = None
    ) -> "StopsamplingResult":
        result = await self._client.send_raw(
            method="HeapProfiler.stopSampling",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return StopsamplingResult.model_validate(result)

    async def stop_tracking_heap_objects(
        self,
        params: "StoptrackingheapobjectsParams | None" = None,
        session_id: str | None = None,
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="HeapProfiler.stopTrackingHeapObjects",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def take_heap_snapshot(
        self,
        params: "TakeheapsnapshotParams | None" = None,
        session_id: str | None = None,
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="HeapProfiler.takeHeapSnapshot",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result
