"""Generated command models from CDP specification"""
# Domain: Debugger Commands

from typing import Literal
from pydantic_cpd.cdp.base import CDPModel

from .types import *

from pydantic_cpd.cdp import runtime


class ContinuetolocationParams(CDPModel):
    """Continues execution until specific location is reached."""

    location: Location
    target_call_frames: Literal["any", "current"] | None = None


class EnableParams(CDPModel):
    """Enables debugger for the given page. Clients should not assume that the debugging has been
    enabled until the result for this command is received."""

    max_scripts_cache_size: float | None = None


class EnableResult(CDPModel):
    debugger_id: runtime.UniqueDebuggerId


class EvaluateoncallframeParams(CDPModel):
    """Evaluates expression on a given call frame."""

    call_frame_id: CallFrameId
    expression: str
    object_group: str | None = None
    include_command_line_a_p_i: bool | None = None
    silent: bool | None = None
    return_by_value: bool | None = None
    generate_preview: bool | None = None
    throw_on_side_effect: bool | None = None
    timeout: runtime.TimeDelta | None = None


class EvaluateoncallframeResult(CDPModel):
    result: runtime.RemoteObject
    exception_details: runtime.ExceptionDetails | None = None


class GetpossiblebreakpointsParams(CDPModel):
    """Returns possible locations for breakpoint. scriptId in start and end range locations should be
    the same."""

    start: Location
    end: Location | None = None
    restrict_to_function: bool | None = None


class GetpossiblebreakpointsResult(CDPModel):
    locations: list[BreakLocation]


class GetscriptsourceParams(CDPModel):
    """Returns source for the script with given id."""

    script_id: runtime.ScriptId


class GetscriptsourceResult(CDPModel):
    script_source: str
    bytecode: str | None = None


class DisassemblewasmmoduleParams(CDPModel):
    script_id: runtime.ScriptId


class DisassemblewasmmoduleResult(CDPModel):
    stream_id: str | None = None
    total_number_of_lines: int
    function_body_offsets: list[int]
    chunk: WasmDisassemblyChunk


class NextwasmdisassemblychunkParams(CDPModel):
    """Disassemble the next chunk of lines for the module corresponding to the
    stream. If disassembly is complete, this API will invalidate the streamId
    and return an empty chunk. Any subsequent calls for the now invalid stream
    will return errors."""

    stream_id: str


class NextwasmdisassemblychunkResult(CDPModel):
    chunk: WasmDisassemblyChunk


class GetwasmbytecodeParams(CDPModel):
    """This command is deprecated. Use getScriptSource instead."""

    script_id: runtime.ScriptId


class GetwasmbytecodeResult(CDPModel):
    bytecode: str


class GetstacktraceParams(CDPModel):
    """Returns stack trace with given `stackTraceId`."""

    stack_trace_id: runtime.StackTraceId


class GetstacktraceResult(CDPModel):
    stack_trace: runtime.StackTrace


class PauseonasynccallParams(CDPModel):
    parent_stack_trace_id: runtime.StackTraceId


class RemovebreakpointParams(CDPModel):
    """Removes JavaScript breakpoint."""

    breakpoint_id: BreakpointId


class RestartframeParams(CDPModel):
    """Restarts particular call frame from the beginning. The old, deprecated
    behavior of `restartFrame` is to stay paused and allow further CDP commands
    after a restart was scheduled. This can cause problems with restarting, so
    we now continue execution immediatly after it has been scheduled until we
    reach the beginning of the restarted frame.

    To stay back-wards compatible, `restartFrame` now expects a `mode`
    parameter to be present. If the `mode` parameter is missing, `restartFrame`
    errors out.

    The various return values are deprecated and `callFrames` is always empty.
    Use the call frames from the `Debugger#paused` events instead, that fires
    once V8 pauses at the beginning of the restarted function."""

    call_frame_id: CallFrameId
    mode: Literal["StepInto"] | None = None


class RestartframeResult(CDPModel):
    call_frames: list[CallFrame]
    async_stack_trace: runtime.StackTrace | None = None
    async_stack_trace_id: runtime.StackTraceId | None = None


class ResumeParams(CDPModel):
    """Resumes JavaScript execution."""

    terminate_on_resume: bool | None = None


class SearchincontentParams(CDPModel):
    """Searches for given string in script content."""

    script_id: runtime.ScriptId
    query: str
    case_sensitive: bool | None = None
    is_regex: bool | None = None


class SearchincontentResult(CDPModel):
    result: list[SearchMatch]


class SetasynccallstackdepthParams(CDPModel):
    """Enables or disables async call stacks tracking."""

    max_depth: int


