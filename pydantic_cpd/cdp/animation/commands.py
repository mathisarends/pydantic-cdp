"""Generated command models from CDP specification"""
# Domain: Animation Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *

from pydantic_cpd.cdp import runtime


class GetcurrenttimeParams(CDPModel):
    """Returns the current time of the an animation."""

    id: str


class GetcurrenttimeResult(CDPModel):
    current_time: float


class GetplaybackrateResult(CDPModel):
    playback_rate: float


class ReleaseanimationsParams(CDPModel):
    """Releases a set of animations to no longer be manipulated."""

    animations: list[str]


class ResolveanimationParams(CDPModel):
    """Gets the remote object of the Animation."""

    animation_id: str


class ResolveanimationResult(CDPModel):
    remote_object: runtime.RemoteObject


class SeekanimationsParams(CDPModel):
    """Seek a set of animations to a particular time within each animation."""

    animations: list[str]
    current_time: float


class SetpausedParams(CDPModel):
    """Sets the paused state of a set of animations."""

    animations: list[str]
    paused: bool


class SetplaybackrateParams(CDPModel):
    """Sets the playback rate of the document timeline."""

    playback_rate: float


class SettimingParams(CDPModel):
    """Sets the timing of an animation node."""

    animation_id: str
    duration: float
    delay: float
