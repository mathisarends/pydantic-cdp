"""Generated command models from CDP specification"""
# Domain: Storage Commands

from typing import Any
from pydantic_cpd.cdp.base import CDPModel

from .types import *

from pydantic_cpd.cdp import browser
from pydantic_cpd.cdp import page


class GetstoragekeyforframeParams(CDPModel):
    """Returns a storage key given a frame id.
    Deprecated. Please use Storage.getStorageKey instead."""

    frame_id: page.FrameId


class GetstoragekeyforframeResult(CDPModel):
    storage_key: SerializedStorageKey


class GetstoragekeyParams(CDPModel):
    """Returns storage key for the given frame. If no frame ID is provided,
    the storage key of the target executing this command is returned."""

    frame_id: page.FrameId | None = None


class GetstoragekeyResult(CDPModel):
    storage_key: SerializedStorageKey


class CleardatafororiginParams(CDPModel):
    """Clears storage for origin."""

    origin: str
    storage_types: str


class CleardataforstoragekeyParams(CDPModel):
    """Clears storage for storage key."""

    storage_key: str
    storage_types: str


class GetcookiesParams(CDPModel):
    """Returns all browser cookies."""

    browser_context_id: browser.BrowserContextID | None = None


class GetcookiesResult(CDPModel):
    cookies: list[Network.Cookie]


class SetcookiesParams(CDPModel):
    """Sets given cookies."""

    cookies: list[Network.CookieParam]
    browser_context_id: browser.BrowserContextID | None = None


class ClearcookiesParams(CDPModel):
    """Clears cookies."""

    browser_context_id: browser.BrowserContextID | None = None


class GetusageandquotaParams(CDPModel):
    """Returns usage and quota in bytes."""

    origin: str


class GetusageandquotaResult(CDPModel):
    usage: float
    quota: float
    override_active: bool
    usage_breakdown: list[UsageForType]


class OverridequotafororiginParams(CDPModel):
    """Override quota for the specified origin"""

    origin: str
    quota_size: float | None = None


class TrackcachestoragefororiginParams(CDPModel):
    """Registers origin to be notified when an update occurs to its cache storage list."""

    origin: str


class TrackcachestorageforstoragekeyParams(CDPModel):
    """Registers storage key to be notified when an update occurs to its cache storage list."""

    storage_key: str


class TrackindexeddbfororiginParams(CDPModel):
    """Registers origin to be notified when an update occurs to its IndexedDB."""

    origin: str


class TrackindexeddbforstoragekeyParams(CDPModel):
    """Registers storage key to be notified when an update occurs to its IndexedDB."""

    storage_key: str


class UntrackcachestoragefororiginParams(CDPModel):
    """Unregisters origin from receiving notifications for cache storage."""

    origin: str


class UntrackcachestorageforstoragekeyParams(CDPModel):
    """Unregisters storage key from receiving notifications for cache storage."""

    storage_key: str


class UntrackindexeddbfororiginParams(CDPModel):
    """Unregisters origin from receiving notifications for IndexedDB."""

    origin: str


class UntrackindexeddbforstoragekeyParams(CDPModel):
    """Unregisters storage key from receiving notifications for IndexedDB."""

    storage_key: str


class GettrusttokensResult(CDPModel):
    tokens: list[TrustTokens]


class CleartrusttokensParams(CDPModel):
    """Removes all Trust Tokens issued by the provided issuerOrigin.
    Leaves other stored data, including the issuer's Redemption Records, intact."""

    issuer_origin: str


class CleartrusttokensResult(CDPModel):
    did_delete_tokens: bool


class GetinterestgroupdetailsParams(CDPModel):
    """Gets details for a named interest group."""

    owner_origin: str
    name: str


class GetinterestgroupdetailsResult(CDPModel):
    details: dict[str, Any]


class SetinterestgrouptrackingParams(CDPModel):
    """Enables/Disables issuing of interestGroupAccessed events."""

    enable: bool


class SetinterestgroupauctiontrackingParams(CDPModel):
    """Enables/Disables issuing of interestGroupAuctionEventOccurred and
    interestGroupAuctionNetworkRequestCreated."""

    enable: bool


class GetsharedstoragemetadataParams(CDPModel):
    """Gets metadata for an origin's shared storage."""

    owner_origin: str


class GetsharedstoragemetadataResult(CDPModel):
    metadata: SharedStorageMetadata


class GetsharedstorageentriesParams(CDPModel):
    """Gets the entries in an given origin's shared storage."""

    owner_origin: str


class GetsharedstorageentriesResult(CDPModel):
    entries: list[SharedStorageEntry]


class SetsharedstorageentryParams(CDPModel):
    """Sets entry with `key` and `value` for a given origin's shared storage."""

    owner_origin: str
    key: str
    value: str
    ignore_if_present: bool | None = None


class DeletesharedstorageentryParams(CDPModel):
    """Deletes entry for `key` (if it exists) for a given origin's shared storage."""

    owner_origin: str
    key: str


class ClearsharedstorageentriesParams(CDPModel):
    """Clears all entries for a given origin's shared storage."""

    owner_origin: str


class ResetsharedstoragebudgetParams(CDPModel):
    """Resets the budget for `ownerOrigin` by clearing all budget withdrawals."""

    owner_origin: str


class SetsharedstoragetrackingParams(CDPModel):
    """Enables/disables issuing of sharedStorageAccessed events."""

    enable: bool


class SetstoragebuckettrackingParams(CDPModel):
    """Set tracking for a storage key's buckets."""

    storage_key: str
    enable: bool


class DeletestoragebucketParams(CDPModel):
    """Deletes the Storage Bucket with the given storage key and bucket name."""

    bucket: StorageBucket


class RunbouncetrackingmitigationsResult(CDPModel):
    deleted_sites: list[str]


class SetattributionreportinglocaltestingmodeParams(CDPModel):
    """https://wicg.github.io/attribution-reporting-api/"""

    enabled: bool


class SetattributionreportingtrackingParams(CDPModel):
    """Enables/disables issuing of Attribution Reporting events."""

    enable: bool


class SendpendingattributionreportsResult(CDPModel):
    num_sent: int


class GetrelatedwebsitesetsResult(CDPModel):
    sets: list[RelatedWebsiteSet]


class GetaffectedurlsforthirdpartycookiemetadataParams(CDPModel):
    """Returns the list of URLs from a page and its embedded resources that match
    existing grace period URL pattern rules.
    https://developers.google.com/privacy-sandbox/cookies/temporary-exceptions/grace-period"""

    first_party_url: str
    third_party_urls: list[str]


class GetaffectedurlsforthirdpartycookiemetadataResult(CDPModel):
    matched_urls: list[str]


class SetprotectedaudiencekanonymityParams(CDPModel):
    owner: str
    name: str
    hashes: list[str]
