"""Generated from CDP specification"""
# Domain: Media
# This domain allows detailed inspection of media elements.

from typing import Any, Literal
from pydantic_cpd.cdp.base import CDPModel

# Players will get an ID that is unique within the agent context.
PlayerId = str

Timestamp = float


class PlayerMessage(CDPModel):
    """Have one type per entry in MediaLogRecord::Type
    Corresponds to kMessage"""

    level: Literal["error", "warning", "info", "debug"]
    message: str


class PlayerProperty(CDPModel):
    """Corresponds to kMediaPropertyChange"""

    name: str
    value: str


class PlayerEvent(CDPModel):
    """Corresponds to kMediaEventTriggered"""

    timestamp: Timestamp
    value: str


class PlayerErrorSourceLocation(CDPModel):
    """Represents logged source line numbers reported in an error.
    NOTE: file and line are from chromium c++ implementation code, not js."""

    file: str
    line: int


class PlayerError(CDPModel):
    """Corresponds to kMediaError"""

    error_type: str
    code: int
    stack: list[PlayerErrorSourceLocation]
    cause: list[PlayerError]
    data: dict[str, Any]


class Player(CDPModel):
    player_id: PlayerId
    dom_node_id: dom.BackendNodeId | None = None
