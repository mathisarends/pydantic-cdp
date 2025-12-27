"""Generated client library from CDP specification"""
# Domain: Animation Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        GetcurrenttimeParams,
        GetcurrenttimeResult,
        GetplaybackrateResult,
        ReleaseanimationsParams,
        ResolveanimationParams,
        ResolveanimationResult,
        SeekanimationsParams,
        SetpausedParams,
        SetplaybackrateParams,
        SettimingParams,
    )


class AnimationClient:
    """CDP Animation domain client."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def disable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Disables animation domain notifications."""
        result = await self._client.send_raw(
            method="Animation.disable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def enable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables animation domain notifications."""
        result = await self._client.send_raw(
            method="Animation.enable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_current_time(
        self, params: "GetcurrenttimeParams", session_id: str | None = None
    ) -> "GetcurrenttimeResult":
        """Returns the current time of the an animation."""
        result = await self._client.send_raw(
            method="Animation.getCurrentTime",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetcurrenttimeResult.model_validate(result)

    async def get_playback_rate(
        self, params: None = None, session_id: str | None = None
    ) -> "GetplaybackrateResult":
        """Gets the playback rate of the document timeline."""
        result = await self._client.send_raw(
            method="Animation.getPlaybackRate",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetplaybackrateResult.model_validate(result)

    async def release_animations(
        self, params: "ReleaseanimationsParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Releases a set of animations to no longer be manipulated."""
        result = await self._client.send_raw(
            method="Animation.releaseAnimations",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def resolve_animation(
        self, params: "ResolveanimationParams", session_id: str | None = None
    ) -> "ResolveanimationResult":
        """Gets the remote object of the Animation."""
        result = await self._client.send_raw(
            method="Animation.resolveAnimation",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return ResolveanimationResult.model_validate(result)

    async def seek_animations(
        self, params: "SeekanimationsParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Seek a set of animations to a particular time within each animation."""
        result = await self._client.send_raw(
            method="Animation.seekAnimations",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_paused(
        self, params: "SetpausedParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets the paused state of a set of animations."""
        result = await self._client.send_raw(
            method="Animation.setPaused",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_playback_rate(
        self, params: "SetplaybackrateParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets the playback rate of the document timeline."""
        result = await self._client.send_raw(
            method="Animation.setPlaybackRate",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_timing(
        self, params: "SettimingParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets the timing of an animation node."""
        result = await self._client.send_raw(
            method="Animation.setTiming",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result
