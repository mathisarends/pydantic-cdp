"""Generated command models from CDP specification"""
# Domain: Log Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *


class StartviolationsreportParams(CDPModel):
    """start violation reporting."""

    config: list[ViolationSetting]
