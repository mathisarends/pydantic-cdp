"""Generated command models from CDP specification"""
# Domain: HeapProfiler Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *

from pydantic_cpd.cdp import runtime


class AddinspectedheapobjectParams(CDPModel):
    """Enables console to refer to the node with given id via $x (see Command Line API for more details
    $x functions)."""

    heap_object_id: HeapSnapshotObjectId


class GetheapobjectidParams(CDPModel):
    object_id: runtime.RemoteObjectId


class GetheapobjectidResult(CDPModel):
    heap_snapshot_object_id: HeapSnapshotObjectId


class GetobjectbyheapobjectidParams(CDPModel):
    object_id: HeapSnapshotObjectId
    object_group: str | None = None


class GetobjectbyheapobjectidResult(CDPModel):
    result: runtime.RemoteObject


class GetsamplingprofileResult(CDPModel):
    profile: SamplingHeapProfile


class StartsamplingParams(CDPModel):
    sampling_interval: float | None = None
    stack_depth: float | None = None
    include_objects_collected_by_major_g_c: bool | None = None
    include_objects_collected_by_minor_g_c: bool | None = None


class StarttrackingheapobjectsParams(CDPModel):
    track_allocations: bool | None = None


class StopsamplingResult(CDPModel):
    profile: SamplingHeapProfile


class StoptrackingheapobjectsParams(CDPModel):
    report_progress: bool | None = None
    treat_global_objects_as_roots: bool | None = None
    capture_numeric_value: bool | None = None
    expose_internals: bool | None = None


class TakeheapsnapshotParams(CDPModel):
    report_progress: bool | None = None
    treat_global_objects_as_roots: bool | None = None
    capture_numeric_value: bool | None = None
    expose_internals: bool | None = None
