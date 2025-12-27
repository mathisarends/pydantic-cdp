"""Generated client library from CDP specification"""
# Domain: Network Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        CanclearbrowsercacheResult,
        CanclearbrowsercookiesResult,
        CanemulatenetworkconditionsResult,
        ConfiguredurablemessagesParams,
        ContinueinterceptedrequestParams,
        DeletecookiesParams,
        EmulatenetworkconditionsParams,
        EmulatenetworkconditionsbyruleParams,
        EmulatenetworkconditionsbyruleResult,
        EnableParams,
        EnablereportingapiParams,
        GetallcookiesResult,
        GetcertificateParams,
        GetcertificateResult,
        GetcookiesParams,
        GetcookiesResult,
        GetrequestpostdataParams,
        GetrequestpostdataResult,
        GetresponsebodyParams,
        GetresponsebodyResult,
        GetresponsebodyforinterceptionParams,
        GetresponsebodyforinterceptionResult,
        GetsecurityisolationstatusParams,
        GetsecurityisolationstatusResult,
        LoadnetworkresourceParams,
        LoadnetworkresourceResult,
        OverridenetworkstateParams,
        ReplayxhrParams,
        SearchinresponsebodyParams,
        SearchinresponsebodyResult,
        SetacceptedencodingsParams,
        SetattachdebugstackParams,
        SetblockedurlsParams,
        SetbypassserviceworkerParams,
        SetcachedisabledParams,
        SetcookieParams,
        SetcookieResult,
        SetcookiecontrolsParams,
        SetcookiesParams,
        SetextrahttpheadersParams,
        SetrequestinterceptionParams,
        SetuseragentoverrideParams,
        StreamresourcecontentParams,
        StreamresourcecontentResult,
        TakeresponsebodyforinterceptionasstreamParams,
        TakeresponsebodyforinterceptionasstreamResult,
    )


