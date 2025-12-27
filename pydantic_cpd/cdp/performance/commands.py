"""Generated command models from CDP specification"""
# Domain: Performance Commands

from typing import Literal
from pydantic_cpd.cdp.base import CDPModel

from .types import *


class EnableParams(CDPModel):
    """Enable collecting and reporting metrics."""

    time_domain: Literal["timeTicks", "threadTicks"] | None = None


class SettimedomainParams(CDPModel):
    """Sets time domain to use for collecting and reporting duration metrics.
    Note that this must be called before enabling metrics collection. Calling
    this method while metrics collection is enabled returns an error."""

    time_domain: Literal["timeTicks", "threadTicks"]


class GetmetricsResult(CDPModel):
    metrics: list[Metric]
