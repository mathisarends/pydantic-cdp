"""Generated command models from CDP specification"""
# Domain: LayerTree Commands

from typing import Any
from pydantic_cpd.cdp.base import CDPModel

from .types import *

from pydantic_cpd.cdp import dom


class CompositingreasonsParams(CDPModel):
    """Provides the reasons why the given layer was composited."""

    layer_id: LayerId


class CompositingreasonsResult(CDPModel):
    compositing_reasons: list[str]
    compositing_reason_ids: list[str]


class LoadsnapshotParams(CDPModel):
    """Returns the snapshot identifier."""

    tiles: list[PictureTile]


class LoadsnapshotResult(CDPModel):
    snapshot_id: SnapshotId


class MakesnapshotParams(CDPModel):
    """Returns the layer snapshot identifier."""

    layer_id: LayerId


class MakesnapshotResult(CDPModel):
    snapshot_id: SnapshotId


class ProfilesnapshotParams(CDPModel):
    snapshot_id: SnapshotId
    min_repeat_count: int | None = None
    min_duration: float | None = None
    clip_rect: dom.Rect | None = None


class ProfilesnapshotResult(CDPModel):
    timings: list[PaintProfile]


class ReleasesnapshotParams(CDPModel):
    """Releases layer snapshot captured by the back-end."""

    snapshot_id: SnapshotId


class ReplaysnapshotParams(CDPModel):
    """Replays the layer snapshot and returns the resulting bitmap."""

    snapshot_id: SnapshotId
    from_step: int | None = None
    to_step: int | None = None
    scale: float | None = None


class ReplaysnapshotResult(CDPModel):
    data_u_r_l: str


class SnapshotcommandlogParams(CDPModel):
    """Replays the layer snapshot and returns canvas log."""

    snapshot_id: SnapshotId


class SnapshotcommandlogResult(CDPModel):
    command_log: list[dict[str, Any]]
