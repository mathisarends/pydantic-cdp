"""Generated command models from CDP specification"""
# Domain: SystemInfo Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *


class GetinfoResult(CDPModel):
    gpu: GPUInfo
    model_name: str
    model_version: str
    command_line: str


class GetfeaturestateParams(CDPModel):
    """Returns information about the feature state."""

    feature_state: str


class GetfeaturestateResult(CDPModel):
    feature_enabled: bool


class GetprocessinfoResult(CDPModel):
    process_info: list[ProcessInfo]
