"""Generated command models from CDP specification"""
# Domain: IndexedDB Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *

from pydantic_cpd.cdp import storage


class ClearobjectstoreParams(CDPModel):
    """Clears all entries from an object store."""

    security_origin: str | None = None
    storage_key: str | None = None
    storage_bucket: storage.StorageBucket | None = None
    database_name: str
    object_store_name: str


class DeletedatabaseParams(CDPModel):
    """Deletes a database."""

    security_origin: str | None = None
    storage_key: str | None = None
    storage_bucket: storage.StorageBucket | None = None
    database_name: str


class DeleteobjectstoreentriesParams(CDPModel):
    """Delete a range of entries from an object store"""

    security_origin: str | None = None
    storage_key: str | None = None
    storage_bucket: storage.StorageBucket | None = None
    database_name: str
    object_store_name: str
    key_range: KeyRange


class RequestdataParams(CDPModel):
    """Requests data from object store or index."""

    security_origin: str | None = None
    storage_key: str | None = None
    storage_bucket: storage.StorageBucket | None = None
    database_name: str
    object_store_name: str
    index_name: str | None = None
    skip_count: int
    page_size: int
    key_range: KeyRange | None = None


class RequestdataResult(CDPModel):
    object_store_data_entries: list[DataEntry]
    has_more: bool


class GetmetadataParams(CDPModel):
    """Gets metadata of an object store."""

    security_origin: str | None = None
    storage_key: str | None = None
    storage_bucket: storage.StorageBucket | None = None
    database_name: str
    object_store_name: str


class GetmetadataResult(CDPModel):
    entries_count: float
    key_generator_value: float


class RequestdatabaseParams(CDPModel):
    """Requests database with given name in given frame."""

    security_origin: str | None = None
    storage_key: str | None = None
    storage_bucket: storage.StorageBucket | None = None
    database_name: str


class RequestdatabaseResult(CDPModel):
    database_with_object_stores: DatabaseWithObjectStores


class RequestdatabasenamesParams(CDPModel):
    """Requests database names for given security origin."""

    security_origin: str | None = None
    storage_key: str | None = None
    storage_bucket: storage.StorageBucket | None = None


class RequestdatabasenamesResult(CDPModel):
    database_names: list[str]
