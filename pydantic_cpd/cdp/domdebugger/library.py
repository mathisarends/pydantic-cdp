"""Generated client library from CDP specification"""
# Domain: DOMDebugger Client

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pydantic_cpd.client import CDPClient
    from .commands import (
        GeteventlistenersParams,
        GeteventlistenersResult,
        RemovedombreakpointParams,
        RemoveeventlistenerbreakpointParams,
        RemoveinstrumentationbreakpointParams,
        RemovexhrbreakpointParams,
        SetbreakoncspviolationParams,
        SetdombreakpointParams,
        SeteventlistenerbreakpointParams,
        SetinstrumentationbreakpointParams,
        SetxhrbreakpointParams,
    )


class DOMDebuggerClient:
    """DOM debugging allows setting breakpoints on particular DOM operations and events. JavaScript
    execution will stop on these operations as if there was a regular breakpoint set."""

    def __init__(self, client: "CDPClient") -> None:
        self._client = client

    async def get_event_listeners(
        self, params: "GeteventlistenersParams", session_id: str | None = None
    ) -> "GeteventlistenersResult":
        """Returns event listeners of the given object."""
        result = await self._client.send_raw(
            method="DOMDebugger.getEventListeners",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return GeteventlistenersResult.model_validate(result)

    async def remove_d_o_m_breakpoint(
        self, params: "RemovedombreakpointParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Removes DOM breakpoint that was set using `setDOMBreakpoint`."""
        result = await self._client.send_raw(
            method="DOMDebugger.removeDOMBreakpoint",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def remove_event_listener_breakpoint(
        self,
        params: "RemoveeventlistenerbreakpointParams",
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Removes breakpoint on particular DOM event."""
        result = await self._client.send_raw(
            method="DOMDebugger.removeEventListenerBreakpoint",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def remove_instrumentation_breakpoint(
        self,
        params: "RemoveinstrumentationbreakpointParams",
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Removes breakpoint on particular native event."""
        result = await self._client.send_raw(
            method="DOMDebugger.removeInstrumentationBreakpoint",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def remove_x_h_r_breakpoint(
        self, params: "RemovexhrbreakpointParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Removes breakpoint from XMLHttpRequest."""
        result = await self._client.send_raw(
            method="DOMDebugger.removeXHRBreakpoint",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_break_on_c_s_p_violation(
        self, params: "SetbreakoncspviolationParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets breakpoint on particular CSP violations."""
        result = await self._client.send_raw(
            method="DOMDebugger.setBreakOnCSPViolation",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_d_o_m_breakpoint(
        self, params: "SetdombreakpointParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets breakpoint on particular operation with DOM."""
        result = await self._client.send_raw(
            method="DOMDebugger.setDOMBreakpoint",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_event_listener_breakpoint(
        self, params: "SeteventlistenerbreakpointParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets breakpoint on particular DOM event."""
        result = await self._client.send_raw(
            method="DOMDebugger.setEventListenerBreakpoint",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_instrumentation_breakpoint(
        self,
        params: "SetinstrumentationbreakpointParams",
        session_id: str | None = None,
    ) -> dict[str, Any]:
        """Sets breakpoint on particular native event."""
        result = await self._client.send_raw(
            method="DOMDebugger.setInstrumentationBreakpoint",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result

    async def set_x_h_r_breakpoint(
        self, params: "SetxhrbreakpointParams", session_id: str | None = None
    ) -> dict[str, Any]:
        """Sets breakpoint on XMLHttpRequest."""
        result = await self._client.send_raw(
            method="DOMDebugger.setXHRBreakpoint",
            params=params.to_cdp_params() if params else None,
            session_id=session_id,
        )
        return result
