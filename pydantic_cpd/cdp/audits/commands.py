"""Generated command models from CDP specification"""
# Domain: Audits Commands

from typing import Literal
from pydantic_cpd.cdp.base import CDPModel

from .types import *

from pydantic_cpd.cdp import network


class GetencodedresponseParams(CDPModel):
    """Returns the response body and size if it were re-encoded with the specified settings. Only
    applies to images."""

    request_id: network.RequestId
    encoding: Literal["webp", "jpeg", "png"]
    quality: float | None = None
    size_only: bool | None = None


class GetencodedresponseResult(CDPModel):
    body: str | None = None
    original_size: int
    encoded_size: int


class CheckcontrastParams(CDPModel):
    """Runs the contrast check for the target page. Found issues are reported
    using Audits.issueAdded event."""

    report_a_a_a: bool | None = None


class CheckformsissuesResult(CDPModel):
    form_issues: list[GenericIssueDetails]
