"""Generated command models from CDP specification"""
# Domain: Target Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *

from pydantic_cpd.cdp import browser


class ActivatetargetParams(CDPModel):
    """Activates (focuses) the target."""

    target_id: TargetID


class AttachtotargetParams(CDPModel):
    """Attaches to the target with given id."""

    target_id: TargetID
    flatten: bool | None = None


class AttachtotargetResult(CDPModel):
    session_id: SessionID


class AttachtobrowsertargetResult(CDPModel):
    session_id: SessionID


class ClosetargetParams(CDPModel):
    """Closes the target. If the target is a page that gets closed too."""

    target_id: TargetID


class ClosetargetResult(CDPModel):
    success: bool


class ExposedevtoolsprotocolParams(CDPModel):
    """Inject object to the target's main frame that provides a communication
    channel with browser target.

    Injected object will be available as `window[bindingName]`.

    The object has the following API:
    - `binding.send(json)` - a method to send messages over the remote debugging protocol
    - `binding.onmessage = json => handleMessage(json)` - a callback that will be called for the protocol notifications and command responses."""

    target_id: TargetID
    binding_name: str | None = None
    inherit_permissions: bool | None = None


class CreatebrowsercontextParams(CDPModel):
    """Creates a new empty BrowserContext. Similar to an incognito profile but you can have more than
    one."""

    dispose_on_detach: bool | None = None
    proxy_server: str | None = None
    proxy_bypass_list: str | None = None
    origins_with_universal_network_access: list[str] | None = None


class CreatebrowsercontextResult(CDPModel):
    browser_context_id: browser.BrowserContextID


class GetbrowsercontextsResult(CDPModel):
    browser_context_ids: list[Browser.BrowserContextID]
    default_browser_context_id: browser.BrowserContextID | None = None


class CreatetargetParams(CDPModel):
    """Creates a new page."""

    url: str
    left: int | None = None
    top: int | None = None
    width: int | None = None
    height: int | None = None
    window_state: WindowState | None = None
    browser_context_id: browser.BrowserContextID | None = None
    enable_begin_frame_control: bool | None = None
    new_window: bool | None = None
    background: bool | None = None
    for_tab: bool | None = None
    hidden: bool | None = None


class CreatetargetResult(CDPModel):
    target_id: TargetID


class DetachfromtargetParams(CDPModel):
    """Detaches session with given id."""

    session_id: SessionID | None = None
    target_id: TargetID | None = None


class DisposebrowsercontextParams(CDPModel):
    """Deletes a BrowserContext. All the belonging pages will be closed without calling their
    beforeunload hooks."""

    browser_context_id: browser.BrowserContextID


class GettargetinfoParams(CDPModel):
    """Returns information about a target."""

    target_id: TargetID | None = None


class GettargetinfoResult(CDPModel):
    target_info: TargetInfo


class GettargetsParams(CDPModel):
    """Retrieves a list of available targets."""

    filter: TargetFilter | None = None


class GettargetsResult(CDPModel):
    target_infos: list[TargetInfo]


class SendmessagetotargetParams(CDPModel):
    """Sends protocol message over session with given id.
    Consider using flat mode instead; see commands attachToTarget, setAutoAttach,
    and crbug.com/991325."""

    message: str
    session_id: SessionID | None = None
    target_id: TargetID | None = None


class SetautoattachParams(CDPModel):
    """Controls whether to automatically attach to new targets which are considered
    to be directly related to this one (for example, iframes or workers).
    When turned on, attaches to all existing related targets as well. When turned off,
    automatically detaches from all currently attached targets.
    This also clears all targets added by `autoAttachRelated` from the list of targets to watch
    for creation of related targets.
    You might want to call this recursively for auto-attached targets to attach
    to all available targets."""

    auto_attach: bool
    wait_for_debugger_on_start: bool
    flatten: bool | None = None
    filter: TargetFilter | None = None


class AutoattachrelatedParams(CDPModel):
    """Adds the specified target to the list of targets that will be monitored for any related target
    creation (such as child frames, child workers and new versions of service worker) and reported
    through `attachedToTarget`. The specified target is also auto-attached.
    This cancels the effect of any previous `setAutoAttach` and is also cancelled by subsequent
    `setAutoAttach`. Only available at the Browser target."""

    target_id: TargetID
    wait_for_debugger_on_start: bool
    filter: TargetFilter | None = None


class SetdiscovertargetsParams(CDPModel):
    """Controls whether to discover available targets and notify via
    `targetCreated/targetInfoChanged/targetDestroyed` events."""

    discover: bool
    filter: TargetFilter | None = None


class SetremotelocationsParams(CDPModel):
    """Enables target discovery for the specified locations, when `setDiscoverTargets` was set to
    `true`."""

    locations: list[RemoteLocation]


class GetdevtoolstargetParams(CDPModel):
    """Gets the targetId of the DevTools page target opened for the given target
    (if any)."""

    target_id: TargetID


class GetdevtoolstargetResult(CDPModel):
    target_id: TargetID | None = None


class OpendevtoolsParams(CDPModel):
    """Opens a DevTools window for the target."""

    target_id: TargetID
    panel_id: str | None = None


class OpendevtoolsResult(CDPModel):
    target_id: TargetID
