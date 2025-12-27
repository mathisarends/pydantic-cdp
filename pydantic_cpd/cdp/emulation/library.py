"""Generated client library from CDP specification"""
# Domain: Emulation Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        AddscreenParams,
        AddscreenResult,
        CanemulateResult,
        GetoverriddensensorinformationParams,
        GetoverriddensensorinformationResult,
        GetscreeninfosResult,
        RemovescreenParams,
        SetautodarkmodeoverrideParams,
        SetautomationoverrideParams,
        SetcputhrottlingrateParams,
        SetdatasaveroverrideParams,
        SetdefaultbackgroundcoloroverrideParams,
        SetdevicemetricsoverrideParams,
        SetdevicepostureoverrideParams,
        SetdisabledimagetypesParams,
        SetdisplayfeaturesoverrideParams,
        SetdocumentcookiedisabledParams,
        SetemittoucheventsformouseParams,
        SetemulatedmediaParams,
        SetemulatedostextscaleParams,
        SetemulatedvisiondeficiencyParams,
        SetfocusemulationenabledParams,
        SetgeolocationoverrideParams,
        SethardwareconcurrencyoverrideParams,
        SetidleoverrideParams,
        SetlocaleoverrideParams,
        SetnavigatoroverridesParams,
        SetpagescalefactorParams,
        SetpressuredataoverrideParams,
        SetpressuresourceoverrideenabledParams,
        SetpressurestateoverrideParams,
        SetsafeareainsetsoverrideParams,
        SetscriptexecutiondisabledParams,
        SetscrollbarshiddenParams,
        SetsensoroverrideenabledParams,
        SetsensoroverridereadingsParams,
        SetsmallviewportheightdifferenceoverrideParams,
        SettimezoneoverrideParams,
        SettouchemulationenabledParams,
        SetuseragentoverrideParams,
        SetvirtualtimepolicyParams,
        SetvirtualtimepolicyResult,
        SetvisiblesizeParams,
    )


