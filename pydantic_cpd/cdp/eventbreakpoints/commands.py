"""Generated command models from CDP specification"""
# Domain: EventBreakpoints Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *


class SetinstrumentationbreakpointParams(CDPModel):
    """Sets breakpoint on particular native event."""

    event_name: str


class RemoveinstrumentationbreakpointParams(CDPModel):
    """Removes breakpoint on particular native event."""

    event_name: str
