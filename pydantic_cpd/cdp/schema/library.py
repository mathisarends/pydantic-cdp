"""Generated client library from CDP specification"""
# Domain: Schema Client

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import GetdomainsResult


class SchemaClient:
    """This domain is deprecated."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def get_domains(
        self, params: None = None, session_id: str | None = None
    ) -> "GetdomainsResult":
        """Returns supported domains."""
        result = await self._client.send_raw(
            method="Schema.getDomains",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GetdomainsResult.model_validate(result)
