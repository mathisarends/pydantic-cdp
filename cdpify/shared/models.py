import logging
import sys
from dataclasses import MISSING, asdict, dataclass, field, fields, is_dataclass
from typing import Any, Self, get_args, get_origin, get_type_hints

from cdpify.shared.naming import to_cdp_case, to_snake_case

logger = logging.getLogger(__name__)

_CDP_FIELD_METADATA_KEY = "cdp"


@dataclass(kw_only=True, slots=True)
class CDPModel:
    def to_cdp_params(self) -> dict[str, Any]:
        return _serialize_model(self)

    @classmethod
    def from_cdp(
        cls,
        data: dict[str, Any],
        *,
        cdp_session_id: str | None = None,
    ) -> Self:
        return _deserialize_model(cls, data, cdp_session_id=cdp_session_id)


@dataclass(kw_only=True, slots=True)
class CDPEvent(CDPModel):
    cdp_session_id: str | None = field(
        default=None,
        repr=False,
        compare=False,
        metadata={_CDP_FIELD_METADATA_KEY: False},
    )


def _serialize_model(model: CDPModel) -> dict[str, Any]:
    values = asdict(model)
    return {
        to_cdp_case(model_field.name): values[model_field.name]
        for model_field in fields(model)
        if model_field.metadata.get(_CDP_FIELD_METADATA_KEY, True)
        and values[model_field.name] is not None
    }


def _deserialize_model[T: CDPModel](
    model_type: type[T],
    data: dict[str, Any],
    *,
    cdp_session_id: str | None,
) -> T:
    resolved_types = _resolve_field_types(model_type)
    converted: dict[str, Any] = {}

    for cdp_name, value in data.items():
        field_name = to_snake_case(cdp_name)
        field_type = resolved_types.get(field_name)
        if field_type is None:
            continue
        converted[field_name] = _deserialize_value(value, field_type)

    if issubclass(model_type, CDPEvent):
        converted["cdp_session_id"] = cdp_session_id

    return _construct_model(model_type, converted, data)


def _construct_model[T: CDPModel](
    model_type: type[T],
    converted: dict[str, Any],
    data: dict[str, Any],
) -> T:
    init_fields = [
        model_field for model_field in fields(model_type) if model_field.init
    ]
    model_fields = {model_field.name for model_field in init_fields}
    values = {key: value for key, value in converted.items() if key in model_fields}
    missing = [
        model_field.name
        for model_field in init_fields
        if model_field.name not in values
        and model_field.default is MISSING
        and model_field.default_factory is MISSING
    ]

    if missing:
        logger.warning(
            "CDP spec mismatch for %s. Missing fields: %s. Data keys: %s",
            model_type.__name__,
            missing,
            list(data.keys()),
        )
        values.update(dict.fromkeys(missing))

    return model_type(**values)


def _resolve_field_types(model_type: type[CDPModel]) -> dict[str, Any]:
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


def _deserialize_value(value: Any, field_type: Any) -> Any:
    if value is None or field_type is Any:
        return value

    origin = get_origin(field_type)
    args = get_args(field_type)

    if args and type(None) in args:
        non_none_types = [arg for arg in args if arg is not type(None)]
        if len(non_none_types) == 1:
            return _deserialize_value(value, non_none_types[0])

    if origin is list and args:
        return [_deserialize_value(item, args[0]) for item in value]

    if isinstance(value, dict) and _is_cdp_model(field_type):
        return field_type.from_cdp(value)

    return value


def _is_cdp_model(field_type: Any) -> bool:
    try:
        return is_dataclass(field_type) and issubclass(field_type, CDPModel)
    except TypeError:
        return False
