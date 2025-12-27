"""Generated client library from CDP specification"""
# Domain: DOM Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        CollectclassnamesfromsubtreeParams,
        CollectclassnamesfromsubtreeResult,
        CopytoParams,
        CopytoResult,
        DescribenodeParams,
        DescribenodeResult,
        DiscardsearchresultsParams,
        EnableParams,
        FocusParams,
        ForceshowpopoverParams,
        ForceshowpopoverResult,
        GetanchorelementParams,
        GetanchorelementResult,
        GetattributesParams,
        GetattributesResult,
        GetboxmodelParams,
        GetboxmodelResult,
        GetcontainerfornodeParams,
        GetcontainerfornodeResult,
        GetcontentquadsParams,
        GetcontentquadsResult,
        GetdetacheddomnodesResult,
        GetdocumentParams,
        GetdocumentResult,
        GetelementbyrelationParams,
        GetelementbyrelationResult,
        GetfileinfoParams,
        GetfileinfoResult,
        GetflatteneddocumentParams,
        GetflatteneddocumentResult,
        GetframeownerParams,
        GetframeownerResult,
        GetnodeforlocationParams,
        GetnodeforlocationResult,
        GetnodesforsubtreebystyleParams,
        GetnodesforsubtreebystyleResult,
        GetnodestacktracesParams,
        GetnodestacktracesResult,
        GetouterhtmlParams,
        GetouterhtmlResult,
        GetqueryingdescendantsforcontainerParams,
        GetqueryingdescendantsforcontainerResult,
        GetrelayoutboundaryParams,
        GetrelayoutboundaryResult,
        GetsearchresultsParams,
        GetsearchresultsResult,
        GettoplayerelementsResult,
        MovetoParams,
        MovetoResult,
        PerformsearchParams,
        PerformsearchResult,
        PushnodebypathtofrontendParams,
        PushnodebypathtofrontendResult,
        PushnodesbybackendidstofrontendParams,
        PushnodesbybackendidstofrontendResult,
        QueryselectorParams,
        QueryselectorResult,
        QueryselectorallParams,
        QueryselectorallResult,
        RemoveattributeParams,
        RemovenodeParams,
        RequestchildnodesParams,
        RequestnodeParams,
        RequestnodeResult,
        ResolvenodeParams,
        ResolvenodeResult,
        ScrollintoviewifneededParams,
        SetattributesastextParams,
        SetattributevalueParams,
        SetfileinputfilesParams,
        SetinspectednodeParams,
        SetnodenameParams,
        SetnodenameResult,
        SetnodestacktracesenabledParams,
        SetnodevalueParams,
        SetouterhtmlParams,
    )


