"""Generated client library from CDP specification"""
# Domain: Accessibility Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        GetaxnodeandancestorsParams,
        GetaxnodeandancestorsResult,
        GetchildaxnodesParams,
        GetchildaxnodesResult,
        GetfullaxtreeParams,
        GetfullaxtreeResult,
        GetpartialaxtreeParams,
        GetpartialaxtreeResult,
        GetrootaxnodeParams,
        GetrootaxnodeResult,
        QueryaxtreeParams,
        QueryaxtreeResult,
    )


class AccessibilityClient:
    """CDP Accessibility domain client."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def disable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Disables the accessibility domain."""
        result = await self._client.send_raw(
            method="Accessibility.disable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def enable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables the accessibility domain which causes `AXNodeId`s to remain consistent between method calls.
        This turns on accessibility for the page, which can impact performance until accessibility is disabled."""
        result = await self._client.send_raw(
            method="Accessibility.enable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_partial_a_x_tree(
        self,
        params: "GetpartialaxtreeParams | None" = None,
        session_id: str | None = None,
    ) -> "GetpartialaxtreeResult":
        """Fetches the accessibility node and partial accessibility tree for this DOM node, if it exists."""
        result = await self._client.send_raw(
            method="Accessibility.getPartialAXTree",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetpartialaxtreeResult.model_validate(result)

    async def get_full_a_x_tree(
        self, params: "GetfullaxtreeParams | None" = None, session_id: str | None = None
    ) -> "GetfullaxtreeResult":
        """Fetches the entire accessibility tree for the root Document"""
        result = await self._client.send_raw(
            method="Accessibility.getFullAXTree",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetfullaxtreeResult.model_validate(result)

    async def get_root_a_x_node(
        self, params: "GetrootaxnodeParams | None" = None, session_id: str | None = None
    ) -> "GetrootaxnodeResult":
        """Fetches the root node.
        Requires `enable()` to have been called previously."""
        result = await self._client.send_raw(
            method="Accessibility.getRootAXNode",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetrootaxnodeResult.model_validate(result)

    async def get_a_x_node_and_ancestors(
        self,
        params: "GetaxnodeandancestorsParams | None" = None,
        session_id: str | None = None,
    ) -> "GetaxnodeandancestorsResult":
        """Fetches a node and all ancestors up to and including the root.
        Requires `enable()` to have been called previously."""
        result = await self._client.send_raw(
            method="Accessibility.getAXNodeAndAncestors",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetaxnodeandancestorsResult.model_validate(result)

    async def get_child_a_x_nodes(
        self, params: "GetchildaxnodesParams", session_id: str | None = None
    ) -> "GetchildaxnodesResult":
        """Fetches a particular accessibility node by AXNodeId.
        Requires `enable()` to have been called previously."""
        result = await self._client.send_raw(
            method="Accessibility.getChildAXNodes",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetchildaxnodesResult.model_validate(result)

    async def query_a_x_tree(
        self, params: "QueryaxtreeParams | None" = None, session_id: str | None = None
    ) -> "QueryaxtreeResult":
        """Query a DOM node's accessibility subtree for accessible name and role.
        This command computes the name and role for all nodes in the subtree, including those that are
        ignored for accessibility, and returns those that match the specified name and role. If no DOM
        node is specified, or the DOM node does not exist, the command returns an error. If neither
        `accessibleName` or `role` is specified, it returns all the accessibility nodes in the subtree."""
        result = await self._client.send_raw(
            method="Accessibility.queryAXTree",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return QueryaxtreeResult.model_validate(result)
