"""Generated command models from CDP specification"""
# Domain: BackgroundService Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *


class StartobservingParams(CDPModel):
    """Enables event updates for the service."""

    service: ServiceName


class StopobservingParams(CDPModel):
    """Disables event updates for the service."""

    service: ServiceName


class SetrecordingParams(CDPModel):
    """Set the recording state for the service."""

    should_record: bool
    service: ServiceName


class CleareventsParams(CDPModel):
    """Clears all stored data for the service."""

    service: ServiceName
