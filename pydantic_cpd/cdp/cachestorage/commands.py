"""Generated command models from CDP specification"""
# Domain: CacheStorage Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *

from pydantic_cpd.cdp import storage


class DeletecacheParams(CDPModel):
    """Deletes a cache."""

    cache_id: CacheId


class DeleteentryParams(CDPModel):
    """Deletes a cache entry."""

    cache_id: CacheId
    request: str


class RequestcachenamesParams(CDPModel):
    """Requests cache names."""

    security_origin: str | None = None
    storage_key: str | None = None
    storage_bucket: storage.StorageBucket | None = None


class RequestcachenamesResult(CDPModel):
    caches: list[Cache]


class RequestcachedresponseParams(CDPModel):
    """Fetches cache entry."""

    cache_id: CacheId
    request_u_r_l: str
    request_headers: list[Header]


class RequestcachedresponseResult(CDPModel):
    response: CachedResponse


class RequestentriesParams(CDPModel):
    """Requests data from cache."""

    cache_id: CacheId
    skip_count: int | None = None
    page_size: int | None = None
    path_filter: str | None = None


class RequestentriesResult(CDPModel):
    cache_data_entries: list[DataEntry]
    return_count: float
