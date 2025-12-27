"""Generated command models from CDP specification"""
# Domain: Network Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *

from pydantic_cpd.cdp import emulation
from pydantic_cpd.cdp import io
from pydantic_cpd.cdp import page


class SetacceptedencodingsParams(CDPModel):
    """Sets a list of content encodings that will be accepted. Empty list means no encoding is accepted."""

    encodings: list[ContentEncoding]


class CanclearbrowsercacheResult(CDPModel):
    result: bool


class CanclearbrowsercookiesResult(CDPModel):
    result: bool


class CanemulatenetworkconditionsResult(CDPModel):
    result: bool


class ContinueinterceptedrequestParams(CDPModel):
    """Response to Network.requestIntercepted which either modifies the request to continue with any
    modifications, or blocks it, or completes it with the provided response bytes. If a network
    fetch occurs as a result which encounters a redirect an additional Network.requestIntercepted
    event will be sent with the same InterceptionId.
    Deprecated, use Fetch.continueRequest, Fetch.fulfillRequest and Fetch.failRequest instead."""

    interception_id: InterceptionId
    error_reason: ErrorReason | None = None
    raw_response: str | None = None
    url: str | None = None
    method: str | None = None
    post_data: str | None = None
    headers: Headers | None = None
    auth_challenge_response: AuthChallengeResponse | None = None


class DeletecookiesParams(CDPModel):
    """Deletes browser cookies with matching name and url or domain/path/partitionKey pair."""

    name: str
    url: str | None = None
    domain: str | None = None
    path: str | None = None
    partition_key: CookiePartitionKey | None = None


class EmulatenetworkconditionsParams(CDPModel):
    """Activates emulation of network conditions. This command is deprecated in favor of the emulateNetworkConditionsByRule
    and overrideNetworkState commands, which can be used together to the same effect."""

    offline: bool
    latency: float
    download_throughput: float
    upload_throughput: float
    connection_type: ConnectionType | None = None
    packet_loss: float | None = None
    packet_queue_length: int | None = None
    packet_reordering: bool | None = None


class EmulatenetworkconditionsbyruleParams(CDPModel):
    """Activates emulation of network conditions for individual requests using URL match patterns. Unlike the deprecated
    Network.emulateNetworkConditions this method does not affect `navigator` state. Use Network.overrideNetworkState to
    explicitly modify `navigator` behavior."""

    offline: bool
    matched_network_conditions: list[NetworkConditions]


class EmulatenetworkconditionsbyruleResult(CDPModel):
    rule_ids: list[str]


class OverridenetworkstateParams(CDPModel):
    """Override the state of navigator.onLine and navigator.connection."""

    offline: bool
    latency: float
    download_throughput: float
    upload_throughput: float
    connection_type: ConnectionType | None = None


class EnableParams(CDPModel):
    """Enables network tracking, network events will now be delivered to the client."""

    max_total_buffer_size: int | None = None
    max_resource_buffer_size: int | None = None
    max_post_data_size: int | None = None
    report_direct_socket_traffic: bool | None = None
    enable_durable_messages: bool | None = None


class ConfiguredurablemessagesParams(CDPModel):
    """Configures storing response bodies outside of renderer, so that these survive
    a cross-process navigation.
    If maxTotalBufferSize is not set, durable messages are disabled."""

    max_total_buffer_size: int | None = None
    max_resource_buffer_size: int | None = None


class GetallcookiesResult(CDPModel):
    cookies: list[Cookie]


class GetcertificateParams(CDPModel):
    """Returns the DER-encoded certificate."""

    origin: str


class GetcertificateResult(CDPModel):
    table_names: list[str]


class GetcookiesParams(CDPModel):
    """Returns all browser cookies for the current URL. Depending on the backend support, will return
    detailed cookie information in the `cookies` field."""

    urls: list[str] | None = None


class GetcookiesResult(CDPModel):
    cookies: list[Cookie]


class GetresponsebodyParams(CDPModel):
    """Returns content served for the given request."""

    request_id: RequestId


class GetresponsebodyResult(CDPModel):
    body: str
    base64_encoded: bool


class GetrequestpostdataParams(CDPModel):
    """Returns post data sent with the request. Returns an error when no data was sent with the request."""

    request_id: RequestId


class GetrequestpostdataResult(CDPModel):
    post_data: str


class GetresponsebodyforinterceptionParams(CDPModel):
    """Returns content served for the given currently intercepted request."""

    interception_id: InterceptionId


