"""Generated command models from CDP specification"""
# Domain: DeviceOrientation Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *


class SetdeviceorientationoverrideParams(CDPModel):
    """Overrides the Device Orientation."""

    alpha: float
    beta: float
    gamma: float
