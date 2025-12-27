"""Generated client library from CDP specification"""
# Domain: CacheStorage Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        DeletecacheParams,
        DeleteentryParams,
        RequestcachedresponseParams,
        RequestcachedresponseResult,
        RequestcachenamesParams,
        RequestcachenamesResult,
        RequestentriesParams,
        RequestentriesResult,
    )


class CacheStorageClient:
    """CDP CacheStorage domain client."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def delete_cache(
        self, params: "DeletecacheParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Deletes a cache."""
        result = await self._client.send_raw(
            method="CacheStorage.deleteCache",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def delete_entry(
        self, params: "DeleteentryParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Deletes a cache entry."""
        result = await self._client.send_raw(
            method="CacheStorage.deleteEntry",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def request_cache_names(
        self,
        params: "RequestcachenamesParams | None" = None,
        session_id: str | None = None,
    ) -> "RequestcachenamesResult":
        """Requests cache names."""
        result = await self._client.send_raw(
            method="CacheStorage.requestCacheNames",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return RequestcachenamesResult.model_validate(result)

    async def request_cached_response(
        self, params: "RequestcachedresponseParams", session_id: str | None = None
    ) -> "RequestcachedresponseResult":
        """Fetches cache entry."""
        result = await self._client.send_raw(
            method="CacheStorage.requestCachedResponse",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return RequestcachedresponseResult.model_validate(result)

    async def request_entries(
        self, params: "RequestentriesParams", session_id: str | None = None
    ) -> "RequestentriesResult":
        """Requests data from cache."""
        result = await self._client.send_raw(
            method="CacheStorage.requestEntries",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return RequestentriesResult.model_validate(result)
