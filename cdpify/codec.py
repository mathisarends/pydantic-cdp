import logging
import sys
from dataclasses import MISSING, dataclass, fields, is_dataclass
from functools import cache
from types import UnionType
from typing import Any, Union, get_args, get_origin, get_type_hints

logger = logging.getLogger(__name__)

_CDP_ENABLED_METADATA_KEY = "cdp"
_CDP_NAME_METADATA_KEY = "cdp_name"


@dataclass(frozen=True, slots=True)
class _FieldPlan:
    name: str
    cdp_name: str
    annotation: Any
    init: bool
    required: bool
    wire_enabled: bool


@dataclass(frozen=True, slots=True)
class _ModelPlan:
    fields: tuple[_FieldPlan, ...]
    fields_by_cdp_name: dict[str, _FieldPlan]
    init_field_names: frozenset[str]


def encode_cdp(model: Any) -> dict[str, Any]:
    """Serialize a generated CDP dataclass to its wire representation."""
    plan = _compile_model(type(model))
    encoded: dict[str, Any] = {}

    for model_field in plan.fields:
        if not model_field.wire_enabled:
            continue

        value = getattr(model, model_field.name)
        if value is not None:
            encoded[model_field.cdp_name] = _encode_value(value)

    return encoded


def decode_cdp[T](
    model_type: type[T],
    data: dict[str, Any],
    *,
    cdp_session_id: str | None = None,
) -> T:
    """Construct a generated CDP dataclass from its wire representation."""
    plan = _compile_model(model_type)
    converted: dict[str, Any] = {}

    for cdp_name, value in data.items():
        model_field = plan.fields_by_cdp_name.get(cdp_name)
        if model_field is None:
            continue
        converted[model_field.name] = _decode_value(value, model_field.annotation)

    if "cdp_session_id" in plan.init_field_names:
        converted["cdp_session_id"] = cdp_session_id

    missing = [
        model_field.name
        for model_field in plan.fields
        if model_field.init
        and model_field.required
        and model_field.name not in converted
    ]
    if missing:
        logger.warning(
            "CDP spec mismatch for %s. Missing fields: %s. Data keys: %s",
            model_type.__name__,
            missing,
            list(data.keys()),
        )
        converted.update(dict.fromkeys(missing))

    values = {
        name: value
        for name, value in converted.items()
        if name in plan.init_field_names
    }
    return model_type(**values)


@cache
def _compile_model(model_type: type) -> _ModelPlan:
    if not is_dataclass(model_type):
        raise TypeError(f"Expected a dataclass type, got {model_type!r}")

    resolved_types = _resolve_field_types(model_type)
    field_plans = tuple(
        _FieldPlan(
            name=model_field.name,
            cdp_name=model_field.metadata.get(_CDP_NAME_METADATA_KEY, model_field.name),
            annotation=resolved_types.get(model_field.name, Any),
            init=model_field.init,
            required=(
                model_field.default is MISSING
                and model_field.default_factory is MISSING
            ),
            wire_enabled=model_field.metadata.get(_CDP_ENABLED_METADATA_KEY, True),
        )
        for model_field in fields(model_type)
    )
    return _ModelPlan(
        fields=field_plans,
        fields_by_cdp_name={
            field_plan.cdp_name: field_plan
            for field_plan in field_plans
            if field_plan.wire_enabled
        },
        init_field_names=frozenset(
            field_plan.name for field_plan in field_plans if field_plan.init
        ),
    )


def _resolve_field_types(model_type: type) -> dict[str, Any]:
    try:
        return get_type_hints(model_type)
    except Exception:
        pass

    module = sys.modules.get(model_type.__module__)
    globalns = getattr(module, "__dict__", {}) if module else {}
    resolved: dict[str, Any] = {}

    for model_field in fields(model_type):
        annotation = model_type.__annotations__.get(model_field.name, model_field.type)
        if not isinstance(annotation, str):
            resolved[model_field.name] = annotation
            continue
        try:
            resolved[model_field.name] = eval(annotation, globalns)
        except Exception:
            resolved[model_field.name] = Any

    return resolved


def _encode_value(value: Any) -> Any:
    if is_dataclass(value) and not isinstance(value, type):
        return encode_cdp(value)
    if isinstance(value, (list, tuple)):
        return [_encode_value(item) for item in value]
    if isinstance(value, dict):
        return {key: _encode_value(item) for key, item in value.items()}
    return value


def _decode_value(value: Any, field_type: Any) -> Any:
    if value is None or field_type is Any:
        return value

    origin = get_origin(field_type)
    args = get_args(field_type)

    if origin in (Union, UnionType):
        candidates = tuple(arg for arg in args if arg is not type(None))
        if len(candidates) == 1:
            return _decode_value(value, candidates[0])
        for candidate in candidates:
            if isinstance(value, dict) and _is_dataclass_type(candidate):
                return decode_cdp(candidate, value)
        return value

    if origin is list and args:
        return [_decode_value(item, args[0]) for item in value]

    if origin is dict and len(args) == 2:
        return {key: _decode_value(item, args[1]) for key, item in value.items()}

    if isinstance(value, dict) and _is_dataclass_type(field_type):
        return decode_cdp(field_type, value)

    return value


def _is_dataclass_type(field_type: Any) -> bool:
    try:
        return isinstance(field_type, type) and is_dataclass(field_type)
    except TypeError:
        return False
