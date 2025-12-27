"""Generated client library from CDP specification"""
# Domain: Storage Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        ClearcookiesParams,
        CleardatafororiginParams,
        CleardataforstoragekeyParams,
        ClearsharedstorageentriesParams,
        CleartrusttokensParams,
        CleartrusttokensResult,
        DeletesharedstorageentryParams,
        DeletestoragebucketParams,
        GetaffectedurlsforthirdpartycookiemetadataParams,
        GetaffectedurlsforthirdpartycookiemetadataResult,
        GetcookiesParams,
        GetcookiesResult,
        GetinterestgroupdetailsParams,
        GetinterestgroupdetailsResult,
        GetrelatedwebsitesetsResult,
        GetsharedstorageentriesParams,
        GetsharedstorageentriesResult,
        GetsharedstoragemetadataParams,
        GetsharedstoragemetadataResult,
        GetstoragekeyParams,
        GetstoragekeyResult,
        GetstoragekeyforframeParams,
        GetstoragekeyforframeResult,
        GettrusttokensResult,
        GetusageandquotaParams,
        GetusageandquotaResult,
        OverridequotafororiginParams,
        ResetsharedstoragebudgetParams,
        RunbouncetrackingmitigationsResult,
        SendpendingattributionreportsResult,
        SetattributionreportinglocaltestingmodeParams,
        SetattributionreportingtrackingParams,
        SetcookiesParams,
        SetinterestgroupauctiontrackingParams,
        SetinterestgrouptrackingParams,
        SetprotectedaudiencekanonymityParams,
        SetsharedstorageentryParams,
        SetsharedstoragetrackingParams,
        SetstoragebuckettrackingParams,
        TrackcachestoragefororiginParams,
        TrackcachestorageforstoragekeyParams,
        TrackindexeddbfororiginParams,
        TrackindexeddbforstoragekeyParams,
        UntrackcachestoragefororiginParams,
        UntrackcachestorageforstoragekeyParams,
        UntrackindexeddbfororiginParams,
        UntrackindexeddbforstoragekeyParams,
    )