class SetblackboxexecutioncontextsParams(CDPModel):
    """Replace previous blackbox execution contexts with passed ones. Forces backend to skip
    stepping/pausing in scripts in these execution contexts. VM will try to leave blackboxed script by
    performing 'step in' several times, finally resorting to 'step out' if unsuccessful."""

    unique_ids: list[str]


class SetblackboxpatternsParams(CDPModel):
    """Replace previous blackbox patterns with passed ones. Forces backend to skip stepping/pausing in
    scripts with url matching one of the patterns. VM will try to leave blackboxed script by
    performing 'step in' several times, finally resorting to 'step out' if unsuccessful."""

    patterns: list[str]
    skip_anonymous: bool | None = None


class SetblackboxedrangesParams(CDPModel):
    """Makes backend skip steps in the script in blackboxed ranges. VM will try leave blacklisted
    scripts by performing 'step in' several times, finally resorting to 'step out' if unsuccessful.
    Positions array contains positions where blackbox state is changed. First interval isn't
    blackboxed. Array should be sorted."""

    script_id: runtime.ScriptId
    positions: list[ScriptPosition]


class SetbreakpointParams(CDPModel):
    """Sets JavaScript breakpoint at a given location."""

    location: Location
    condition: str | None = None


class SetbreakpointResult(CDPModel):
    breakpoint_id: BreakpointId
    actual_location: Location


class SetinstrumentationbreakpointParams(CDPModel):
    """Sets instrumentation breakpoint."""

    instrumentation: Literal[
        "beforeScriptExecution", "beforeScriptWithSourceMapExecution"
    ]


class SetinstrumentationbreakpointResult(CDPModel):
    breakpoint_id: BreakpointId


class SetbreakpointbyurlParams(CDPModel):
    """Sets JavaScript breakpoint at given location specified either by URL or URL regex. Once this
    command is issued, all existing parsed scripts will have breakpoints resolved and returned in
    `locations` property. Further matching script parsing will result in subsequent
    `breakpointResolved` events issued. This logical breakpoint will survive page reloads."""

    line_number: int
    url: str | None = None
    url_regex: str | None = None
    script_hash: str | None = None
    column_number: int | None = None
    condition: str | None = None


class SetbreakpointbyurlResult(CDPModel):
    breakpoint_id: BreakpointId
    locations: list[Location]


class SetbreakpointonfunctioncallParams(CDPModel):
    """Sets JavaScript breakpoint before each call to the given function.
    If another function was created from the same source as a given one,
    calling it will also trigger the breakpoint."""

    object_id: runtime.RemoteObjectId
    condition: str | None = None


class SetbreakpointonfunctioncallResult(CDPModel):
    breakpoint_id: BreakpointId


class SetbreakpointsactiveParams(CDPModel):
    """Activates / deactivates all breakpoints on the page."""

    active: bool


class SetpauseonexceptionsParams(CDPModel):
    """Defines pause on exceptions state. Can be set to stop on all exceptions, uncaught exceptions,
    or caught exceptions, no exceptions. Initial pause on exceptions state is `none`."""

    state: Literal["none", "caught", "uncaught", "all"]


class SetreturnvalueParams(CDPModel):
    """Changes return value in top frame. Available only at return break position."""

    new_value: runtime.CallArgument


class SetscriptsourceParams(CDPModel):
    """Edits JavaScript source live.

    In general, functions that are currently on the stack can not be edited with
    a single exception: If the edited function is the top-most stack frame and
    that is the only activation of that function on the stack. In this case
    the live edit will be successful and a `Debugger.restartFrame` for the
    top-most function is automatically triggered."""

    script_id: runtime.ScriptId
    script_source: str
    dry_run: bool | None = None
    allow_top_frame_editing: bool | None = None


class SetscriptsourceResult(CDPModel):
    call_frames: list[CallFrame] | None = None
    stack_changed: bool | None = None
    async_stack_trace: runtime.StackTrace | None = None
    async_stack_trace_id: runtime.StackTraceId | None = None
    status: Literal[
        "Ok",
        "CompileError",
        "BlockedByActiveGenerator",
        "BlockedByActiveFunction",
        "BlockedByTopLevelEsModuleChange",
    ]
    exception_details: runtime.ExceptionDetails | None = None


class SetskipallpausesParams(CDPModel):
    """Makes page not interrupt on any pauses (breakpoint, exception, dom exception etc)."""

    skip: bool


class SetvariablevalueParams(CDPModel):
    """Changes value of variable in a callframe. Object-based scopes are not supported and must be
    mutated manually."""

    scope_number: int
    variable_name: str
    new_value: runtime.CallArgument
    call_frame_id: CallFrameId


class StepintoParams(CDPModel):
    """Steps into the function call."""

    break_on_async_call: bool | None = None
    skip_list: list[LocationRange] | None = None


class StepoverParams(CDPModel):
    """Steps over the statement."""

    skip_list: list[LocationRange] | None = None
