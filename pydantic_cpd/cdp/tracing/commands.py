"""Generated command models from CDP specification"""
# Domain: Tracing Commands

from typing import Literal
from pydantic_cpd.cdp.base import CDPModel

from .types import *


class GetcategoriesResult(CDPModel):
    categories: list[str]


class GettrackeventdescriptorResult(CDPModel):
    descriptor: str


class RecordclocksyncmarkerParams(CDPModel):
    """Record a clock sync marker in the trace."""

    sync_id: str


class RequestmemorydumpParams(CDPModel):
    """Request a global memory dump."""

    deterministic: bool | None = None
    level_of_detail: MemoryDumpLevelOfDetail | None = None


class RequestmemorydumpResult(CDPModel):
    dump_guid: str
    success: bool


class StartParams(CDPModel):
    """Start trace events collection."""

    categories: str | None = None
    options: str | None = None
    buffer_usage_reporting_interval: float | None = None
    transfer_mode: Literal["ReportEvents", "ReturnAsStream"] | None = None
    stream_format: StreamFormat | None = None
    stream_compression: StreamCompression | None = None
    trace_config: TraceConfig | None = None
    perfetto_config: str | None = None
    tracing_backend: TracingBackend | None = None
