"""Generated client library from CDP specification"""
# Domain: CSS Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        AddruleParams,
        AddruleResult,
        CollectclassnamesParams,
        CollectclassnamesResult,
        CreatestylesheetParams,
        CreatestylesheetResult,
        ForcepseudostateParams,
        ForcestartingstyleParams,
        GetanimatedstylesfornodeParams,
        GetanimatedstylesfornodeResult,
        GetbackgroundcolorsParams,
        GetbackgroundcolorsResult,
        GetcomputedstylefornodeParams,
        GetcomputedstylefornodeResult,
        GetenvironmentvariablesResult,
        GetinlinestylesfornodeParams,
        GetinlinestylesfornodeResult,
        GetlayersfornodeParams,
        GetlayersfornodeResult,
        GetlocationforselectorParams,
        GetlocationforselectorResult,
        GetlonghandpropertiesParams,
        GetlonghandpropertiesResult,
        GetmatchedstylesfornodeParams,
        GetmatchedstylesfornodeResult,
        GetmediaqueriesResult,
        GetplatformfontsfornodeParams,
        GetplatformfontsfornodeResult,
        GetstylesheettextParams,
        GetstylesheettextResult,
        ResolvevaluesParams,
        ResolvevaluesResult,
        SetcontainerquerytextParams,
        SetcontainerquerytextResult,
        SeteffectivepropertyvaluefornodeParams,
        SetkeyframekeyParams,
        SetkeyframekeyResult,
        SetlocalfontsenabledParams,
        SetmediatextParams,
        SetmediatextResult,
        SetpropertyrulepropertynameParams,
        SetpropertyrulepropertynameResult,
        SetruleselectorParams,
        SetruleselectorResult,
        SetscopetextParams,
        SetscopetextResult,
        SetstylesheettextParams,
        SetstylesheettextResult,
        SetstyletextsParams,
        SetstyletextsResult,
        SetsupportstextParams,
        SetsupportstextResult,
        StopruleusagetrackingResult,
        TakecomputedstyleupdatesResult,
        TakecoveragedeltaResult,
        TrackcomputedstyleupdatesParams,
        TrackcomputedstyleupdatesfornodeParams,
    )


