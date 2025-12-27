"""Generated command models from CDP specification"""
# Domain: DOMDebugger Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *

from pydantic_cpd.cdp import dom
from pydantic_cpd.cdp import runtime


class GeteventlistenersParams(CDPModel):
    """Returns event listeners of the given object."""

    object_id: runtime.RemoteObjectId
    depth: int | None = None
    pierce: bool | None = None


class GeteventlistenersResult(CDPModel):
    listeners: list[EventListener]


class RemovedombreakpointParams(CDPModel):
    """Removes DOM breakpoint that was set using `setDOMBreakpoint`."""

    node_id: dom.NodeId
    type: DOMBreakpointType


class RemoveeventlistenerbreakpointParams(CDPModel):
    """Removes breakpoint on particular DOM event."""

    event_name: str
    target_name: str | None = None


class RemoveinstrumentationbreakpointParams(CDPModel):
    """Removes breakpoint on particular native event."""

    event_name: str


class RemovexhrbreakpointParams(CDPModel):
    """Removes breakpoint from XMLHttpRequest."""

    url: str


class SetbreakoncspviolationParams(CDPModel):
    """Sets breakpoint on particular CSP violations."""

    violation_types: list[CSPViolationType]


class SetdombreakpointParams(CDPModel):
    """Sets breakpoint on particular operation with DOM."""

    node_id: dom.NodeId
    type: DOMBreakpointType


class SeteventlistenerbreakpointParams(CDPModel):
    """Sets breakpoint on particular DOM event."""

    event_name: str
    target_name: str | None = None


class SetinstrumentationbreakpointParams(CDPModel):
    """Sets breakpoint on particular native event."""

    event_name: str


class SetxhrbreakpointParams(CDPModel):
    """Sets breakpoint on XMLHttpRequest."""

    url: str
