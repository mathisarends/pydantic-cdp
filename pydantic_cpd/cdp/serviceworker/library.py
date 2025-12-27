"""Generated client library from CDP specification"""
# Domain: ServiceWorker Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        DeliverpushmessageParams,
        DispatchperiodicsynceventParams,
        DispatchsynceventParams,
        SetforceupdateonpageloadParams,
        SkipwaitingParams,
        StartworkerParams,
        StopworkerParams,
        UnregisterParams,
        UpdateregistrationParams,
    )


class ServiceWorkerClient:
    """CDP ServiceWorker domain client."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def deliver_push_message(
        self, params: "DeliverpushmessageParams", session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="ServiceWorker.deliverPushMessage",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def disable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="ServiceWorker.disable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def dispatch_sync_event(
        self, params: "DispatchsynceventParams", session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="ServiceWorker.dispatchSyncEvent",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def dispatch_periodic_sync_event(
        self, params: "DispatchperiodicsynceventParams", session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="ServiceWorker.dispatchPeriodicSyncEvent",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def enable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="ServiceWorker.enable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_force_update_on_page_load(
        self, params: "SetforceupdateonpageloadParams", session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="ServiceWorker.setForceUpdateOnPageLoad",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def skip_waiting(
        self, params: "SkipwaitingParams", session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="ServiceWorker.skipWaiting",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def start_worker(
        self, params: "StartworkerParams", session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="ServiceWorker.startWorker",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def stop_all_workers(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="ServiceWorker.stopAllWorkers",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def stop_worker(
        self, params: "StopworkerParams", session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="ServiceWorker.stopWorker",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def unregister(
        self, params: "UnregisterParams", session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="ServiceWorker.unregister",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def update_registration(
        self, params: "UpdateregistrationParams", session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="ServiceWorker.updateRegistration",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result
