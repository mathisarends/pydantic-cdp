"""Generated command models from CDP specification"""
# Domain: Accessibility Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *

from pydantic_cpd.cdp import dom
from pydantic_cpd.cdp import page
from pydantic_cpd.cdp import runtime


class GetpartialaxtreeParams(CDPModel):
    """Fetches the accessibility node and partial accessibility tree for this DOM node, if it exists."""

    node_id: dom.NodeId | None = None
    backend_node_id: dom.BackendNodeId | None = None
    object_id: runtime.RemoteObjectId | None = None
    fetch_relatives: bool | None = None


class GetpartialaxtreeResult(CDPModel):
    nodes: list[AXNode]


class GetfullaxtreeParams(CDPModel):
    """Fetches the entire accessibility tree for the root Document"""

    depth: int | None = None
    frame_id: page.FrameId | None = None


class GetfullaxtreeResult(CDPModel):
    nodes: list[AXNode]


class GetrootaxnodeParams(CDPModel):
    """Fetches the root node.
    Requires `enable()` to have been called previously."""

    frame_id: page.FrameId | None = None


class GetrootaxnodeResult(CDPModel):
    node: AXNode


class GetaxnodeandancestorsParams(CDPModel):
    """Fetches a node and all ancestors up to and including the root.
    Requires `enable()` to have been called previously."""

    node_id: dom.NodeId | None = None
    backend_node_id: dom.BackendNodeId | None = None
    object_id: runtime.RemoteObjectId | None = None


class GetaxnodeandancestorsResult(CDPModel):
    nodes: list[AXNode]


class GetchildaxnodesParams(CDPModel):
    """Fetches a particular accessibility node by AXNodeId.
    Requires `enable()` to have been called previously."""

    id: AXNodeId
    frame_id: page.FrameId | None = None


class GetchildaxnodesResult(CDPModel):
    nodes: list[AXNode]


class QueryaxtreeParams(CDPModel):
    """Query a DOM node's accessibility subtree for accessible name and role.
    This command computes the name and role for all nodes in the subtree, including those that are
    ignored for accessibility, and returns those that match the specified name and role. If no DOM
    node is specified, or the DOM node does not exist, the command returns an error. If neither
    `accessibleName` or `role` is specified, it returns all the accessibility nodes in the subtree."""

    node_id: dom.NodeId | None = None
    backend_node_id: dom.BackendNodeId | None = None
    object_id: runtime.RemoteObjectId | None = None
    accessible_name: str | None = None
    role: str | None = None


class QueryaxtreeResult(CDPModel):
    nodes: list[AXNode]
