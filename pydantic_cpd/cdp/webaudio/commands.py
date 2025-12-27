"""Generated command models from CDP specification"""
# Domain: WebAudio Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *


class GetrealtimedataParams(CDPModel):
    """Fetch the realtime data from the registered contexts."""

    context_id: GraphObjectId


class GetrealtimedataResult(CDPModel):
    realtime_data: ContextRealtimeData