class StorageClient:
    """CDP Storage domain client."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def get_storage_key_for_frame(
        self, params: "GetstoragekeyforframeParams", session_id: str | None = None
    ) -> "GetstoragekeyforframeResult":
        """Returns a storage key given a frame id.
        Deprecated. Please use Storage.getStorageKey instead."""
        result = await self._client.send_raw(
            method="Storage.getStorageKeyForFrame",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetstoragekeyforframeResult.model_validate(result)

    async def get_storage_key(
        self, params: "GetstoragekeyParams | None" = None, session_id: str | None = None
    ) -> "GetstoragekeyResult":
        """Returns storage key for the given frame. If no frame ID is provided,
        the storage key of the target executing this command is returned."""
        result = await self._client.send_raw(
            method="Storage.getStorageKey",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetstoragekeyResult.model_validate(result)

    async def clear_data_for_origin(
        self, params: "CleardatafororiginParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Clears storage for origin."""
        result = await self._client.send_raw(
            method="Storage.clearDataForOrigin",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def clear_data_for_storage_key(
        self, params: "CleardataforstoragekeyParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Clears storage for storage key."""
        result = await self._client.send_raw(
            method="Storage.clearDataForStorageKey",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_cookies(
        self, params: "GetcookiesParams | None" = None, session_id: str | None = None
    ) -> "GetcookiesResult":
        """Returns all browser cookies."""
        result = await self._client.send_raw(
            method="Storage.getCookies",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetcookiesResult.model_validate(result)

    async def set_cookies(
        self, params: "SetcookiesParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets given cookies."""
        result = await self._client.send_raw(
            method="Storage.setCookies",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def clear_cookies(
        self, params: "ClearcookiesParams | None" = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Clears cookies."""
        result = await self._client.send_raw(
            method="Storage.clearCookies",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_usage_and_quota(
        self, params: "GetusageandquotaParams", session_id: str | None = None
    ) -> "GetusageandquotaResult":
        """Returns usage and quota in bytes."""
        result = await self._client.send_raw(
            method="Storage.getUsageAndQuota",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetusageandquotaResult.model_validate(result)

    async def override_quota_for_origin(
        self, params: "OverridequotafororiginParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Override quota for the specified origin"""
        result = await self._client.send_raw(
            method="Storage.overrideQuotaForOrigin",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def track_cache_storage_for_origin(
        self, params: "TrackcachestoragefororiginParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Registers origin to be notified when an update occurs to its cache storage list."""
        result = await self._client.send_raw(
            method="Storage.trackCacheStorageForOrigin",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def track_cache_storage_for_storage_key(
        self,
        params: "TrackcachestorageforstoragekeyParams",
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Registers storage key to be notified when an update occurs to its cache storage list."""
        result = await self._client.send_raw(
            method="Storage.trackCacheStorageForStorageKey",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def track_indexed_d_b_for_origin(
        self, params: "TrackindexeddbfororiginParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Registers origin to be notified when an update occurs to its IndexedDB."""
        result = await self._client.send_raw(
            method="Storage.trackIndexedDBForOrigin",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def track_indexed_d_b_for_storage_key(
        self, params: "TrackindexeddbforstoragekeyParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Registers storage key to be notified when an update occurs to its IndexedDB."""
        result = await self._client.send_raw(
            method="Storage.trackIndexedDBForStorageKey",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def untrack_cache_storage_for_origin(
        self,
        params: "UntrackcachestoragefororiginParams",
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Unregisters origin from receiving notifications for cache storage."""
        result = await self._client.send_raw(
            method="Storage.untrackCacheStorageForOrigin",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def untrack_cache_storage_for_storage_key(
        self,
        params: "UntrackcachestorageforstoragekeyParams",
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Unregisters storage key from receiving notifications for cache storage."""
        result = await self._client.send_raw(
            method="Storage.untrackCacheStorageForStorageKey",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def untrack_indexed_d_b_for_origin(
        self, params: "UntrackindexeddbfororiginParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Unregisters origin from receiving notifications for IndexedDB."""
        result = await self._client.send_raw(
            method="Storage.untrackIndexedDBForOrigin",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def untrack_indexed_d_b_for_storage_key(
        self,
        params: "UntrackindexeddbforstoragekeyParams",
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Unregisters storage key from receiving notifications for IndexedDB."""
        result = await self._client.send_raw(
            method="Storage.untrackIndexedDBForStorageKey",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_trust_tokens(
        self, params: None = None, session_id: str | None = None
    ) -> "GettrusttokensResult":
        """Returns the number of stored Trust Tokens per issuer for the
        current browsing context."""
        result = await self._client.send_raw(
            method="Storage.getTrustTokens",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GettrusttokensResult.model_validate(result)

    async def clear_trust_tokens(
        self, params: "CleartrusttokensParams", session_id: str | None = None
    ) -> "CleartrusttokensResult":
        """Removes all Trust Tokens issued by the provided issuerOrigin.
        Leaves other stored data, including the issuer's Redemption Records, intact."""
        result = await self._client.send_raw(
            method="Storage.clearTrustTokens",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return CleartrusttokensResult.model_validate(result)

    async def get_interest_group_details(
        self, params: "GetinterestgroupdetailsParams", session_id: str | None = None
    ) -> "GetinterestgroupdetailsResult":
        """Gets details for a named interest group."""
        result = await self._client.send_raw(
            method="Storage.getInterestGroupDetails",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetinterestgroupdetailsResult.model_validate(result)

    async def set_interest_group_tracking(
        self, params: "SetinterestgrouptrackingParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables/Disables issuing of interestGroupAccessed events."""
        result = await self._client.send_raw(
            method="Storage.setInterestGroupTracking",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_interest_group_auction_tracking(
        self,
        params: "SetinterestgroupauctiontrackingParams",
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Enables/Disables issuing of interestGroupAuctionEventOccurred and
        interestGroupAuctionNetworkRequestCreated."""
        result = await self._client.send_raw(
            method="Storage.setInterestGroupAuctionTracking",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def get_shared_storage_metadata(
        self, params: "GetsharedstoragemetadataParams", session_id: str | None = None
    ) -> "GetsharedstoragemetadataResult":
        """Gets metadata for an origin's shared storage."""
        result = await self._client.send_raw(
            method="Storage.getSharedStorageMetadata",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetsharedstoragemetadataResult.model_validate(result)

    async def get_shared_storage_entries(
        self, params: "GetsharedstorageentriesParams", session_id: str | None = None
    ) -> "GetsharedstorageentriesResult":
        """Gets the entries in an given origin's shared storage."""
        result = await self._client.send_raw(
            method="Storage.getSharedStorageEntries",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetsharedstorageentriesResult.model_validate(result)

    async def set_shared_storage_entry(
        self, params: "SetsharedstorageentryParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets entry with `key` and `value` for a given origin's shared storage."""
        result = await self._client.send_raw(
            method="Storage.setSharedStorageEntry",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def delete_shared_storage_entry(
        self, params: "DeletesharedstorageentryParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Deletes entry for `key` (if it exists) for a given origin's shared storage."""
        result = await self._client.send_raw(
            method="Storage.deleteSharedStorageEntry",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def clear_shared_storage_entries(
        self, params: "ClearsharedstorageentriesParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Clears all entries for a given origin's shared storage."""
        result = await self._client.send_raw(
            method="Storage.clearSharedStorageEntries",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def reset_shared_storage_budget(
        self, params: "ResetsharedstoragebudgetParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Resets the budget for `ownerOrigin` by clearing all budget withdrawals."""
        result = await self._client.send_raw(
            method="Storage.resetSharedStorageBudget",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_shared_storage_tracking(
        self, params: "SetsharedstoragetrackingParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables/disables issuing of sharedStorageAccessed events."""
        result = await self._client.send_raw(
            method="Storage.setSharedStorageTracking",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_storage_bucket_tracking(
        self, params: "SetstoragebuckettrackingParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Set tracking for a storage key's buckets."""
        result = await self._client.send_raw(
            method="Storage.setStorageBucketTracking",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def delete_storage_bucket(
        self, params: "DeletestoragebucketParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Deletes the Storage Bucket with the given storage key and bucket name."""
        result = await self._client.send_raw(
            method="Storage.deleteStorageBucket",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def run_bounce_tracking_mitigations(
        self, params: None = None, session_id: str | None = None
    ) -> "RunbouncetrackingmitigationsResult":
        """Deletes state for sites identified as potential bounce trackers, immediately."""
        result = await self._client.send_raw(
            method="Storage.runBounceTrackingMitigations",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return RunbouncetrackingmitigationsResult.model_validate(result)

    async def set_attribution_reporting_local_testing_mode(
        self,
        params: "SetattributionreportinglocaltestingmodeParams",
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """https://wicg.github.io/attribution-reporting-api/"""
        result = await self._client.send_raw(
            method="Storage.setAttributionReportingLocalTestingMode",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_attribution_reporting_tracking(
        self,
        params: "SetattributionreportingtrackingParams",
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Enables/disables issuing of Attribution Reporting events."""
        result = await self._client.send_raw(
            method="Storage.setAttributionReportingTracking",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def send_pending_attribution_reports(
        self, params: None = None, session_id: str | None = None
    ) -> "SendpendingattributionreportsResult":
        """Sends all pending Attribution Reports immediately, regardless of their
        scheduled report time."""
        result = await self._client.send_raw(
            method="Storage.sendPendingAttributionReports",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return SendpendingattributionreportsResult.model_validate(result)

    async def get_related_website_sets(
        self, params: None = None, session_id: str | None = None
    ) -> "GetrelatedwebsitesetsResult":
        """Returns the effective Related Website Sets in use by this profile for the browser
        session. The effective Related Website Sets will not change during a browser session."""
        result = await self._client.send_raw(
            method="Storage.getRelatedWebsiteSets",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetrelatedwebsitesetsResult.model_validate(result)

    async def get_affected_urls_for_third_party_cookie_metadata(
        self,
        params: "GetaffectedurlsforthirdpartycookiemetadataParams",
        session_id: str | None = None,
    ) -> "GetaffectedurlsforthirdpartycookiemetadataResult":
        """Returns the list of URLs from a page and its embedded resources that match
        existing grace period URL pattern rules.
        https://developers.google.com/privacy-sandbox/cookies/temporary-exceptions/grace-period"""
        result = await self._client.send_raw(
            method="Storage.getAffectedUrlsForThirdPartyCookieMetadata",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetaffectedurlsforthirdpartycookiemetadataResult.model_validate(result)

    async def set_protected_audience_k_anonymity(
        self,
        params: "SetprotectedaudiencekanonymityParams",
        session_id: str | None = None,
    ) -> dict[str, Any]:
        result = await self._client.send_raw(
            method="Storage.setProtectedAudienceKAnonymity",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result