class GetresponsebodyforinterceptionResult(CDPModel):
    body: str
    base64_encoded: bool


class TakeresponsebodyforinterceptionasstreamParams(CDPModel):
    """Returns a handle to the stream representing the response body. Note that after this command,
    the intercepted request can't be continued as is -- you either need to cancel it or to provide
    the response body. The stream only supports sequential read, IO.read will fail if the position
    is specified."""

    interception_id: InterceptionId


class TakeresponsebodyforinterceptionasstreamResult(CDPModel):
    stream: io.StreamHandle


class ReplayxhrParams(CDPModel):
    """This method sends a new XMLHttpRequest which is identical to the original one. The following
    parameters should be identical: method, url, async, request body, extra headers, withCredentials
    attribute, user, password."""

    request_id: RequestId


class SearchinresponsebodyParams(CDPModel):
    """Searches for given string in response content."""

    request_id: RequestId
    query: str
    case_sensitive: bool | None = None
    is_regex: bool | None = None


class SearchinresponsebodyResult(CDPModel):
    result: list[Debugger.SearchMatch]


class SetblockedurlsParams(CDPModel):
    """Blocks URLs from loading."""

    url_patterns: list[BlockPattern] | None = None
    urls: list[str] | None = None


class SetbypassserviceworkerParams(CDPModel):
    """Toggles ignoring of service worker for each request."""

    bypass: bool


class SetcachedisabledParams(CDPModel):
    """Toggles ignoring cache for each request. If `true`, cache will not be used."""

    cache_disabled: bool


class SetcookieParams(CDPModel):
    """Sets a cookie with the given cookie data; may overwrite equivalent cookies if they exist."""

    name: str
    value: str
    url: str | None = None
    domain: str | None = None
    path: str | None = None
    secure: bool | None = None
    http_only: bool | None = None
    same_site: CookieSameSite | None = None
    expires: TimeSinceEpoch | None = None
    priority: CookiePriority | None = None
    same_party: bool | None = None
    source_scheme: CookieSourceScheme | None = None
    source_port: int | None = None
    partition_key: CookiePartitionKey | None = None


class SetcookieResult(CDPModel):
    success: bool


class SetcookiesParams(CDPModel):
    """Sets given cookies."""

    cookies: list[CookieParam]


class SetextrahttpheadersParams(CDPModel):
    """Specifies whether to always send extra HTTP headers with the requests from this page."""

    headers: Headers


class SetattachdebugstackParams(CDPModel):
    """Specifies whether to attach a page script stack id in requests"""

    enabled: bool


class SetrequestinterceptionParams(CDPModel):
    """Sets the requests to intercept that match the provided patterns and optionally resource types.
    Deprecated, please use Fetch.enable instead."""

    patterns: list[RequestPattern]


class SetuseragentoverrideParams(CDPModel):
    """Allows overriding user agent with the given string."""

    user_agent: str
    accept_language: str | None = None
    platform: str | None = None
    user_agent_metadata: emulation.UserAgentMetadata | None = None


class StreamresourcecontentParams(CDPModel):
    """Enables streaming of the response for the given requestId.
    If enabled, the dataReceived event contains the data that was received during streaming."""

    request_id: RequestId


class StreamresourcecontentResult(CDPModel):
    buffered_data: str


class GetsecurityisolationstatusParams(CDPModel):
    """Returns information about the COEP/COOP isolation status."""

    frame_id: page.FrameId | None = None


class GetsecurityisolationstatusResult(CDPModel):
    status: SecurityIsolationStatus


class EnablereportingapiParams(CDPModel):
    """Enables tracking for the Reporting API, events generated by the Reporting API will now be delivered to the client.
    Enabling triggers 'reportingApiReportAdded' for all existing reports."""

    enable: bool


class LoadnetworkresourceParams(CDPModel):
    """Fetches the resource and returns the content."""

    frame_id: page.FrameId | None = None
    url: str
    options: LoadNetworkResourceOptions


class LoadnetworkresourceResult(CDPModel):
    resource: LoadNetworkResourcePageResult


class SetcookiecontrolsParams(CDPModel):
    """Sets Controls for third-party cookie access
    Page reload is required before the new cookie behavior will be observed"""

    enable_third_party_cookie_restriction: bool
    disable_third_party_cookie_metadata: bool
    disable_third_party_cookie_heuristics: bool