class DOMClient:
    """This domain exposes DOM read/write operations. Each DOM Node is represented with its mirror object
    that has an `id`. This `id` can be used to get additional information on the Node, resolve it into
    the JavaScript object wrapper, etc. It is important that client receives DOM events only for the
    nodes that are known to the client. Backend keeps track of the nodes that were sent to the client
    and never sends the same node twice. It is client's responsibility to collect information about
    the nodes that were sent to the client. Note that `iframe` owner elements will return
    corresponding document elements as their child nodes."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def collect_class_names_from_subtree(
        self,
        params: "CollectclassnamesfromsubtreeParams",
        session_id: str | None = None,
    ) -> "CollectclassnamesfromsubtreeResult":
        """Collects class names for the node with given id and all of it's child nodes."""
        result = await self._client.send_raw(
            method="DOM.collectClassNamesFromSubtree",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return CollectclassnamesfromsubtreeResult.model_validate(result)

    async def copy_to(
        self, params: "CopytoParams", session_id: str | None = None
    ) -> "CopytoResult":
        """Creates a deep copy of the specified node and places it into the target container before the
        given anchor."""
        result = await self._client.send_raw(
            method="DOM.copyTo",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return CopytoResult.model_validate(result)

    async def describe_node(
        self, params: "DescribenodeParams | None" = None, session_id: str | None = None
    ) -> "DescribenodeResult":
        """Describes node given its id, does not require domain to be enabled. Does not start tracking any
        objects, can be used for automation."""
        result = await self._client.send_raw(
            method="DOM.describeNode",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return DescribenodeResult.model_validate(result)

    async def scroll_into_view_if_needed(
        self,
        params: "ScrollintoviewifneededParams | None" = None,
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Scrolls the specified rect of the given node into view if not already visible.
        Note: exactly one between nodeId, backendNodeId and objectId should be passed
        to identify the node."""
        result = await self._client.send_raw(
            method="DOM.scrollIntoViewIfNeeded",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def disable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Disables DOM agent for the given page."""
        result = await self._client.send_raw(
            method="DOM.disable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def discard_search_results(
        self, params: "DiscardsearchresultsParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Discards search results from the session with the given id. `getSearchResults` should no longer
        be called for that search."""
        result = await self._client.send_raw(
            method="DOM.discardSearchResults",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def enable(
        self, params: "EnableParams | None" = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables DOM agent for the given page."""
        result = await self._client.send_raw(
            method="DOM.enable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def focus(
        self, params: "FocusParams | None" = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Focuses the given element."""
        result = await self._client.send_raw(
            method="DOM.focus",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_attributes(
        self, params: "GetattributesParams", session_id: str | None = None
    ) -> "GetattributesResult":
        """Returns attributes for the specified node."""
        result = await self._client.send_raw(
            method="DOM.getAttributes",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetattributesResult.model_validate(result)

    async def get_box_model(
        self, params: "GetboxmodelParams | None" = None, session_id: str | None = None
    ) -> "GetboxmodelResult":
        """Returns boxes for the given node."""
        result = await self._client.send_raw(
            method="DOM.getBoxModel",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetboxmodelResult.model_validate(result)

    async def get_content_quads(
        self,
        params: "GetcontentquadsParams | None" = None,
        session_id: str | None = None,
    ) -> "GetcontentquadsResult":
        """Returns quads that describe node position on the page. This method
        might return multiple quads for inline nodes."""
        result = await self._client.send_raw(
            method="DOM.getContentQuads",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetcontentquadsResult.model_validate(result)

    async def get_document(
        self, params: "GetdocumentParams | None" = None, session_id: str | None = None
    ) -> "GetdocumentResult":
        """Returns the root DOM node (and optionally the subtree) to the caller.
        Implicitly enables the DOM domain events for the current target."""
        result = await self._client.send_raw(
            method="DOM.getDocument",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetdocumentResult.model_validate(result)

    async def get_flattened_document(
        self,
        params: "GetflatteneddocumentParams | None" = None,
        session_id: str | None = None,
    ) -> "GetflatteneddocumentResult":
        """Returns the root DOM node (and optionally the subtree) to the caller.
        Deprecated, as it is not designed to work well with the rest of the DOM agent.
        Use DOMSnapshot.captureSnapshot instead."""
        result = await self._client.send_raw(
            method="DOM.getFlattenedDocument",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetflatteneddocumentResult.model_validate(result)

    async def get_nodes_for_subtree_by_style(
        self, params: "GetnodesforsubtreebystyleParams", session_id: str | None = None
    ) -> "GetnodesforsubtreebystyleResult":
        """Finds nodes with a given computed style in a subtree."""
        result = await self._client.send_raw(
            method="DOM.getNodesForSubtreeByStyle",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetnodesforsubtreebystyleResult.model_validate(result)

    async def get_node_for_location(
        self, params: "GetnodeforlocationParams", session_id: str | None = None
    ) -> "GetnodeforlocationResult":
        """Returns node id at given location. Depending on whether DOM domain is enabled, nodeId is
        either returned or not."""
        result = await self._client.send_raw(
            method="DOM.getNodeForLocation",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetnodeforlocationResult.model_validate(result)

    async def get_outer_h_t_m_l(
        self, params: "GetouterhtmlParams | None" = None, session_id: str | None = None
    ) -> "GetouterhtmlResult":
        """Returns node's HTML markup."""
        result = await self._client.send_raw(
            method="DOM.getOuterHTML",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetouterhtmlResult.model_validate(result)

    async def get_relayout_boundary(
        self, params: "GetrelayoutboundaryParams", session_id: str | None = None
    ) -> "GetrelayoutboundaryResult":
        """Returns the id of the nearest ancestor that is a relayout boundary."""
        result = await self._client.send_raw(
            method="DOM.getRelayoutBoundary",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetrelayoutboundaryResult.model_validate(result)

    async def get_search_results(
        self, params: "GetsearchresultsParams", session_id: str | None = None
    ) -> "GetsearchresultsResult":
        """Returns search results from given `fromIndex` to given `toIndex` from the search with the given
        identifier."""
        result = await self._client.send_raw(
            method="DOM.getSearchResults",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetsearchresultsResult.model_validate(result)

    async def hide_highlight(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Hides any highlight."""
        result = await self._client.send_raw(
            method="DOM.hideHighlight",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def highlight_node(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Highlights DOM node."""
        result = await self._client.send_raw(
            method="DOM.highlightNode",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def highlight_rect(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Highlights given rectangle."""
        result = await self._client.send_raw(
            method="DOM.highlightRect",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def mark_undoable_state(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Marks last undoable state."""
        result = await self._client.send_raw(
            method="DOM.markUndoableState",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def move_to(
        self, params: "MovetoParams", session_id: str | None = None
    ) -> "MovetoResult":
        """Moves node into the new container, places it before the given anchor."""
        result = await self._client.send_raw(
            method="DOM.moveTo",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return MovetoResult.model_validate(result)

    async def perform_search(
        self, params: "PerformsearchParams", session_id: str | None = None
    ) -> "PerformsearchResult":
        """Searches for a given string in the DOM tree. Use `getSearchResults` to access search results or
        `cancelSearch` to end this search session."""
        result = await self._client.send_raw(
            method="DOM.performSearch",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return PerformsearchResult.model_validate(result)

    async def push_node_by_path_to_frontend(
        self, params: "PushnodebypathtofrontendParams", session_id: str | None = None
    ) -> "PushnodebypathtofrontendResult":
        """Requests that the node is sent to the caller given its path. // FIXME, use XPath"""
        result = await self._client.send_raw(
            method="DOM.pushNodeByPathToFrontend",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return PushnodebypathtofrontendResult.model_validate(result)

    async def push_nodes_by_backend_ids_to_frontend(
        self,
        params: "PushnodesbybackendidstofrontendParams",
        session_id: str | None = None,
    ) -> "PushnodesbybackendidstofrontendResult":
        """Requests that a batch of nodes is sent to the caller given their backend node ids."""
        result = await self._client.send_raw(
            method="DOM.pushNodesByBackendIdsToFrontend",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return PushnodesbybackendidstofrontendResult.model_validate(result)

    async def query_selector(
        self, params: "QueryselectorParams", session_id: str | None = None
    ) -> "QueryselectorResult":
        """Executes `querySelector` on a given node."""
        result = await self._client.send_raw(
            method="DOM.querySelector",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return QueryselectorResult.model_validate(result)

    async def query_selector_all(
        self, params: "QueryselectorallParams", session_id: str | None = None
    ) -> "QueryselectorallResult":
        """Executes `querySelectorAll` on a given node."""
        result = await self._client.send_raw(
            method="DOM.querySelectorAll",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return QueryselectorallResult.model_validate(result)

    async def get_top_layer_elements(
        self, params: None = None, session_id: str | None = None
    ) -> "GettoplayerelementsResult":
        """Returns NodeIds of current top layer elements.
        Top layer is rendered closest to the user within a viewport, therefore its elements always
        appear on top of all other content."""
        result = await self._client.send_raw(
            method="DOM.getTopLayerElements",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GettoplayerelementsResult.model_validate(result)

    async def get_element_by_relation(
        self, params: "GetelementbyrelationParams", session_id: str | None = None
    ) -> "GetelementbyrelationResult":
        """Returns the NodeId of the matched element according to certain relations."""
        result = await self._client.send_raw(
            method="DOM.getElementByRelation",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetelementbyrelationResult.model_validate(result)

    async def redo(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Re-does the last undone action."""
        result = await self._client.send_raw(
            method="DOM.redo",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def remove_attribute(
        self, params: "RemoveattributeParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Removes attribute with given name from an element with given id."""
        result = await self._client.send_raw(
            method="DOM.removeAttribute",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def remove_node(
        self, params: "RemovenodeParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Removes node with given id."""
        result = await self._client.send_raw(
            method="DOM.removeNode",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def request_child_nodes(
        self, params: "RequestchildnodesParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Requests that children of the node with given id are returned to the caller in form of
        `setChildNodes` events where not only immediate children are retrieved, but all children down to
        the specified depth."""
        result = await self._client.send_raw(
            method="DOM.requestChildNodes",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def request_node(
        self, params: "RequestnodeParams", session_id: str | None = None
    ) -> "RequestnodeResult":
        """Requests that the node is sent to the caller given the JavaScript node object reference. All
        nodes that form the path from the node to the root are also sent to the client as a series of
        `setChildNodes` notifications."""
        result = await self._client.send_raw(
            method="DOM.requestNode",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return RequestnodeResult.model_validate(result)

    async def resolve_node(
        self, params: "ResolvenodeParams | None" = None, session_id: str | None = None
    ) -> "ResolvenodeResult":
        """Resolves the JavaScript node object for a given NodeId or BackendNodeId."""
        result = await self._client.send_raw(
            method="DOM.resolveNode",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return ResolvenodeResult.model_validate(result)

    async def set_attribute_value(
        self, params: "SetattributevalueParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets attribute for an element with given id."""
        result = await self._client.send_raw(
            method="DOM.setAttributeValue",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_attributes_as_text(
        self, params: "SetattributesastextParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets attributes on element with given id. This method is useful when user edits some existing
        attribute value and types in several attribute name/value pairs."""
        result = await self._client.send_raw(
            method="DOM.setAttributesAsText",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_file_input_files(
        self, params: "SetfileinputfilesParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets files for the given file input element."""
        result = await self._client.send_raw(
            method="DOM.setFileInputFiles",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_node_stack_traces_enabled(
        self, params: "SetnodestacktracesenabledParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets if stack traces should be captured for Nodes. See `Node.getNodeStackTraces`. Default is disabled."""
        result = await self._client.send_raw(
            method="DOM.setNodeStackTracesEnabled",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_node_stack_traces(
        self, params: "GetnodestacktracesParams", session_id: str | None = None
    ) -> "GetnodestacktracesResult":
        """Gets stack traces associated with a Node. As of now, only provides stack trace for Node creation."""
        result = await self._client.send_raw(
            method="DOM.getNodeStackTraces",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetnodestacktracesResult.model_validate(result)

    async def get_file_info(
        self, params: "GetfileinfoParams", session_id: str | None = None
    ) -> "GetfileinfoResult":
        """Returns file information for the given
        File wrapper."""
        result = await self._client.send_raw(
            method="DOM.getFileInfo",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetfileinfoResult.model_validate(result)

    async def get_detached_dom_nodes(
        self, params: None = None, session_id: str | None = None
    ) -> "GetdetacheddomnodesResult":
        """Returns list of detached nodes"""
        result = await self._client.send_raw(
            method="DOM.getDetachedDomNodes",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetdetacheddomnodesResult.model_validate(result)

    async def set_inspected_node(
        self, params: "SetinspectednodeParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables console to refer to the node with given id via $x (see Command Line API for more details
        $x functions)."""
        result = await self._client.send_raw(
            method="DOM.setInspectedNode",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_node_name(
        self, params: "SetnodenameParams", session_id: str | None = None
    ) -> "SetnodenameResult":
        """Sets node name for a node with given id."""
        result = await self._client.send_raw(
            method="DOM.setNodeName",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return SetnodenameResult.model_validate(result)

    async def set_node_value(
        self, params: "SetnodevalueParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets node value for a node with given id."""
        result = await self._client.send_raw(
            method="DOM.setNodeValue",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_outer_h_t_m_l(
        self, params: "SetouterhtmlParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets node HTML markup, returns new node id."""
        result = await self._client.send_raw(
            method="DOM.setOuterHTML",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def undo(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Undoes the last performed action."""
        result = await self._client.send_raw(
            method="DOM.undo",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_frame_owner(
        self, params: "GetframeownerParams", session_id: str | None = None
    ) -> "GetframeownerResult":
        """Returns iframe node that owns iframe with the given domain."""
        result = await self._client.send_raw(
            method="DOM.getFrameOwner",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetframeownerResult.model_validate(result)

    async def get_container_for_node(
        self, params: "GetcontainerfornodeParams", session_id: str | None = None
    ) -> "GetcontainerfornodeResult":
        """Returns the query container of the given node based on container query
        conditions: containerName, physical and logical axes, and whether it queries
        scroll-state or anchored elements. If no axes are provided and
        queriesScrollState is false, the style container is returned, which is the
        direct parent or the closest element with a matching container-name."""
        result = await self._client.send_raw(
            method="DOM.getContainerForNode",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetcontainerfornodeResult.model_validate(result)

    async def get_querying_descendants_for_container(
        self,
        params: "GetqueryingdescendantsforcontainerParams",
        session_id: str | None = None,
    ) -> "GetqueryingdescendantsforcontainerResult":
        """Returns the descendants of a container query container that have
        container queries against this container."""
        result = await self._client.send_raw(
            method="DOM.getQueryingDescendantsForContainer",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetqueryingdescendantsforcontainerResult.model_validate(result)

    async def get_anchor_element(
        self, params: "GetanchorelementParams", session_id: str | None = None
    ) -> "GetanchorelementResult":
        """Returns the target anchor element of the given anchor query according to
        https://www.w3.org/TR/css-anchor-position-1/#target."""
        result = await self._client.send_raw(
            method="DOM.getAnchorElement",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetanchorelementResult.model_validate(result)

    async def force_show_popover(
        self, params: "ForceshowpopoverParams", session_id: str | None = None
    ) -> "ForceshowpopoverResult":
        """When enabling, this API force-opens the popover identified by nodeId
        and keeps it open until disabled."""
        result = await self._client.send_raw(
            method="DOM.forceShowPopover",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return ForceshowpopoverResult.model_validate(result)
