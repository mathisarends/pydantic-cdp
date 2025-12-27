"""Generated client library from CDP specification"""
# Domain: IndexedDB Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        ClearobjectstoreParams,
        DeletedatabaseParams,
        DeleteobjectstoreentriesParams,
        GetmetadataParams,
        GetmetadataResult,
        RequestdataParams,
        RequestdataResult,
        RequestdatabaseParams,
        RequestdatabaseResult,
        RequestdatabasenamesParams,
        RequestdatabasenamesResult,
    )


class IndexedDBClient:
    """CDP IndexedDB domain client."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def clear_object_store(
        self, params: "ClearobjectstoreParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Clears all entries from an object store."""
        result = await self._client.send_raw(
            method="IndexedDB.clearObjectStore",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def delete_database(
        self, params: "DeletedatabaseParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Deletes a database."""
        result = await self._client.send_raw(
            method="IndexedDB.deleteDatabase",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def delete_object_store_entries(
        self, params: "DeleteobjectstoreentriesParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Delete a range of entries from an object store"""
        result = await self._client.send_raw(
            method="IndexedDB.deleteObjectStoreEntries",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def disable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Disables events from backend."""
        result = await self._client.send_raw(
            method="IndexedDB.disable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def enable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables events from backend."""
        result = await self._client.send_raw(
            method="IndexedDB.enable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def request_data(
        self, params: "RequestdataParams", session_id: str | None = None
    ) -> "RequestdataResult":
        """Requests data from object store or index."""
        result = await self._client.send_raw(
            method="IndexedDB.requestData",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return RequestdataResult.model_validate(result)

    async def get_metadata(
        self, params: "GetmetadataParams", session_id: str | None = None
    ) -> "GetmetadataResult":
        """Gets metadata of an object store."""
        result = await self._client.send_raw(
            method="IndexedDB.getMetadata",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetmetadataResult.model_validate(result)

    async def request_database(
        self, params: "RequestdatabaseParams", session_id: str | None = None
    ) -> "RequestdatabaseResult":
        """Requests database with given name in given frame."""
        result = await self._client.send_raw(
            method="IndexedDB.requestDatabase",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return RequestdatabaseResult.model_validate(result)

    async def request_database_names(
        self,
        params: "RequestdatabasenamesParams | None" = None,
        session_id: str | None = None,
    ) -> "RequestdatabasenamesResult":
        """Requests database names for given security origin."""
        result = await self._client.send_raw(
            method="IndexedDB.requestDatabaseNames",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return RequestdatabasenamesResult.model_validate(result)
