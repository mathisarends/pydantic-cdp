"""Generated command models from CDP specification"""
# Domain: DOM Commands

from typing import Literal
from pydantic_cpd.cdp.base import CDPModel

from .types import *

from pydantic_cpd.cdp import dom
from pydantic_cpd.cdp import page
from pydantic_cpd.cdp import runtime


class CollectclassnamesfromsubtreeParams(CDPModel):
    """Collects class names for the node with given id and all of it's child nodes."""

    node_id: NodeId


class CollectclassnamesfromsubtreeResult(CDPModel):
    class_names: list[str]


class CopytoParams(CDPModel):
    """Creates a deep copy of the specified node and places it into the target container before the
    given anchor."""

    node_id: NodeId
    target_node_id: NodeId
    insert_before_node_id: NodeId | None = None


class CopytoResult(CDPModel):
    node_id: NodeId


class DescribenodeParams(CDPModel):
    """Describes node given its id, does not require domain to be enabled. Does not start tracking any
    objects, can be used for automation."""

    node_id: NodeId | None = None
    backend_node_id: BackendNodeId | None = None
    object_id: runtime.RemoteObjectId | None = None
    depth: int | None = None
    pierce: bool | None = None


class DescribenodeResult(CDPModel):
    node: Node


class ScrollintoviewifneededParams(CDPModel):
    """Scrolls the specified rect of the given node into view if not already visible.
    Note: exactly one between nodeId, backendNodeId and objectId should be passed
    to identify the node."""

    node_id: NodeId | None = None
    backend_node_id: BackendNodeId | None = None
    object_id: runtime.RemoteObjectId | None = None
    rect: Rect | None = None


class DiscardsearchresultsParams(CDPModel):
    """Discards search results from the session with the given id. `getSearchResults` should no longer
    be called for that search."""

    search_id: str


class EnableParams(CDPModel):
    """Enables DOM agent for the given page."""

    include_whitespace: Literal["none", "all"] | None = None


class FocusParams(CDPModel):
    """Focuses the given element."""

    node_id: NodeId | None = None
    backend_node_id: BackendNodeId | None = None
    object_id: runtime.RemoteObjectId | None = None


class GetattributesParams(CDPModel):
    """Returns attributes for the specified node."""

    node_id: NodeId


class GetattributesResult(CDPModel):
    attributes: list[str]


class GetboxmodelParams(CDPModel):
    """Returns boxes for the given node."""

    node_id: NodeId | None = None
    backend_node_id: BackendNodeId | None = None
    object_id: runtime.RemoteObjectId | None = None


class GetboxmodelResult(CDPModel):
    model: BoxModel


class GetcontentquadsParams(CDPModel):
    """Returns quads that describe node position on the page. This method
    might return multiple quads for inline nodes."""

    node_id: NodeId | None = None
    backend_node_id: BackendNodeId | None = None
    object_id: runtime.RemoteObjectId | None = None


class GetcontentquadsResult(CDPModel):
    quads: list[Quad]


class GetdocumentParams(CDPModel):
    """Returns the root DOM node (and optionally the subtree) to the caller.
    Implicitly enables the DOM domain events for the current target."""

    depth: int | None = None
    pierce: bool | None = None


class GetdocumentResult(CDPModel):
    root: Node


class GetflatteneddocumentParams(CDPModel):
    """Returns the root DOM node (and optionally the subtree) to the caller.
    Deprecated, as it is not designed to work well with the rest of the DOM agent.
    Use DOMSnapshot.captureSnapshot instead."""

    depth: int | None = None
    pierce: bool | None = None


class GetflatteneddocumentResult(CDPModel):
    nodes: list[Node]


class GetnodesforsubtreebystyleParams(CDPModel):
    """Finds nodes with a given computed style in a subtree."""

    node_id: NodeId
    computed_styles: list[CSSComputedStyleProperty]
    pierce: bool | None = None


class GetnodesforsubtreebystyleResult(CDPModel):
    node_ids: list[NodeId]


