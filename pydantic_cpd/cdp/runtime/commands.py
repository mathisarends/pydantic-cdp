"""Generated command models from CDP specification"""
# Domain: Runtime Commands

from pydantic_cpd.cdp.base import CDPModel

from .types import *


class AwaitpromiseParams(CDPModel):
    """Add handler to promise with given promise object id."""

    promise_object_id: RemoteObjectId
    return_by_value: bool | None = None
    generate_preview: bool | None = None


class AwaitpromiseResult(CDPModel):
    result: RemoteObject
    exception_details: ExceptionDetails | None = None


class CallfunctiononParams(CDPModel):
    """Calls function with given declaration on the given object. Object group of the result is
    inherited from the target object."""

    function_declaration: str
    object_id: RemoteObjectId | None = None
    arguments: list[CallArgument] | None = None
    silent: bool | None = None
    return_by_value: bool | None = None
    generate_preview: bool | None = None
    user_gesture: bool | None = None
    await_promise: bool | None = None
    execution_context_id: ExecutionContextId | None = None
    object_group: str | None = None
    throw_on_side_effect: bool | None = None
    unique_context_id: str | None = None
    serialization_options: SerializationOptions | None = None


class CallfunctiononResult(CDPModel):
    result: RemoteObject
    exception_details: ExceptionDetails | None = None


class CompilescriptParams(CDPModel):
    """Compiles expression."""

    expression: str
    source_u_r_l: str
    persist_script: bool
    execution_context_id: ExecutionContextId | None = None


class CompilescriptResult(CDPModel):
    script_id: ScriptId | None = None
    exception_details: ExceptionDetails | None = None


class EvaluateParams(CDPModel):
    """Evaluates expression on global object."""

    expression: str
    object_group: str | None = None
    include_command_line_a_p_i: bool | None = None
    silent: bool | None = None
    context_id: ExecutionContextId | None = None
    return_by_value: bool | None = None
    generate_preview: bool | None = None
    user_gesture: bool | None = None
    await_promise: bool | None = None
    throw_on_side_effect: bool | None = None
    timeout: TimeDelta | None = None
    disable_breaks: bool | None = None
    repl_mode: bool | None = None
    allow_unsafe_eval_blocked_by_c_s_p: bool | None = None
    unique_context_id: str | None = None
    serialization_options: SerializationOptions | None = None


class EvaluateResult(CDPModel):
    result: RemoteObject
    exception_details: ExceptionDetails | None = None


class GetisolateidResult(CDPModel):
    id: str


class GetheapusageResult(CDPModel):
    used_size: float
    total_size: float
    embedder_heap_used_size: float
    backing_storage_size: float


class GetpropertiesParams(CDPModel):
    """Returns properties of a given object. Object group of the result is inherited from the target
    object."""

    object_id: RemoteObjectId
    own_properties: bool | None = None
    accessor_properties_only: bool | None = None
    generate_preview: bool | None = None
    non_indexed_properties_only: bool | None = None


class GetpropertiesResult(CDPModel):
    result: list[PropertyDescriptor]
    internal_properties: list[InternalPropertyDescriptor] | None = None
    private_properties: list[PrivatePropertyDescriptor] | None = None
    exception_details: ExceptionDetails | None = None


class GloballexicalscopenamesParams(CDPModel):
    """Returns all let, const and class variables from global scope."""

    execution_context_id: ExecutionContextId | None = None


class GloballexicalscopenamesResult(CDPModel):
    names: list[str]


class QueryobjectsParams(CDPModel):
    prototype_object_id: RemoteObjectId
    object_group: str | None = None


class QueryobjectsResult(CDPModel):
    objects: RemoteObject


class ReleaseobjectParams(CDPModel):
    """Releases remote object with given id."""

    object_id: RemoteObjectId


class ReleaseobjectgroupParams(CDPModel):
    """Releases all remote objects that belong to a given group."""

    object_group: str


class RunscriptParams(CDPModel):
    """Runs script with given id in a given context."""

    script_id: ScriptId
    execution_context_id: ExecutionContextId | None = None
    object_group: str | None = None
    silent: bool | None = None
    include_command_line_a_p_i: bool | None = None
    return_by_value: bool | None = None
    generate_preview: bool | None = None
    await_promise: bool | None = None


class RunscriptResult(CDPModel):
    result: RemoteObject
    exception_details: ExceptionDetails | None = None


class SetasynccallstackdepthParams(CDPModel):
    """Enables or disables async call stacks tracking."""

    max_depth: int


class SetcustomobjectformatterenabledParams(CDPModel):
    enabled: bool


class SetmaxcallstacksizetocaptureParams(CDPModel):
    size: int


class AddbindingParams(CDPModel):
    """If executionContextId is empty, adds binding with the given name on the
    global objects of all inspected contexts, including those created later,
    bindings survive reloads.
    Binding function takes exactly one argument, this argument should be string,
    in case of any other input, function throws an exception.
    Each binding function call produces Runtime.bindingCalled notification."""

    name: str
    execution_context_id: ExecutionContextId | None = None
    execution_context_name: str | None = None


class RemovebindingParams(CDPModel):
    """This method does not remove binding function from global object but
    unsubscribes current runtime agent from Runtime.bindingCalled notifications."""

    name: str


class GetexceptiondetailsParams(CDPModel):
    """This method tries to lookup and populate exception details for a
    JavaScript Error object.
    Note that the stackTrace portion of the resulting exceptionDetails will
    only be populated if the Runtime domain was enabled at the time when the
    Error was thrown."""

    error_object_id: RemoteObjectId


class GetexceptiondetailsResult(CDPModel):
    exception_details: ExceptionDetails | None = None
