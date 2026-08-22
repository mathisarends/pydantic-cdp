from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FieldView:
    name: str
    annotation: str
    optional: bool = False


@dataclass(frozen=True, slots=True)
class EnumMemberView:
    name: str
    value: str


@dataclass(frozen=True, slots=True)
class TypeDefinitionView:
    kind: str
    name: str
    docstring: str | None = None
    annotation: str | None = None
    fields: tuple[FieldView, ...] = ()


@dataclass(frozen=True, slots=True)
class ModelView:
    name: str
    base: str
    docstring: str | None = None
    fields: tuple[FieldView, ...] = ()


@dataclass(frozen=True, slots=True)
class MethodView:
    name: str
    parameters: tuple[FieldView, ...]
    return_type: str
    command_member: str
    docstring: str | None = None
    deprecated: bool = False
    params_model: str | None = None
    constructor_args: str = ""
    result_model: str | None = None


@dataclass(frozen=True, slots=True)
class DomainView:
    name: str
    module: str
    property_name: str


@dataclass(frozen=True, slots=True)
class ImportBlockView:
    module: str
    names: tuple[str, ...]
