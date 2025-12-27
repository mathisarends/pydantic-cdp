"""Generated client library from CDP specification"""
# Domain: DOMSnapshot Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        CapturesnapshotParams,
        CapturesnapshotResult,
        GetsnapshotParams,
        GetsnapshotResult,
    )


class DOMSnapshotClient:
    """This domain facilitates obtaining document snapshots with DOM, layout, and style information."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def disable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Disables DOM snapshot agent for the given page."""
        result = await self._client.send_raw(
            method="DOMSnapshot.disable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def enable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables DOM snapshot agent for the given page."""
        result = await self._client.send_raw(
            method="DOMSnapshot.enable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_snapshot(
        self, params: "GetsnapshotParams", session_id: str | None = None
    ) -> "GetsnapshotResult":
        """Returns a document snapshot, including the full DOM tree of the root node (including iframes,
        template contents, and imported documents) in a flattened array, as well as layout and
        white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is
        flattened."""
        result = await self._client.send_raw(
            method="DOMSnapshot.getSnapshot",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetsnapshotResult.model_validate(result)

    async def capture_snapshot(
        self, params: "CapturesnapshotParams", session_id: str | None = None
    ) -> "CapturesnapshotResult":
        """Returns a document snapshot, including the full DOM tree of the root node (including iframes,
        template contents, and imported documents) in a flattened array, as well as layout and
        white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is
        flattened."""
        result = await self._client.send_raw(
            method="DOMSnapshot.captureSnapshot",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return CapturesnapshotResult.model_validate(result)
