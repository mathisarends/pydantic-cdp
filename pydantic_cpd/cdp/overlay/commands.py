"""Generated command models from CDP specification"""
# Domain: Overlay Commands

from typing import Any
from pydantic_cpd.cdp.base import CDPModel

from .types import *

from pydantic_cpd.cdp import dom
from pydantic_cpd.cdp import page
from pydantic_cpd.cdp import runtime


class GethighlightobjectfortestParams(CDPModel):
    """For testing."""

    node_id: dom.NodeId
    include_distance: bool | None = None
    include_style: bool | None = None
    color_format: ColorFormat | None = None
    show_accessibility_info: bool | None = None


class GethighlightobjectfortestResult(CDPModel):
    highlight: dict[str, Any]


class GetgridhighlightobjectsfortestParams(CDPModel):
    """For Persistent Grid testing."""

    node_ids: list[DOM.NodeId]


class GetgridhighlightobjectsfortestResult(CDPModel):
    highlights: dict[str, Any]


class GetsourceorderhighlightobjectfortestParams(CDPModel):
    """For Source Order Viewer testing."""

    node_id: dom.NodeId


class GetsourceorderhighlightobjectfortestResult(CDPModel):
    highlight: dict[str, Any]


class HighlightframeParams(CDPModel):
    """Highlights owner element of the frame with given id.
    Deprecated: Doesn't work reliably and cannot be fixed due to process
    separation (the owner node might be in a different process). Determine
    the owner node in the client and use highlightNode."""

    frame_id: page.FrameId
    content_color: dom.RGBA | None = None
    content_outline_color: dom.RGBA | None = None


class HighlightnodeParams(CDPModel):
    """Highlights DOM node with given id or with the given JavaScript object wrapper. Either nodeId or
    objectId must be specified."""

    highlight_config: HighlightConfig
    node_id: dom.NodeId | None = None
    backend_node_id: dom.BackendNodeId | None = None
    object_id: runtime.RemoteObjectId | None = None
    selector: str | None = None


class HighlightquadParams(CDPModel):
    """Highlights given quad. Coordinates are absolute with respect to the main frame viewport."""

    quad: dom.Quad
    color: dom.RGBA | None = None
    outline_color: dom.RGBA | None = None


class HighlightrectParams(CDPModel):
    """Highlights given rectangle. Coordinates are absolute with respect to the main frame viewport.
    Issue: the method does not handle device pixel ratio (DPR) correctly.
    The coordinates currently have to be adjusted by the client
    if DPR is not 1 (see crbug.com/437807128)."""

    x: int
    y: int
    width: int
    height: int
    color: dom.RGBA | None = None
    outline_color: dom.RGBA | None = None


class HighlightsourceorderParams(CDPModel):
    """Highlights the source order of the children of the DOM node with given id or with the given
    JavaScript object wrapper. Either nodeId or objectId must be specified."""

    source_order_config: SourceOrderConfig
    node_id: dom.NodeId | None = None
    backend_node_id: dom.BackendNodeId | None = None
    object_id: runtime.RemoteObjectId | None = None


class SetinspectmodeParams(CDPModel):
    """Enters the 'inspect' mode. In this mode, elements that user is hovering over are highlighted.
    Backend then generates 'inspectNodeRequested' event upon element selection."""

    mode: InspectMode
    highlight_config: HighlightConfig | None = None


class SetshowadhighlightsParams(CDPModel):
    """Highlights owner element of all frames detected to be ads."""

    show: bool


class SetpausedindebuggermessageParams(CDPModel):
    message: str | None = None


class SetshowdebugbordersParams(CDPModel):
    """Requests that backend shows debug borders on layers"""

    show: bool


class SetshowfpscounterParams(CDPModel):
    """Requests that backend shows the FPS counter"""

    show: bool


class SetshowgridoverlaysParams(CDPModel):
    """Highlight multiple elements with the CSS Grid overlay."""

    grid_node_highlight_configs: list[GridNodeHighlightConfig]


class SetshowflexoverlaysParams(CDPModel):
    flex_node_highlight_configs: list[FlexNodeHighlightConfig]


class SetshowscrollsnapoverlaysParams(CDPModel):
    scroll_snap_highlight_configs: list[ScrollSnapHighlightConfig]


class SetshowcontainerqueryoverlaysParams(CDPModel):
    container_query_highlight_configs: list[ContainerQueryHighlightConfig]


class SetshowpaintrectsParams(CDPModel):
    """Requests that backend shows paint rectangles"""

    result: bool


class SetshowlayoutshiftregionsParams(CDPModel):
    """Requests that backend shows layout shift regions"""

    result: bool


class SetshowscrollbottleneckrectsParams(CDPModel):
    """Requests that backend shows scroll bottleneck rects"""

    show: bool


class SetshowhittestbordersParams(CDPModel):
    """Deprecated, no longer has any effect."""

    show: bool


class SetshowwebvitalsParams(CDPModel):
    """Deprecated, no longer has any effect."""

    show: bool


class SetshowviewportsizeonresizeParams(CDPModel):
    """Paints viewport size upon main frame resize."""

    show: bool


class SetshowhingeParams(CDPModel):
    """Add a dual screen device hinge"""

    hinge_config: HingeConfig | None = None


class SetshowisolatedelementsParams(CDPModel):
    """Show elements in isolation mode with overlays."""

    isolated_element_highlight_configs: list[IsolatedElementHighlightConfig]


class SetshowwindowcontrolsoverlayParams(CDPModel):
    """Show Window Controls Overlay for PWA"""

    window_controls_overlay_config: WindowControlsOverlayConfig | None = None
