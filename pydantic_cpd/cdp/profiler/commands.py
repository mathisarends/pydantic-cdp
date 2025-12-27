"""Generated command models from CDP specification"""
# Domain: Profiler Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *


class GetbesteffortcoverageResult(CDPModel):
    result: list[ScriptCoverage]


class SetsamplingintervalParams(CDPModel):
    """Changes CPU profiler sampling interval. Must be called before CPU profiles recording started."""

    interval: int


class StartprecisecoverageParams(CDPModel):
    """Enable precise code coverage. Coverage data for JavaScript executed before enabling precise code
    coverage may be incomplete. Enabling prevents running optimized code and resets execution
    counters."""

    call_count: bool | None = None
    detailed: bool | None = None
    allow_triggered_updates: bool | None = None


class StartprecisecoverageResult(CDPModel):
    timestamp: float


class StopResult(CDPModel):
    profile: Profile


class TakeprecisecoverageResult(CDPModel):
    result: list[ScriptCoverage]
    timestamp: float
