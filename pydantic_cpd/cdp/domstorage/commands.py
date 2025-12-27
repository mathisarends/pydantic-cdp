"""Generated command models from CDP specification"""
# Domain: DOMStorage Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *


class ClearParams(CDPModel):
    storage_id: StorageId


class GetdomstorageitemsParams(CDPModel):
    storage_id: StorageId


class GetdomstorageitemsResult(CDPModel):
    entries: list[Item]


class RemovedomstorageitemParams(CDPModel):
    storage_id: StorageId
    key: str


class SetdomstorageitemParams(CDPModel):
    storage_id: StorageId
    key: str
    value: str