class EmulationClient:
    """This domain emulates different environments for the page."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def can_emulate(
        self, params: None = None, session_id: str | None = None
    ) -> "CanemulateResult":
        """Tells whether emulation is supported."""
        result = await self._client.send_raw(
            method="Emulation.canEmulate",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return CanemulateResult.model_validate(result)

    async def clear_device_metrics_override(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Clears the overridden device metrics."""
        result = await self._client.send_raw(
            method="Emulation.clearDeviceMetricsOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def clear_geolocation_override(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Clears the overridden Geolocation Position and Error."""
        result = await self._client.send_raw(
            method="Emulation.clearGeolocationOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def reset_page_scale_factor(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Requests that page scale factor is reset to initial values."""
        result = await self._client.send_raw(
            method="Emulation.resetPageScaleFactor",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_focus_emulation_enabled(
        self, params: "SetfocusemulationenabledParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables or disables simulating a focused and active page."""
        result = await self._client.send_raw(
            method="Emulation.setFocusEmulationEnabled",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_auto_dark_mode_override(
        self,
        params: "SetautodarkmodeoverrideParams | None" = None,
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Automatically render all web contents using a dark theme."""
        result = await self._client.send_raw(
            method="Emulation.setAutoDarkModeOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_c_p_u_throttling_rate(
        self, params: "SetcputhrottlingrateParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables CPU throttling to emulate slow CPUs."""
        result = await self._client.send_raw(
            method="Emulation.setCPUThrottlingRate",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_default_background_color_override(
        self,
        params: "SetdefaultbackgroundcoloroverrideParams | None" = None,
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Sets or clears an override of the default background color of the frame. This override is used
        if the content does not specify one."""
        result = await self._client.send_raw(
            method="Emulation.setDefaultBackgroundColorOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_safe_area_insets_override(
        self, params: "SetsafeareainsetsoverrideParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Overrides the values for env(safe-area-inset-*) and env(safe-area-max-inset-*). Unset values will cause the
        respective variables to be undefined, even if previously overridden."""
        result = await self._client.send_raw(
            method="Emulation.setSafeAreaInsetsOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_device_metrics_override(
        self, params: "SetdevicemetricsoverrideParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
        window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media
        query results)."""
        result = await self._client.send_raw(
            method="Emulation.setDeviceMetricsOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_device_posture_override(
        self, params: "SetdevicepostureoverrideParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Start reporting the given posture value to the Device Posture API.
        This override can also be set in setDeviceMetricsOverride()."""
        result = await self._client.send_raw(
            method="Emulation.setDevicePostureOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def clear_device_posture_override(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Clears a device posture override set with either setDeviceMetricsOverride()
        or setDevicePostureOverride() and starts using posture information from the
        platform again.
        Does nothing if no override is set."""
        result = await self._client.send_raw(
            method="Emulation.clearDevicePostureOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_display_features_override(
        self, params: "SetdisplayfeaturesoverrideParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Start using the given display features to pupulate the Viewport Segments API.
        This override can also be set in setDeviceMetricsOverride()."""
        result = await self._client.send_raw(
            method="Emulation.setDisplayFeaturesOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def clear_display_features_override(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Clears the display features override set with either setDeviceMetricsOverride()
        or setDisplayFeaturesOverride() and starts using display features from the
        platform again.
        Does nothing if no override is set."""
        result = await self._client.send_raw(
            method="Emulation.clearDisplayFeaturesOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_scrollbars_hidden(
        self, params: "SetscrollbarshiddenParams", session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="Emulation.setScrollbarsHidden",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_document_cookie_disabled(
        self, params: "SetdocumentcookiedisabledParams", session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="Emulation.setDocumentCookieDisabled",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_emit_touch_events_for_mouse(
        self, params: "SetemittoucheventsformouseParams", session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="Emulation.setEmitTouchEventsForMouse",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_emulated_media(
        self,
        params: "SetemulatedmediaParams | None" = None,
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Emulates the given media type or media feature for CSS media queries."""
        result = await self._client.send_raw(
            method="Emulation.setEmulatedMedia",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_emulated_vision_deficiency(
        self, params: "SetemulatedvisiondeficiencyParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Emulates the given vision deficiency."""
        result = await self._client.send_raw(
            method="Emulation.setEmulatedVisionDeficiency",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_emulated_o_s_text_scale(
        self,
        params: "SetemulatedostextscaleParams | None" = None,
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Emulates the given OS text scale."""
        result = await self._client.send_raw(
            method="Emulation.setEmulatedOSTextScale",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_geolocation_override(
        self,
        params: "SetgeolocationoverrideParams | None" = None,
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Overrides the Geolocation Position or Error. Omitting latitude, longitude or
        accuracy emulates position unavailable."""
        result = await self._client.send_raw(
            method="Emulation.setGeolocationOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_overridden_sensor_information(
        self,
        params: "GetoverriddensensorinformationParams",
        session_id: str | None = None,
    ) -> "GetoverriddensensorinformationResult":
        result = await self._client.send_raw(
            method="Emulation.getOverriddenSensorInformation",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetoverriddensensorinformationResult.model_validate(result)

    async def set_sensor_override_enabled(
        self, params: "SetsensoroverrideenabledParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Overrides a platform sensor of a given type. If |enabled| is true, calls to
        Sensor.start() will use a virtual sensor as backend rather than fetching
        data from a real hardware sensor. Otherwise, existing virtual
        sensor-backend Sensor objects will fire an error event and new calls to
        Sensor.start() will attempt to use a real sensor instead."""
        result = await self._client.send_raw(
            method="Emulation.setSensorOverrideEnabled",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_sensor_override_readings(
        self, params: "SetsensoroverridereadingsParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Updates the sensor readings reported by a sensor type previously overridden
        by setSensorOverrideEnabled."""
        result = await self._client.send_raw(
            method="Emulation.setSensorOverrideReadings",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_pressure_source_override_enabled(
        self,
        params: "SetpressuresourceoverrideenabledParams",
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Overrides a pressure source of a given type, as used by the Compute
        Pressure API, so that updates to PressureObserver.observe() are provided
        via setPressureStateOverride instead of being retrieved from
        platform-provided telemetry data."""
        result = await self._client.send_raw(
            method="Emulation.setPressureSourceOverrideEnabled",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_pressure_state_override(
        self, params: "SetpressurestateoverrideParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """TODO: OBSOLETE: To remove when setPressureDataOverride is merged.
        Provides a given pressure state that will be processed and eventually be
        delivered to PressureObserver users. |source| must have been previously
        overridden by setPressureSourceOverrideEnabled."""
        result = await self._client.send_raw(
            method="Emulation.setPressureStateOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_pressure_data_override(
        self, params: "SetpressuredataoverrideParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Provides a given pressure data set that will be processed and eventually be
        delivered to PressureObserver users. |source| must have been previously
        overridden by setPressureSourceOverrideEnabled."""
        result = await self._client.send_raw(
            method="Emulation.setPressureDataOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_idle_override(
        self, params: "SetidleoverrideParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Overrides the Idle state."""
        result = await self._client.send_raw(
            method="Emulation.setIdleOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def clear_idle_override(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Clears Idle state overrides."""
        result = await self._client.send_raw(
            method="Emulation.clearIdleOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_navigator_overrides(
        self, params: "SetnavigatoroverridesParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Overrides value returned by the javascript navigator object."""
        result = await self._client.send_raw(
            method="Emulation.setNavigatorOverrides",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_page_scale_factor(
        self, params: "SetpagescalefactorParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets a specified page scale factor."""
        result = await self._client.send_raw(
            method="Emulation.setPageScaleFactor",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_script_execution_disabled(
        self, params: "SetscriptexecutiondisabledParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Switches script execution in the page."""
        result = await self._client.send_raw(
            method="Emulation.setScriptExecutionDisabled",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_touch_emulation_enabled(
        self, params: "SettouchemulationenabledParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables touch on platforms which do not support them."""
        result = await self._client.send_raw(
            method="Emulation.setTouchEmulationEnabled",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_virtual_time_policy(
        self, params: "SetvirtualtimepolicyParams", session_id: str | None = None
    ) -> "SetvirtualtimepolicyResult":
        """Turns on virtual time for all frames (replacing real-time with a synthetic time source) and sets
        the current virtual time policy.  Note this supersedes any previous time budget."""
        result = await self._client.send_raw(
            method="Emulation.setVirtualTimePolicy",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return SetvirtualtimepolicyResult.model_validate(result)

    async def set_locale_override(
        self,
        params: "SetlocaleoverrideParams | None" = None,
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Overrides default host system locale with the specified one."""
        result = await self._client.send_raw(
            method="Emulation.setLocaleOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_timezone_override(
        self, params: "SettimezoneoverrideParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Overrides default host system timezone with the specified one."""
        result = await self._client.send_raw(
            method="Emulation.setTimezoneOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_visible_size(
        self, params: "SetvisiblesizeParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Resizes the frame/viewport of the page. Note that this does not affect the frame's container
        (e.g. browser window). Can be used to produce screenshots of the specified size. Not supported
        on Android."""
        result = await self._client.send_raw(
            method="Emulation.setVisibleSize",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_disabled_image_types(
        self, params: "SetdisabledimagetypesParams", session_id: str | None = None
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="Emulation.setDisabledImageTypes",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_data_saver_override(
        self,
        params: "SetdatasaveroverrideParams | None" = None,
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Override the value of navigator.connection.saveData"""
        result = await self._client.send_raw(
            method="Emulation.setDataSaverOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_hardware_concurrency_override(
        self,
        params: "SethardwareconcurrencyoverrideParams",
        session_id: str | None = None,
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="Emulation.setHardwareConcurrencyOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_user_agent_override(
        self, params: "SetuseragentoverrideParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Allows overriding user agent with the given string.
        `userAgentMetadata` must be set for Client Hint headers to be sent."""
        result = await self._client.send_raw(
            method="Emulation.setUserAgentOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_automation_override(
        self, params: "SetautomationoverrideParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Allows overriding the automation flag."""
        result = await self._client.send_raw(
            method="Emulation.setAutomationOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_small_viewport_height_difference_override(
        self,
        params: "SetsmallviewportheightdifferenceoverrideParams",
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Allows overriding the difference between the small and large viewport sizes, which determine the
        value of the `svh` and `lvh` unit, respectively. Only supported for top-level frames."""
        result = await self._client.send_raw(
            method="Emulation.setSmallViewportHeightDifferenceOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_screen_infos(
        self, params: None = None, session_id: str | None = None
    ) -> "GetscreeninfosResult":
        """Returns device's screen configuration."""
        result = await self._client.send_raw(
            method="Emulation.getScreenInfos",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetscreeninfosResult.model_validate(result)

    async def add_screen(
        self, params: "AddscreenParams", session_id: str | None = None
    ) -> "AddscreenResult":
        """Add a new screen to the device. Only supported in headless mode."""
        result = await self._client.send_raw(
            method="Emulation.addScreen",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return AddscreenResult.model_validate(result)

    async def remove_screen(
        self, params: "RemovescreenParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Remove screen from the device. Only supported in headless mode."""
        result = await self._client.send_raw(
            method="Emulation.removeScreen",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result