class NetworkClient:
    """Network domain allows tracking network activities of the page. It exposes information about http,
    file, data and other requests and responses, their headers, bodies, timing, etc."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def set_accepted_encodings(
        self, params: "SetacceptedencodingsParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets a list of content encodings that will be accepted. Empty list means no encoding is accepted."""
        result = await self._client.send_raw(
            method="Network.setAcceptedEncodings",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def clear_accepted_encodings_override(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Clears accepted encodings set by setAcceptedEncodings"""
        result = await self._client.send_raw(
            method="Network.clearAcceptedEncodingsOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def can_clear_browser_cache(
        self, params: None = None, session_id: str | None = None
    ) -> "CanclearbrowsercacheResult":
        """Tells whether clearing browser cache is supported."""
        result = await self._client.send_raw(
            method="Network.canClearBrowserCache",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return CanclearbrowsercacheResult.model_validate(result)

    async def can_clear_browser_cookies(
        self, params: None = None, session_id: str | None = None
    ) -> "CanclearbrowsercookiesResult":
        """Tells whether clearing browser cookies is supported."""
        result = await self._client.send_raw(
            method="Network.canClearBrowserCookies",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return CanclearbrowsercookiesResult.model_validate(result)

    async def can_emulate_network_conditions(
        self, params: None = None, session_id: str | None = None
    ) -> "CanemulatenetworkconditionsResult":
        """Tells whether emulation of network conditions is supported."""
        result = await self._client.send_raw(
            method="Network.canEmulateNetworkConditions",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return CanemulatenetworkconditionsResult.model_validate(result)

    async def clear_browser_cache(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Clears browser cache."""
        result = await self._client.send_raw(
            method="Network.clearBrowserCache",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def clear_browser_cookies(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Clears browser cookies."""
        result = await self._client.send_raw(
            method="Network.clearBrowserCookies",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def continue_intercepted_request(
        self, params: "ContinueinterceptedrequestParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Response to Network.requestIntercepted which either modifies the request to continue with any
        modifications, or blocks it, or completes it with the provided response bytes. If a network
        fetch occurs as a result which encounters a redirect an additional Network.requestIntercepted
        event will be sent with the same InterceptionId.
        Deprecated, use Fetch.continueRequest, Fetch.fulfillRequest and Fetch.failRequest instead."""
        result = await self._client.send_raw(
            method="Network.continueInterceptedRequest",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def delete_cookies(
        self, params: "DeletecookiesParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Deletes browser cookies with matching name and url or domain/path/partitionKey pair."""
        result = await self._client.send_raw(
            method="Network.deleteCookies",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def disable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Disables network tracking, prevents network events from being sent to the client."""
        result = await self._client.send_raw(
            method="Network.disable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def emulate_network_conditions(
        self, params: "EmulatenetworkconditionsParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Activates emulation of network conditions. This command is deprecated in favor of the emulateNetworkConditionsByRule
        and overrideNetworkState commands, which can be used together to the same effect."""
        result = await self._client.send_raw(
            method="Network.emulateNetworkConditions",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def emulate_network_conditions_by_rule(
        self,
        params: "EmulatenetworkconditionsbyruleParams",
        session_id: str | None = None,
    ) -> "EmulatenetworkconditionsbyruleResult":
        """Activates emulation of network conditions for individual requests using URL match patterns. Unlike the deprecated
        Network.emulateNetworkConditions this method does not affect `navigator` state. Use Network.overrideNetworkState to
        explicitly modify `navigator` behavior."""
        result = await self._client.send_raw(
            method="Network.emulateNetworkConditionsByRule",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return EmulatenetworkconditionsbyruleResult.model_validate(result)

    async def override_network_state(
        self, params: "OverridenetworkstateParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Override the state of navigator.onLine and navigator.connection."""
        result = await self._client.send_raw(
            method="Network.overrideNetworkState",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def enable(
        self, params: "EnableParams | None" = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables network tracking, network events will now be delivered to the client."""
        result = await self._client.send_raw(
            method="Network.enable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def configure_durable_messages(
        self,
        params: "ConfiguredurablemessagesParams | None" = None,
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Configures storing response bodies outside of renderer, so that these survive
        a cross-process navigation.
        If maxTotalBufferSize is not set, durable messages are disabled."""
        result = await self._client.send_raw(
            method="Network.configureDurableMessages",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_all_cookies(
        self, params: None = None, session_id: str | None = None
    ) -> "GetallcookiesResult":
        """Returns all browser cookies. Depending on the backend support, will return detailed cookie
        information in the `cookies` field.
        Deprecated. Use Storage.getCookies instead."""
        result = await self._client.send_raw(
            method="Network.getAllCookies",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetallcookiesResult.model_validate(result)

    async def get_certificate(
        self, params: "GetcertificateParams", session_id: str | None = None
    ) -> "GetcertificateResult":
        """Returns the DER-encoded certificate."""
        result = await self._client.send_raw(
            method="Network.getCertificate",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetcertificateResult.model_validate(result)

    async def get_cookies(
        self, params: "GetcookiesParams | None" = None, session_id: str | None = None
    ) -> "GetcookiesResult":
        """Returns all browser cookies for the current URL. Depending on the backend support, will return
        detailed cookie information in the `cookies` field."""
        result = await self._client.send_raw(
            method="Network.getCookies",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetcookiesResult.model_validate(result)

    async def get_response_body(
        self, params: "GetresponsebodyParams", session_id: str | None = None
    ) -> "GetresponsebodyResult":
        """Returns content served for the given request."""
        result = await self._client.send_raw(
            method="Network.getResponseBody",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetresponsebodyResult.model_validate(result)

    async def get_request_post_data(
        self, params: "GetrequestpostdataParams", session_id: str | None = None
    ) -> "GetrequestpostdataResult":
        """Returns post data sent with the request. Returns an error when no data was sent with the request."""
        result = await self._client.send_raw(
            method="Network.getRequestPostData",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetrequestpostdataResult.model_validate(result)

    async def get_response_body_for_interception(
        self,
        params: "GetresponsebodyforinterceptionParams",
        session_id: str | None = None,
    ) -> "GetresponsebodyforinterceptionResult":
        """Returns content served for the given currently intercepted request."""
        result = await self._client.send_raw(
            method="Network.getResponseBodyForInterception",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetresponsebodyforinterceptionResult.model_validate(result)

    async def take_response_body_for_interception_as_stream(
        self,
        params: "TakeresponsebodyforinterceptionasstreamParams",
        session_id: str | None = None,
    ) -> "TakeresponsebodyforinterceptionasstreamResult":
        """Returns a handle to the stream representing the response body. Note that after this command,
        the intercepted request can't be continued as is -- you either need to cancel it or to provide
        the response body. The stream only supports sequential read, IO.read will fail if the position
        is specified."""
        result = await self._client.send_raw(
            method="Network.takeResponseBodyForInterceptionAsStream",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return TakeresponsebodyforinterceptionasstreamResult.model_validate(result)

    async def replay_x_h_r(
        self, params: "ReplayxhrParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """This method sends a new XMLHttpRequest which is identical to the original one. The following
        parameters should be identical: method, url, async, request body, extra headers, withCredentials
        attribute, user, password."""
        result = await self._client.send_raw(
            method="Network.replayXHR",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def search_in_response_body(
        self, params: "SearchinresponsebodyParams", session_id: str | None = None
    ) -> "SearchinresponsebodyResult":
        """Searches for given string in response content."""
        result = await self._client.send_raw(
            method="Network.searchInResponseBody",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return SearchinresponsebodyResult.model_validate(result)

    async def set_blocked_u_r_ls(
        self,
        params: "SetblockedurlsParams | None" = None,
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Blocks URLs from loading."""
        result = await self._client.send_raw(
            method="Network.setBlockedURLs",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_bypass_service_worker(
        self, params: "SetbypassserviceworkerParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Toggles ignoring of service worker for each request."""
        result = await self._client.send_raw(
            method="Network.setBypassServiceWorker",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_cache_disabled(
        self, params: "SetcachedisabledParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Toggles ignoring cache for each request. If `true`, cache will not be used."""
        result = await self._client.send_raw(
            method="Network.setCacheDisabled",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_cookie(
        self, params: "SetcookieParams", session_id: str | None = None
    ) -> "SetcookieResult":
        """Sets a cookie with the given cookie data; may overwrite equivalent cookies if they exist."""
        result = await self._client.send_raw(
            method="Network.setCookie",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return SetcookieResult.model_validate(result)

    async def set_cookies(
        self, params: "SetcookiesParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets given cookies."""
        result = await self._client.send_raw(
            method="Network.setCookies",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_extra_h_t_t_p_headers(
        self, params: "SetextrahttpheadersParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Specifies whether to always send extra HTTP headers with the requests from this page."""
        result = await self._client.send_raw(
            method="Network.setExtraHTTPHeaders",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_attach_debug_stack(
        self, params: "SetattachdebugstackParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Specifies whether to attach a page script stack id in requests"""
        result = await self._client.send_raw(
            method="Network.setAttachDebugStack",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_request_interception(
        self, params: "SetrequestinterceptionParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets the requests to intercept that match the provided patterns and optionally resource types.
        Deprecated, please use Fetch.enable instead."""
        result = await self._client.send_raw(
            method="Network.setRequestInterception",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_user_agent_override(
        self, params: "SetuseragentoverrideParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Allows overriding user agent with the given string."""
        result = await self._client.send_raw(
            method="Network.setUserAgentOverride",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def stream_resource_content(
        self, params: "StreamresourcecontentParams", session_id: str | None = None
    ) -> "StreamresourcecontentResult":
        """Enables streaming of the response for the given requestId.
        If enabled, the dataReceived event contains the data that was received during streaming."""
        result = await self._client.send_raw(
            method="Network.streamResourceContent",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return StreamresourcecontentResult.model_validate(result)

    async def get_security_isolation_status(
        self,
        params: "GetsecurityisolationstatusParams | None" = None,
        session_id: str | None = None,
    ) -> "GetsecurityisolationstatusResult":
        """Returns information about the COEP/COOP isolation status."""
        result = await self._client.send_raw(
            method="Network.getSecurityIsolationStatus",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetsecurityisolationstatusResult.model_validate(result)

    async def enable_reporting_api(
        self, params: "EnablereportingapiParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables tracking for the Reporting API, events generated by the Reporting API will now be delivered to the client.
        Enabling triggers 'reportingApiReportAdded' for all existing reports."""
        result = await self._client.send_raw(
            method="Network.enableReportingApi",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def load_network_resource(
        self, params: "LoadnetworkresourceParams", session_id: str | None = None
    ) -> "LoadnetworkresourceResult":
        """Fetches the resource and returns the content."""
        result = await self._client.send_raw(
            method="Network.loadNetworkResource",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return LoadnetworkresourceResult.model_validate(result)

    async def set_cookie_controls(
        self, params: "SetcookiecontrolsParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets Controls for third-party cookie access
        Page reload is required before the new cookie behavior will be observed"""
        result = await self._client.send_raw(
            method="Network.setCookieControls",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result
