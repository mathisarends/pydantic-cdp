"""Generated client library from CDP specification"""
# Domain: Browser Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        AddprivacysandboxcoordinatorkeyconfigParams,
        AddprivacysandboxenrollmentoverrideParams,
        CanceldownloadParams,
        ExecutebrowsercommandParams,
        GetbrowsercommandlineResult,
        GethistogramParams,
        GethistogramResult,
        GethistogramsParams,
        GethistogramsResult,
        GetversionResult,
        GetwindowboundsParams,
        GetwindowboundsResult,
        GetwindowfortargetParams,
        GetwindowfortargetResult,
        GrantpermissionsParams,
        ResetpermissionsParams,
        SetcontentssizeParams,
        SetdocktileParams,
        SetdownloadbehaviorParams,
        SetpermissionParams,
        SetwindowboundsParams,
    )


class BrowserClient:
    """The Browser domain defines methods and events for browser managing."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def set_permission(
        self, params: "SetpermissionParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Set permission settings for given embedding and embedded origins."""
        result = await self._client.send_raw(
            method="Browser.setPermission",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def grant_permissions(
        self, params: "GrantpermissionsParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Grant specific permissions to the given origin and reject all others. Deprecated. Use
        setPermission instead."""
        result = await self._client.send_raw(
            method="Browser.grantPermissions",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def reset_permissions(
        self,
        params: "ResetpermissionsParams | None" = None,
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Reset all permission management for all origins."""
        result = await self._client.send_raw(
            method="Browser.resetPermissions",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_download_behavior(
        self, params: "SetdownloadbehaviorParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Set the behavior when downloading a file."""
        result = await self._client.send_raw(
            method="Browser.setDownloadBehavior",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def cancel_download(
        self, params: "CanceldownloadParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Cancel a download if in progress"""
        result = await self._client.send_raw(
            method="Browser.cancelDownload",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def close(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Close browser gracefully."""
        result = await self._client.send_raw(
            method="Browser.close",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def crash(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Crashes browser on the main thread."""
        result = await self._client.send_raw(
            method="Browser.crash",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def crash_gpu_process(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Crashes GPU process."""
        result = await self._client.send_raw(
            method="Browser.crashGpuProcess",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_version(
        self, params: None = None, session_id: str | None = None
    ) -> "GetversionResult":
        """Returns version information."""
        result = await self._client.send_raw(
            method="Browser.getVersion",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetversionResult.model_validate(result)

    async def get_browser_command_line(
        self, params: None = None, session_id: str | None = None
    ) -> "GetbrowsercommandlineResult":
        """Returns the command line switches for the browser process if, and only if
        --enable-automation is on the commandline."""
        result = await self._client.send_raw(
            method="Browser.getBrowserCommandLine",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetbrowsercommandlineResult.model_validate(result)

    async def get_histograms(
        self, params: "GethistogramsParams | None" = None, session_id: str | None = None
    ) -> "GethistogramsResult":
        """Get Chrome histograms."""
        result = await self._client.send_raw(
            method="Browser.getHistograms",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GethistogramsResult.model_validate(result)

    async def get_histogram(
        self, params: "GethistogramParams", session_id: str | None = None
    ) -> "GethistogramResult":
        """Get a Chrome histogram by name."""
        result = await self._client.send_raw(
            method="Browser.getHistogram",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GethistogramResult.model_validate(result)

    async def get_window_bounds(
        self, params: "GetwindowboundsParams", session_id: str | None = None
    ) -> "GetwindowboundsResult":
        """Get position and size of the browser window."""
        result = await self._client.send_raw(
            method="Browser.getWindowBounds",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetwindowboundsResult.model_validate(result)

    async def get_window_for_target(
        self,
        params: "GetwindowfortargetParams | None" = None,
        session_id: str | None = None,
    ) -> "GetwindowfortargetResult":
        """Get the browser window that contains the devtools target."""
        result = await self._client.send_raw(
            method="Browser.getWindowForTarget",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetwindowfortargetResult.model_validate(result)

    async def set_window_bounds(
        self, params: "SetwindowboundsParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Set position and/or size of the browser window."""
        result = await self._client.send_raw(
            method="Browser.setWindowBounds",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_contents_size(
        self, params: "SetcontentssizeParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Set size of the browser contents resizing browser window as necessary."""
        result = await self._client.send_raw(
            method="Browser.setContentsSize",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_dock_tile(
        self, params: "SetdocktileParams | None" = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Set dock tile details, platform-specific."""
        result = await self._client.send_raw(
            method="Browser.setDockTile",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def execute_browser_command(
        self, params: "ExecutebrowsercommandParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Invoke custom browser commands used by telemetry."""
        result = await self._client.send_raw(
            method="Browser.executeBrowserCommand",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def add_privacy_sandbox_enrollment_override(
        self,
        params: "AddprivacysandboxenrollmentoverrideParams",
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Allows a site to use privacy sandbox features that require enrollment
        without the site actually being enrolled. Only supported on page targets."""
        result = await self._client.send_raw(
            method="Browser.addPrivacySandboxEnrollmentOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def add_privacy_sandbox_coordinator_key_config(
        self,
        params: "AddprivacysandboxcoordinatorkeyconfigParams",
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Configures encryption keys used with a given privacy sandbox API to talk
        to a trusted coordinator.  Since this is intended for test automation only,
        coordinatorOrigin must be a .test domain. No existing coordinator
        configuration for the origin may exist."""
        result = await self._client.send_raw(
            method="Browser.addPrivacySandboxCoordinatorKeyConfig",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result
