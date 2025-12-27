"""Generated command models from CDP specification"""
# Domain: Browser Commands

from typing import Literal
from pydantic_cpd.cdp.base import CDPModel

from .types import *

from pydantic_cpd.cdp import target


class SetpermissionParams(CDPModel):
    """Set permission settings for given embedding and embedded origins."""

    permission: PermissionDescriptor
    setting: PermissionSetting
    origin: str | None = None
    embedded_origin: str | None = None
    browser_context_id: BrowserContextID | None = None


class GrantpermissionsParams(CDPModel):
    """Grant specific permissions to the given origin and reject all others. Deprecated. Use
    setPermission instead."""

    permissions: list[PermissionType]
    origin: str | None = None
    browser_context_id: BrowserContextID | None = None


class ResetpermissionsParams(CDPModel):
    """Reset all permission management for all origins."""

    browser_context_id: BrowserContextID | None = None


class SetdownloadbehaviorParams(CDPModel):
    """Set the behavior when downloading a file."""

    behavior: Literal["deny", "allow", "allowAndName", "default"]
    browser_context_id: BrowserContextID | None = None
    download_path: str | None = None
    events_enabled: bool | None = None


class CanceldownloadParams(CDPModel):
    """Cancel a download if in progress"""

    guid: str
    browser_context_id: BrowserContextID | None = None


class GetversionResult(CDPModel):
    protocol_version: str
    product: str
    revision: str
    user_agent: str
    js_version: str


class GetbrowsercommandlineResult(CDPModel):
    arguments: list[str]


class GethistogramsParams(CDPModel):
    """Get Chrome histograms."""

    query: str | None = None
    delta: bool | None = None


class GethistogramsResult(CDPModel):
    histograms: list[Histogram]


class GethistogramParams(CDPModel):
    """Get a Chrome histogram by name."""

    name: str
    delta: bool | None = None


class GethistogramResult(CDPModel):
    histogram: Histogram


class GetwindowboundsParams(CDPModel):
    """Get position and size of the browser window."""

    window_id: WindowID


class GetwindowboundsResult(CDPModel):
    bounds: Bounds


class GetwindowfortargetParams(CDPModel):
    """Get the browser window that contains the devtools target."""

    target_id: target.TargetID | None = None


class GetwindowfortargetResult(CDPModel):
    window_id: WindowID
    bounds: Bounds


class SetwindowboundsParams(CDPModel):
    """Set position and/or size of the browser window."""

    window_id: WindowID
    bounds: Bounds


class SetcontentssizeParams(CDPModel):
    """Set size of the browser contents resizing browser window as necessary."""

    window_id: WindowID
    width: int | None = None
    height: int | None = None


class SetdocktileParams(CDPModel):
    """Set dock tile details, platform-specific."""

    badge_label: str | None = None
    image: str | None = None


class ExecutebrowsercommandParams(CDPModel):
    """Invoke custom browser commands used by telemetry."""

    command_id: BrowserCommandId


class AddprivacysandboxenrollmentoverrideParams(CDPModel):
    """Allows a site to use privacy sandbox features that require enrollment
    without the site actually being enrolled. Only supported on page targets."""

    url: str


class AddprivacysandboxcoordinatorkeyconfigParams(CDPModel):
    """Configures encryption keys used with a given privacy sandbox API to talk
    to a trusted coordinator.  Since this is intended for test automation only,
    coordinatorOrigin must be a .test domain. No existing coordinator
    configuration for the origin may exist."""

    api: PrivacySandboxAPI
    coordinator_origin: str
    key_config: str
    browser_context_id: BrowserContextID | None = None