class CSSClient:
    """This domain exposes CSS read/write operations. All CSS objects (stylesheets, rules, and styles)
    have an associated `id` used in subsequent operations on the related object. Each object type has
    a specific `id` structure, and those are not interchangeable between objects of different kinds.
    CSS objects can be loaded using the `get*ForNode()` calls (which accept a DOM node id). A client
    can also keep track of stylesheets via the `styleSheetAdded`/`styleSheetRemoved` events and
    subsequently load the required stylesheet contents using the `getStyleSheet[Text]()` methods."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def add_rule(
        self, params: "AddruleParams", session_id: str | None = None
    ) -> "AddruleResult":
        """Inserts a new rule with the given `ruleText` in a stylesheet with given `styleSheetId`, at the
        position specified by `location`."""
        result = await self._client.send_raw(
            method="CSS.addRule",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return AddruleResult.model_validate(result)

    async def collect_class_names(
        self, params: "CollectclassnamesParams", session_id: str | None = None
    ) -> "CollectclassnamesResult":
        """Returns all class names from specified stylesheet."""
        result = await self._client.send_raw(
            method="CSS.collectClassNames",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return CollectclassnamesResult.model_validate(result)

    async def create_style_sheet(
        self, params: "CreatestylesheetParams", session_id: str | None = None
    ) -> "CreatestylesheetResult":
        """Creates a new special "via-inspector" stylesheet in the frame with given `frameId`."""
        result = await self._client.send_raw(
            method="CSS.createStyleSheet",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return CreatestylesheetResult.model_validate(result)

    async def disable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Disables the CSS agent for the given page."""
        result = await self._client.send_raw(
            method="CSS.disable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def enable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been
        enabled until the result of this command is received."""
        result = await self._client.send_raw(
            method="CSS.enable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def force_pseudo_state(
        self, params: "ForcepseudostateParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Ensures that the given node will have specified pseudo-classes whenever its style is computed by
        the browser."""
        result = await self._client.send_raw(
            method="CSS.forcePseudoState",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def force_starting_style(
        self, params: "ForcestartingstyleParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Ensures that the given node is in its starting-style state."""
        result = await self._client.send_raw(
            method="CSS.forceStartingStyle",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_background_colors(
        self, params: "GetbackgroundcolorsParams", session_id: str | None = None
    ) -> "GetbackgroundcolorsResult":
        result = await self._client.send_raw(
            method="CSS.getBackgroundColors",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetbackgroundcolorsResult.model_validate(result)

    async def get_computed_style_for_node(
        self, params: "GetcomputedstylefornodeParams", session_id: str | None = None
    ) -> "GetcomputedstylefornodeResult":
        """Returns the computed style for a DOM node identified by `nodeId`."""
        result = await self._client.send_raw(
            method="CSS.getComputedStyleForNode",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetcomputedstylefornodeResult.model_validate(result)

    async def resolve_values(
        self, params: "ResolvevaluesParams", session_id: str | None = None
    ) -> "ResolvevaluesResult":
        """Resolve the specified values in the context of the provided element.
        For example, a value of '1em' is evaluated according to the computed
        'font-size' of the element and a value 'calc(1px + 2px)' will be
        resolved to '3px'.
        If the `propertyName` was specified the `values` are resolved as if
        they were property's declaration. If a value cannot be parsed according
        to the provided property syntax, the value is parsed using combined
        syntax as if null `propertyName` was provided. If the value cannot be
        resolved even then, return the provided value without any changes."""
        result = await self._client.send_raw(
            method="CSS.resolveValues",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return ResolvevaluesResult.model_validate(result)

    async def get_longhand_properties(
        self, params: "GetlonghandpropertiesParams", session_id: str | None = None
    ) -> "GetlonghandpropertiesResult":
        result = await self._client.send_raw(
            method="CSS.getLonghandProperties",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetlonghandpropertiesResult.model_validate(result)

    async def get_inline_styles_for_node(
        self, params: "GetinlinestylesfornodeParams", session_id: str | None = None
    ) -> "GetinlinestylesfornodeResult":
        """Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM
        attributes) for a DOM node identified by `nodeId`."""
        result = await self._client.send_raw(
            method="CSS.getInlineStylesForNode",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetinlinestylesfornodeResult.model_validate(result)

    async def get_animated_styles_for_node(
        self, params: "GetanimatedstylesfornodeParams", session_id: str | None = None
    ) -> "GetanimatedstylesfornodeResult":
        """Returns the styles coming from animations & transitions
        including the animation & transition styles coming from inheritance chain."""
        result = await self._client.send_raw(
            method="CSS.getAnimatedStylesForNode",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetanimatedstylesfornodeResult.model_validate(result)

    async def get_matched_styles_for_node(
        self, params: "GetmatchedstylesfornodeParams", session_id: str | None = None
    ) -> "GetmatchedstylesfornodeResult":
        """Returns requested styles for a DOM node identified by `nodeId`."""
        result = await self._client.send_raw(
            method="CSS.getMatchedStylesForNode",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetmatchedstylesfornodeResult.model_validate(result)

    async def get_environment_variables(
        self, params: None = None, session_id: str | None = None
    ) -> "GetenvironmentvariablesResult":
        """Returns the values of the default UA-defined environment variables used in env()"""
        result = await self._client.send_raw(
            method="CSS.getEnvironmentVariables",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetenvironmentvariablesResult.model_validate(result)

    async def get_media_queries(
        self, params: None = None, session_id: str | None = None
    ) -> "GetmediaqueriesResult":
        """Returns all media queries parsed by the rendering engine."""
        result = await self._client.send_raw(
            method="CSS.getMediaQueries",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetmediaqueriesResult.model_validate(result)

    async def get_platform_fonts_for_node(
        self, params: "GetplatformfontsfornodeParams", session_id: str | None = None
    ) -> "GetplatformfontsfornodeResult":
        """Requests information about platform fonts which we used to render child TextNodes in the given
        node."""
        result = await self._client.send_raw(
            method="CSS.getPlatformFontsForNode",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetplatformfontsfornodeResult.model_validate(result)

    async def get_style_sheet_text(
        self, params: "GetstylesheettextParams", session_id: str | None = None
    ) -> "GetstylesheettextResult":
        """Returns the current textual content for a stylesheet."""
        result = await self._client.send_raw(
            method="CSS.getStyleSheetText",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetstylesheettextResult.model_validate(result)

    async def get_layers_for_node(
        self, params: "GetlayersfornodeParams", session_id: str | None = None
    ) -> "GetlayersfornodeResult":
        """Returns all layers parsed by the rendering engine for the tree scope of a node.
        Given a DOM element identified by nodeId, getLayersForNode returns the root
        layer for the nearest ancestor document or shadow root. The layer root contains
        the full layer tree for the tree scope and their ordering."""
        result = await self._client.send_raw(
            method="CSS.getLayersForNode",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetlayersfornodeResult.model_validate(result)

    async def get_location_for_selector(
        self, params: "GetlocationforselectorParams", session_id: str | None = None
    ) -> "GetlocationforselectorResult":
        """Given a CSS selector text and a style sheet ID, getLocationForSelector
        returns an array of locations of the CSS selector in the style sheet."""
        result = await self._client.send_raw(
            method="CSS.getLocationForSelector",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetlocationforselectorResult.model_validate(result)

    async def track_computed_style_updates_for_node(
        self,
        params: "TrackcomputedstyleupdatesfornodeParams | None" = None,
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Starts tracking the given node for the computed style updates
        and whenever the computed style is updated for node, it queues
        a `computedStyleUpdated` event with throttling.
        There can only be 1 node tracked for computed style updates
        so passing a new node id removes tracking from the previous node.
        Pass `undefined` to disable tracking."""
        result = await self._client.send_raw(
            method="CSS.trackComputedStyleUpdatesForNode",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def track_computed_style_updates(
        self, params: "TrackcomputedstyleupdatesParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Starts tracking the given computed styles for updates. The specified array of properties
        replaces the one previously specified. Pass empty array to disable tracking.
        Use takeComputedStyleUpdates to retrieve the list of nodes that had properties modified.
        The changes to computed style properties are only tracked for nodes pushed to the front-end
        by the DOM agent. If no changes to the tracked properties occur after the node has been pushed
        to the front-end, no updates will be issued for the node."""
        result = await self._client.send_raw(
            method="CSS.trackComputedStyleUpdates",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def take_computed_style_updates(
        self, params: None = None, session_id: str | None = None
    ) -> "TakecomputedstyleupdatesResult":
        """Polls the next batch of computed style updates."""
        result = await self._client.send_raw(
            method="CSS.takeComputedStyleUpdates",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return TakecomputedstyleupdatesResult.model_validate(result)

    async def set_effective_property_value_for_node(
        self,
        params: "SeteffectivepropertyvaluefornodeParams",
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Find a rule with the given active property for the given node and set the new value for this
        property"""
        result = await self._client.send_raw(
            method="CSS.setEffectivePropertyValueForNode",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_property_rule_property_name(
        self, params: "SetpropertyrulepropertynameParams", session_id: str | None = None
    ) -> "SetpropertyrulepropertynameResult":
        """Modifies the property rule property name."""
        result = await self._client.send_raw(
            method="CSS.setPropertyRulePropertyName",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return SetpropertyrulepropertynameResult.model_validate(result)

    async def set_keyframe_key(
        self, params: "SetkeyframekeyParams", session_id: str | None = None
    ) -> "SetkeyframekeyResult":
        """Modifies the keyframe rule key text."""
        result = await self._client.send_raw(
            method="CSS.setKeyframeKey",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return SetkeyframekeyResult.model_validate(result)

    async def set_media_text(
        self, params: "SetmediatextParams", session_id: str | None = None
    ) -> "SetmediatextResult":
        """Modifies the rule selector."""
        result = await self._client.send_raw(
            method="CSS.setMediaText",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return SetmediatextResult.model_validate(result)

    async def set_container_query_text(
        self, params: "SetcontainerquerytextParams", session_id: str | None = None
    ) -> "SetcontainerquerytextResult":
        """Modifies the expression of a container query."""
        result = await self._client.send_raw(
            method="CSS.setContainerQueryText",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return SetcontainerquerytextResult.model_validate(result)

    async def set_supports_text(
        self, params: "SetsupportstextParams", session_id: str | None = None
    ) -> "SetsupportstextResult":
        """Modifies the expression of a supports at-rule."""
        result = await self._client.send_raw(
            method="CSS.setSupportsText",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return SetsupportstextResult.model_validate(result)

    async def set_scope_text(
        self, params: "SetscopetextParams", session_id: str | None = None
    ) -> "SetscopetextResult":
        """Modifies the expression of a scope at-rule."""
        result = await self._client.send_raw(
            method="CSS.setScopeText",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return SetscopetextResult.model_validate(result)

    async def set_rule_selector(
        self, params: "SetruleselectorParams", session_id: str | None = None
    ) -> "SetruleselectorResult":
        """Modifies the rule selector."""
        result = await self._client.send_raw(
            method="CSS.setRuleSelector",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return SetruleselectorResult.model_validate(result)

    async def set_style_sheet_text(
        self, params: "SetstylesheettextParams", session_id: str | None = None
    ) -> "SetstylesheettextResult":
        """Sets the new stylesheet text."""
        result = await self._client.send_raw(
            method="CSS.setStyleSheetText",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return SetstylesheettextResult.model_validate(result)

    async def set_style_texts(
        self, params: "SetstyletextsParams", session_id: str | None = None
    ) -> "SetstyletextsResult":
        """Applies specified style edits one after another in the given order."""
        result = await self._client.send_raw(
            method="CSS.setStyleTexts",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return SetstyletextsResult.model_validate(result)

    async def start_rule_usage_tracking(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables the selector recording."""
        result = await self._client.send_raw(
            method="CSS.startRuleUsageTracking",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def stop_rule_usage_tracking(
        self, params: None = None, session_id: str | None = None
    ) -> "StopruleusagetrackingResult":
        """Stop tracking rule usage and return the list of rules that were used since last call to
        `takeCoverageDelta` (or since start of coverage instrumentation)."""
        result = await self._client.send_raw(
            method="CSS.stopRuleUsageTracking",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return StopruleusagetrackingResult.model_validate(result)

    async def take_coverage_delta(
        self, params: None = None, session_id: str | None = None
    ) -> "TakecoveragedeltaResult":
        """Obtain list of rules that became used since last call to this method (or since start of coverage
        instrumentation)."""
        result = await self._client.send_raw(
            method="CSS.takeCoverageDelta",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return TakecoveragedeltaResult.model_validate(result)

    async def set_local_fonts_enabled(
        self, params: "SetlocalfontsenabledParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables/disables rendering of local CSS fonts (enabled by default)."""
        result = await self._client.send_raw(
            method="CSS.setLocalFontsEnabled",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result
