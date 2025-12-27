"""Generated event models from CDP specification"""
# Domain: Performance Events

from pydantic_cpd.cdp.base import CDPModel

from .types import *


class MetricsEvent(CDPModel):
    """Current values of the metrics."""

    metrics: list[Metric]
    title: str
