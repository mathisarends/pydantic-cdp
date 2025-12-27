"""Generated client library from CDP specification"""
# Domain: LayerTree Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        CompositingreasonsParams,
        CompositingreasonsResult,
        LoadsnapshotParams,
        LoadsnapshotResult,
        MakesnapshotParams,
        MakesnapshotResult,
        ProfilesnapshotParams,
        ProfilesnapshotResult,
        ReleasesnapshotParams,
        ReplaysnapshotParams,
        ReplaysnapshotResult,
        SnapshotcommandlogParams,
        SnapshotcommandlogResult,
    )


class LayerTreeClient:
    """CDP LayerTree domain client."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def compositing_reasons(
        self, params: "CompositingreasonsParams", session_id: str | None = None
    ) -> "CompositingreasonsResult":
        """Provides the reasons why the given layer was composited."""
        result = await self._client.send_raw(
            method="LayerTree.compositingReasons",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return CompositingreasonsResult.model_validate(result)

    async def disable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Disables compositing tree inspection."""
        result = await self._client.send_raw(
            method="LayerTree.disable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def enable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables compositing tree inspection."""
        result = await self._client.send_raw(
            method="LayerTree.enable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def load_snapshot(
        self, params: "LoadsnapshotParams", session_id: str | None = None
    ) -> "LoadsnapshotResult":
        """Returns the snapshot identifier."""
        result = await self._client.send_raw(
            method="LayerTree.loadSnapshot",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return LoadsnapshotResult.model_validate(result)

    async def make_snapshot(
        self, params: "MakesnapshotParams", session_id: str | None = None
    ) -> "MakesnapshotResult":
        """Returns the layer snapshot identifier."""
        result = await self._client.send_raw(
            method="LayerTree.makeSnapshot",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return MakesnapshotResult.model_validate(result)

    async def profile_snapshot(
        self, params: "ProfilesnapshotParams", session_id: str | None = None
    ) -> "ProfilesnapshotResult":
        result = await self._client.send_raw(
            method="LayerTree.profileSnapshot",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return ProfilesnapshotResult.model_validate(result)

    async def release_snapshot(
        self, params: "ReleasesnapshotParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Releases layer snapshot captured by the back-end."""
        result = await self._client.send_raw(
            method="LayerTree.releaseSnapshot",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def replay_snapshot(
        self, params: "ReplaysnapshotParams", session_id: str | None = None
    ) -> "ReplaysnapshotResult":
        """Replays the layer snapshot and returns the resulting bitmap."""
        result = await self._client.send_raw(
            method="LayerTree.replaySnapshot",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return ReplaysnapshotResult.model_validate(result)

    async def snapshot_command_log(
        self, params: "SnapshotcommandlogParams", session_id: str | None = None
    ) -> "SnapshotcommandlogResult":
        """Replays the layer snapshot and returns canvas log."""
        result = await self._client.send_raw(
            method="LayerTree.snapshotCommandLog",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return SnapshotcommandlogResult.model_validate(result)
