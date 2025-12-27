"""Generated client library from CDP specification"""
# Domain: SystemInfo Client

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        GetfeaturestateParams,
        GetfeaturestateResult,
        GetinfoResult,
        GetprocessinfoResult,
    )


class SystemInfoClient:
    """The SystemInfo domain defines methods and events for querying low-level system information."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def get_info(
        self, params: None = None, session_id: str | None = None
    ) -> "GetinfoResult":
        """Returns information about the system."""
        result = await self._client.send_raw(
            method="SystemInfo.getInfo",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetinfoResult.model_validate(result)

    async def get_feature_state(
        self, params: "GetfeaturestateParams", session_id: str | None = None
    ) -> "GetfeaturestateResult":
        """Returns information about the feature state."""
        result = await self._client.send_raw(
            method="SystemInfo.getFeatureState",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetfeaturestateResult.model_validate(result)

    async def get_process_info(
        self, params: None = None, session_id: str | None = None
    ) -> "GetprocessinfoResult":
        """Returns information about all running processes."""
        result = await self._client.send_raw(
            method="SystemInfo.getProcessInfo",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetprocessinfoResult.model_validate(result)
