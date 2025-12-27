"""Generated command models from CDP specification"""
# Domain: Memory Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *


class GetdomcountersResult(CDPModel):
    documents: int
    nodes: int
    js_event_listeners: int


class GetdomcountersforleakdetectionResult(CDPModel):
    counters: list[DOMCounter]


class SetpressurenotificationssuppressedParams(CDPModel):
    """Enable/disable suppressing memory pressure notifications in all processes."""

    suppressed: bool


class SimulatepressurenotificationParams(CDPModel):
    """Simulate a memory pressure notification in all processes."""

    level: PressureLevel


class StartsamplingParams(CDPModel):
    """Start collecting native memory profile."""

    sampling_interval: int | None = None
    suppress_randomness: bool | None = None


class GetalltimesamplingprofileResult(CDPModel):
    profile: SamplingProfile


class GetbrowsersamplingprofileResult(CDPModel):
    profile: SamplingProfile


class GetsamplingprofileResult(CDPModel):
    profile: SamplingProfile
