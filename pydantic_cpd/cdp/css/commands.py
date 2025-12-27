"""Generated command models from CDP specification"""
# Domain: CSS Commands

from typing import Any
from pydantic_cpd.cdp.base import CDPModel

from .types import *

from pydantic_cpd.cdp import dom
from pydantic_cpd.cdp import page


class AddruleParams(CDPModel):
    """Inserts a new rule with the given `ruleText` in a stylesheet with given `styleSheetId`, at the
    position specified by `location`."""

    style_sheet_id: dom.StyleSheetId
    rule_text: str
    location: SourceRange
    node_for_property_syntax_validation: dom.NodeId | None = None


class AddruleResult(CDPModel):
    rule: CSSRule


class CollectclassnamesParams(CDPModel):
    """Returns all class names from specified stylesheet."""

    style_sheet_id: dom.StyleSheetId


class CollectclassnamesResult(CDPModel):
    class_names: list[str]


class CreatestylesheetParams(CDPModel):
    """Creates a new special "via-inspector" stylesheet in the frame with given `frameId`."""

    frame_id: page.FrameId
    force: bool | None = None


class CreatestylesheetResult(CDPModel):
    style_sheet_id: dom.StyleSheetId


class ForcepseudostateParams(CDPModel):
    """Ensures that the given node will have specified pseudo-classes whenever its style is computed by
    the browser."""

    node_id: dom.NodeId
    forced_pseudo_classes: list[str]


class ForcestartingstyleParams(CDPModel):
    """Ensures that the given node is in its starting-style state."""

    node_id: dom.NodeId
    forced: bool


class GetbackgroundcolorsParams(CDPModel):
    node_id: dom.NodeId


class GetbackgroundcolorsResult(CDPModel):
    background_colors: list[str] | None = None
    computed_font_size: str | None = None
    computed_font_weight: str | None = None


class GetcomputedstylefornodeParams(CDPModel):
    """Returns the computed style for a DOM node identified by `nodeId`."""

    node_id: dom.NodeId


class GetcomputedstylefornodeResult(CDPModel):
    computed_style: list[CSSComputedStyleProperty]
    extra_fields: ComputedStyleExtraFields


class ResolvevaluesParams(CDPModel):
    """Resolve the specified values in the context of the provided element.
    For example, a value of '1em' is evaluated according to the computed
    'font-size' of the element and a value 'calc(1px + 2px)' will be
    resolved to '3px'.
    If the `propertyName` was specified the `values` are resolved as if
    they were property's declaration. If a value cannot be parsed according
    to the provided property syntax, the value is parsed using combined
    syntax as if null `propertyName` was provided. If the value cannot be
    resolved even then, return the provided value without any changes."""

    values: list[str]
    node_id: dom.NodeId
    property_name: str | None = None
    pseudo_type: dom.PseudoType | None = None
    pseudo_identifier: str | None = None


class ResolvevaluesResult(CDPModel):
    results: list[str]


class GetlonghandpropertiesParams(CDPModel):
    shorthand_name: str
    value: str


class GetlonghandpropertiesResult(CDPModel):
    longhand_properties: list[CSSProperty]


class GetinlinestylesfornodeParams(CDPModel):
    """Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM
    attributes) for a DOM node identified by `nodeId`."""

    node_id: dom.NodeId


class GetinlinestylesfornodeResult(CDPModel):
    inline_style: CSSStyle | None = None
    attributes_style: CSSStyle | None = None


class GetanimatedstylesfornodeParams(CDPModel):
    """Returns the styles coming from animations & transitions
    including the animation & transition styles coming from inheritance chain."""

    node_id: dom.NodeId


class GetanimatedstylesfornodeResult(CDPModel):
    animation_styles: list[CSSAnimationStyle] | None = None
    transitions_style: CSSStyle | None = None
    inherited: list[InheritedAnimatedStyleEntry] | None = None


class GetmatchedstylesfornodeParams(CDPModel):
    """Returns requested styles for a DOM node identified by `nodeId`."""

    node_id: dom.NodeId


class GetmatchedstylesfornodeResult(CDPModel):
    inline_style: CSSStyle | None = None
    attributes_style: CSSStyle | None = None
    matched_c_s_s_rules: list[RuleMatch] | None = None
    pseudo_elements: list[PseudoElementMatches] | None = None
    inherited: list[InheritedStyleEntry] | None = None
    inherited_pseudo_elements: list[InheritedPseudoElementMatches] | None = None
    css_keyframes_rules: list[CSSKeyframesRule] | None = None
    css_position_try_rules: list[CSSPositionTryRule] | None = None
    active_position_fallback_index: int | None = None
    css_property_rules: list[CSSPropertyRule] | None = None
    css_property_registrations: list[CSSPropertyRegistration] | None = None
    css_at_rules: list[CSSAtRule] | None = None
    parent_layout_node_id: dom.NodeId | None = None
    css_function_rules: list[CSSFunctionRule] | None = None


class GetenvironmentvariablesResult(CDPModel):
    environment_variables: dict[str, Any]


class GetmediaqueriesResult(CDPModel):
    medias: list[CSSMedia]