class GetnodeforlocationParams(CDPModel):
    """Returns node id at given location. Depending on whether DOM domain is enabled, nodeId is
    either returned or not."""

    x: int
    y: int
    include_user_agent_shadow_d_o_m: bool | None = None
    ignore_pointer_events_none: bool | None = None


class GetnodeforlocationResult(CDPModel):
    backend_node_id: BackendNodeId
    frame_id: page.FrameId
    node_id: NodeId | None = None


class GetouterhtmlParams(CDPModel):
    """Returns node's HTML markup."""

    node_id: NodeId | None = None
    backend_node_id: BackendNodeId | None = None
    object_id: runtime.RemoteObjectId | None = None
    include_shadow_d_o_m: bool | None = None


class GetouterhtmlResult(CDPModel):
    outer_h_t_m_l: str


class GetrelayoutboundaryParams(CDPModel):
    """Returns the id of the nearest ancestor that is a relayout boundary."""

    node_id: NodeId


class GetrelayoutboundaryResult(CDPModel):
    node_id: NodeId


class GetsearchresultsParams(CDPModel):
    """Returns search results from given `fromIndex` to given `toIndex` from the search with the given
    identifier."""

    search_id: str
    from_index: int
    to_index: int


class GetsearchresultsResult(CDPModel):
    node_ids: list[NodeId]


class MovetoParams(CDPModel):
    """Moves node into the new container, places it before the given anchor."""

    node_id: NodeId
    target_node_id: NodeId
    insert_before_node_id: NodeId | None = None


class MovetoResult(CDPModel):
    node_id: NodeId


class PerformsearchParams(CDPModel):
    """Searches for a given string in the DOM tree. Use `getSearchResults` to access search results or
    `cancelSearch` to end this search session."""

    query: str
    include_user_agent_shadow_d_o_m: bool | None = None


class PerformsearchResult(CDPModel):
    search_id: str
    result_count: int


class PushnodebypathtofrontendParams(CDPModel):
    """Requests that the node is sent to the caller given its path. // FIXME, use XPath"""

    path: str


class PushnodebypathtofrontendResult(CDPModel):
    node_id: NodeId


class PushnodesbybackendidstofrontendParams(CDPModel):
    """Requests that a batch of nodes is sent to the caller given their backend node ids."""

    backend_node_ids: list[BackendNodeId]


class PushnodesbybackendidstofrontendResult(CDPModel):
    node_ids: list[NodeId]


class QueryselectorParams(CDPModel):
    """Executes `querySelector` on a given node."""

    node_id: NodeId
    selector: str


class QueryselectorResult(CDPModel):
    node_id: NodeId


class QueryselectorallParams(CDPModel):
    """Executes `querySelectorAll` on a given node."""

    node_id: NodeId
    selector: str


class QueryselectorallResult(CDPModel):
    node_ids: list[NodeId]


class GettoplayerelementsResult(CDPModel):
    node_ids: list[NodeId]


class GetelementbyrelationParams(CDPModel):
    """Returns the NodeId of the matched element according to certain relations."""

    node_id: NodeId
    relation: Literal["PopoverTarget", "InterestTarget", "CommandFor"]


class GetelementbyrelationResult(CDPModel):
    node_id: NodeId


class RemoveattributeParams(CDPModel):
    """Removes attribute with given name from an element with given id."""

    node_id: NodeId
    name: str


class RemovenodeParams(CDPModel):
    """Removes node with given id."""

    node_id: NodeId


class RequestchildnodesParams(CDPModel):
    """Requests that children of the node with given id are returned to the caller in form of
    `setChildNodes` events where not only immediate children are retrieved, but all children down to
    the specified depth."""

    node_id: NodeId
    depth: int | None = None
    pierce: bool | None = None


class RequestnodeParams(CDPModel):
    """Requests that the node is sent to the caller given the JavaScript node object reference. All
    nodes that form the path from the node to the root are also sent to the client as a series of
    `setChildNodes` notifications."""

    object_id: runtime.RemoteObjectId


class RequestnodeResult(CDPModel):
    node_id: NodeId


