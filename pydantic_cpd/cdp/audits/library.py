"""Generated client library from CDP specification"""
# Domain: Audits Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        CheckcontrastParams,
        CheckformsissuesResult,
        GetencodedresponseParams,
        GetencodedresponseResult,
    )


class AuditsClient:
    """Audits domain allows investigation of page violations and possible improvements."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def get_encoded_response(
        self, params: "GetencodedresponseParams", session_id: str | None = None
    ) -> "GetencodedresponseResult":
        """Returns the response body and size if it were re-encoded with the specified settings. Only
        applies to images."""
        result = await self._client.send_raw(
            method="Audits.getEncodedResponse",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetencodedresponseResult.model_validate(result)

    async def disable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Disables issues domain, prevents further issues from being reported to the client."""
        result = await self._client.send_raw(
            method="Audits.disable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def enable(
        self, params: None = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Enables issues domain, sends the issues collected so far to the client by means of the
        `issueAdded` event."""
        result = await self._client.send_raw(
            method="Audits.enable",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def check_contrast(
        self, params: "CheckcontrastParams | None" = None, session_id: str | None = None
    ) -> dict[str, Any]:
        """Runs the contrast check for the target page. Found issues are reported
        using Audits.issueAdded event."""
        result = await self._client.send_raw(
            method="Audits.checkContrast",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def check_forms_issues(
        self, params: None = None, session_id: str | None = None
    ) -> "CheckformsissuesResult":
        """Runs the form issues check for the target page. Found issues are reported
        using Audits.issueAdded event."""
        result = await self._client.send_raw(
            method="Audits.checkFormsIssues",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return CheckformsissuesResult.model_validate(result)
