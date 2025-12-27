"""Generated event models from CDP specification"""
# Domain: Runtime Events

from typing import Any, Literal
from pydantic_cpd.cdp.base import CDPModel

from .types import *


class BindingcalledEvent(CDPModel):
    """Notification is issued every time when binding is called."""

    name: str
    payload: str
    execution_context_id: ExecutionContextId


class ConsoleapicalledEvent(CDPModel):
    """Issued when console API was called."""

    type: Literal[
        "log",
        "debug",
        "info",
        "error",
        "warning",
        "dir",
        "dirxml",
        "table",
        "trace",
        "clear",
        "startGroup",
        "startGroupCollapsed",
        "endGroup",
        "assert",
        "profile",
        "profileEnd",
        "count",
        "timeEnd",
    ]
    args: list[RemoteObject]
    execution_context_id: ExecutionContextId
    timestamp: Timestamp
    stack_trace: StackTrace | None = None
    context: str | None = None


class ExceptionrevokedEvent(CDPModel):
    """Issued when unhandled exception was revoked."""

    reason: str
    exception_id: int


class ExceptionthrownEvent(CDPModel):
    """Issued when exception was thrown and unhandled."""

    timestamp: Timestamp
    exception_details: ExceptionDetails


class ExecutioncontextcreatedEvent(CDPModel):
    """Issued when new execution context is created."""

    context: ExecutionContextDescription


class ExecutioncontextdestroyedEvent(CDPModel):
    """Issued when execution context is destroyed."""

    execution_context_id: ExecutionContextId
    execution_context_unique_id: str


class ExecutioncontextsclearedEvent(CDPModel):
    """Issued when all executionContexts were cleared in browser"""

    pass


class InspectrequestedEvent(CDPModel):
    """Issued when object should be inspected (for example, as a result of inspect() command line API
    call)."""

    object: RemoteObject
    hints: dict[str, Any]
    execution_context_id: ExecutionContextId | None = None