class GetplatformfontsfornodeParams(CDPModel):
    """Requests information about platform fonts which we used to render child TextNodes in the given
    node."""

    node_id: dom.NodeId


class GetplatformfontsfornodeResult(CDPModel):
    fonts: list[PlatformFontUsage]


class GetstylesheettextParams(CDPModel):
    """Returns the current textual content for a stylesheet."""

    style_sheet_id: dom.StyleSheetId


class GetstylesheettextResult(CDPModel):
    text: str


class GetlayersfornodeParams(CDPModel):
    """Returns all layers parsed by the rendering engine for the tree scope of a node.
    Given a DOM element identified by nodeId, getLayersForNode returns the root
    layer for the nearest ancestor document or shadow root. The layer root contains
    the full layer tree for the tree scope and their ordering."""

    node_id: dom.NodeId


class GetlayersfornodeResult(CDPModel):
    root_layer: CSSLayerData


class GetlocationforselectorParams(CDPModel):
    """Given a CSS selector text and a style sheet ID, getLocationForSelector
    returns an array of locations of the CSS selector in the style sheet."""

    style_sheet_id: dom.StyleSheetId
    selector_text: str


class GetlocationforselectorResult(CDPModel):
    ranges: list[SourceRange]


class TrackcomputedstyleupdatesfornodeParams(CDPModel):
    """Starts tracking the given node for the computed style updates
    and whenever the computed style is updated for node, it queues
    a `computedStyleUpdated` event with throttling.
    There can only be 1 node tracked for computed style updates
    so passing a new node id removes tracking from the previous node.
    Pass `undefined` to disable tracking."""

    node_id: dom.NodeId | None = None


class TrackcomputedstyleupdatesParams(CDPModel):
    """Starts tracking the given computed styles for updates. The specified array of properties
    replaces the one previously specified. Pass empty array to disable tracking.
    Use takeComputedStyleUpdates to retrieve the list of nodes that had properties modified.
    The changes to computed style properties are only tracked for nodes pushed to the front-end
    by the DOM agent. If no changes to the tracked properties occur after the node has been pushed
    to the front-end, no updates will be issued for the node."""

    properties_to_track: list[CSSComputedStyleProperty]


class TakecomputedstyleupdatesResult(CDPModel):
    node_ids: list[DOM.NodeId]


class SeteffectivepropertyvaluefornodeParams(CDPModel):
    """Find a rule with the given active property for the given node and set the new value for this
    property"""

    node_id: dom.NodeId
    property_name: str
    value: str


class SetpropertyrulepropertynameParams(CDPModel):
    """Modifies the property rule property name."""

    style_sheet_id: dom.StyleSheetId
    range: SourceRange
    property_name: str


class SetpropertyrulepropertynameResult(CDPModel):
    property_name: Value


class SetkeyframekeyParams(CDPModel):
    """Modifies the keyframe rule key text."""

    style_sheet_id: dom.StyleSheetId
    range: SourceRange
    key_text: str


class SetkeyframekeyResult(CDPModel):
    key_text: Value


class SetmediatextParams(CDPModel):
    """Modifies the rule selector."""

    style_sheet_id: dom.StyleSheetId
    range: SourceRange
    text: str


class SetmediatextResult(CDPModel):
    media: CSSMedia


class SetcontainerquerytextParams(CDPModel):
    """Modifies the expression of a container query."""

    style_sheet_id: dom.StyleSheetId
    range: SourceRange
    text: str


class SetcontainerquerytextResult(CDPModel):
    container_query: CSSContainerQuery


class SetsupportstextParams(CDPModel):
    """Modifies the expression of a supports at-rule."""

    style_sheet_id: dom.StyleSheetId
    range: SourceRange
    text: str


class SetsupportstextResult(CDPModel):
    supports: CSSSupports


class SetscopetextParams(CDPModel):
    """Modifies the expression of a scope at-rule."""

    style_sheet_id: dom.StyleSheetId
    range: SourceRange
    text: str


class SetscopetextResult(CDPModel):
    scope: CSSScope


class SetruleselectorParams(CDPModel):
    """Modifies the rule selector."""

    style_sheet_id: dom.StyleSheetId
    range: SourceRange
    selector: str


class SetruleselectorResult(CDPModel):
    selector_list: SelectorList


class SetstylesheettextParams(CDPModel):
    """Sets the new stylesheet text."""

    style_sheet_id: dom.StyleSheetId
    text: str


class SetstylesheettextResult(CDPModel):
    source_map_u_r_l: str | None = None


class SetstyletextsParams(CDPModel):
    """Applies specified style edits one after another in the given order."""

    edits: list[StyleDeclarationEdit]
    node_for_property_syntax_validation: dom.NodeId | None = None


class SetstyletextsResult(CDPModel):
    styles: list[CSSStyle]


class StopruleusagetrackingResult(CDPModel):
    rule_usage: list[RuleUsage]


class TakecoveragedeltaResult(CDPModel):
    coverage: list[RuleUsage]
    timestamp: float


class SetlocalfontsenabledParams(CDPModel):
    """Enables/disables rendering of local CSS fonts (enabled by default)."""

    enabled: bool
