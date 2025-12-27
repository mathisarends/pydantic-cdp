"""Generated from CDP specification"""
# Domain: Schema
# This domain is deprecated.

from pydantic_cpd.cdp.base import CDPModel


class Domain(CDPModel):
    """Description of the protocol domain."""

    name: str
    version: str
