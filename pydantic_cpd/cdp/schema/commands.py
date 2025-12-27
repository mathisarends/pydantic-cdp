"""Generated command models from CDP specification"""
# Domain: Schema Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *


class GetdomainsResult(CDPModel):
    domains: list[Domain]
