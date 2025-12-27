"""Generated client library from CDP specification"""
# Domain: DOMStorage Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        ClearParams,
        GetdomstorageitemsParams,
        GetdomstorageitemsResult,
        RemovedomstorageitemParams,
        SetdomstorageitemParams,
    )


class DOMStorageClient:
    """Query and modify DOM storage."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def clear(
        self, params: "ClearParams", session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="DOMStorage.clear",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def disable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Disables storage tracking, prevents storage events from being sent to the client."""
        result = await self._client.send_raw(
            method="DOMStorage.disable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def enable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables storage tracking, storage events will now be delivered to the client."""
        result = await self._client.send_raw(
            method="DOMStorage.enable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_d_o_m_storage_items(
        self, params: "GetdomstorageitemsParams", session_id: str | None = None
    ) -> "GetdomstorageitemsResult":
        result = await self._client.send_raw(
            method="DOMStorage.getDOMStorageItems",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetdomstorageitemsResult.model_validate(result)

    async def remove_d_o_m_storage_item(
        self, params: "RemovedomstorageitemParams", session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="DOMStorage.removeDOMStorageItem",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_d_o_m_storage_item(
        self, params: "SetdomstorageitemParams", session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="DOMStorage.setDOMStorageItem",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result