class ResolvenodeParams(CDPModel):
    """Resolves the JavaScript node object for a given NodeId or BackendNodeId."""

    node_id: NodeId | None = None
    backend_node_id: dom.BackendNodeId | None = None
    object_group: str | None = None
    execution_context_id: runtime.ExecutionContextId | None = None


class ResolvenodeResult(CDPModel):
    object: runtime.RemoteObject


class SetattributevalueParams(CDPModel):
    """Sets attribute for an element with given id."""

    node_id: NodeId
    name: str
    value: str


class SetattributesastextParams(CDPModel):
    """Sets attributes on element with given id. This method is useful when user edits some existing
    attribute value and types in several attribute name/value pairs."""

    node_id: NodeId
    text: str
    name: str | None = None


class SetfileinputfilesParams(CDPModel):
    """Sets files for the given file input element."""

    files: list[str]
    node_id: NodeId | None = None
    backend_node_id: BackendNodeId | None = None
    object_id: runtime.RemoteObjectId | None = None


class SetnodestacktracesenabledParams(CDPModel):
    """Sets if stack traces should be captured for Nodes. See `Node.getNodeStackTraces`. Default is disabled."""

    enable: bool


class GetnodestacktracesParams(CDPModel):
    """Gets stack traces associated with a Node. As of now, only provides stack trace for Node creation."""

    node_id: NodeId


class GetnodestacktracesResult(CDPModel):
    creation: runtime.StackTrace | None = None


class GetfileinfoParams(CDPModel):
    """Returns file information for the given
    File wrapper."""

    object_id: runtime.RemoteObjectId


class GetfileinfoResult(CDPModel):
    path: str


class GetdetacheddomnodesResult(CDPModel):
    detached_nodes: list[DetachedElementInfo]


class SetinspectednodeParams(CDPModel):
    """Enables console to refer to the node with given id via $x (see Command Line API for more details
    $x functions)."""

    node_id: NodeId


class SetnodenameParams(CDPModel):
    """Sets node name for a node with given id."""

    node_id: NodeId
    name: str


class SetnodenameResult(CDPModel):
    node_id: NodeId


class SetnodevalueParams(CDPModel):
    """Sets node value for a node with given id."""

    node_id: NodeId
    value: str


class SetouterhtmlParams(CDPModel):
    """Sets node HTML markup, returns new node id."""

    node_id: NodeId
    outer_h_t_m_l: str


class GetframeownerParams(CDPModel):
    """Returns iframe node that owns iframe with the given domain."""

    frame_id: page.FrameId


class GetframeownerResult(CDPModel):
    backend_node_id: BackendNodeId
    node_id: NodeId | None = None


class GetcontainerfornodeParams(CDPModel):
    """Returns the query container of the given node based on container query
    conditions: containerName, physical and logical axes, and whether it queries
    scroll-state or anchored elements. If no axes are provided and
    queriesScrollState is false, the style container is returned, which is the
    direct parent or the closest element with a matching container-name."""

    node_id: NodeId
    container_name: str | None = None
    physical_axes: PhysicalAxes | None = None
    logical_axes: LogicalAxes | None = None
    queries_scroll_state: bool | None = None
    queries_anchored: bool | None = None


class GetcontainerfornodeResult(CDPModel):
    node_id: NodeId | None = None


class GetqueryingdescendantsforcontainerParams(CDPModel):
    """Returns the descendants of a container query container that have
    container queries against this container."""

    node_id: NodeId


class GetqueryingdescendantsforcontainerResult(CDPModel):
    node_ids: list[NodeId]


class GetanchorelementParams(CDPModel):
    """Returns the target anchor element of the given anchor query according to
    https://www.w3.org/TR/css-anchor-position-1/#target."""

    node_id: NodeId
    anchor_specifier: str | None = None


class GetanchorelementResult(CDPModel):
    node_id: NodeId


class ForceshowpopoverParams(CDPModel):
    """When enabling, this API force-opens the popover identified by nodeId
    and keeps it open until disabled."""

    node_id: NodeId
    enable: bool


class ForceshowpopoverResult(CDPModel):
    node_ids: list[NodeId]
