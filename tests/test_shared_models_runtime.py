from dataclasses import dataclass
from typing import Any

from cdpify.shared.models import CDPModel


@dataclass
class _Child(CDPModel):
    value: int


@dataclass
class _Parent(CDPModel):
    child: _Child | None
    values: list[int] | None = None


@dataclass
class _StringHintsModel(CDPModel):
    value: "int"
    known: "int"


def test_deserialize_nested_models_and_optional_lists() -> None:
    model = _Parent.from_cdp({"child": {"value": 3}, "values": [1, 2, 3]})

    assert model.child is not None
    assert model.child.value == 3
    assert model.values == [1, 2, 3]


def test_construct_handles_missing_required_fields_with_none(caplog) -> None:
    model = _Parent.from_cdp({})

    assert model.child is None
    assert "CDP spec mismatch for _Parent" in caplog.text


def test_deserialization_falls_back_when_get_type_hints_fails(monkeypatch) -> None:
    def _raise_type_hints(_: type[CDPModel]) -> dict[str, Any]:
        raise RuntimeError("boom")

    monkeypatch.setattr("cdpify.shared.models.get_type_hints", _raise_type_hints)

    model = _StringHintsModel.from_cdp({"value": 1, "known": 2})

    assert model.value == 1
    assert model.known == 2


def test_deserialization_keeps_raw_values_when_annotations_cannot_resolve(
    monkeypatch,
) -> None:
    def _raise_type_hints(_: type[CDPModel]) -> dict[str, Any]:
        raise RuntimeError("boom")

    def _raise_eval(_: str, __: dict[str, Any]) -> Any:
        raise NameError("unknown")

    monkeypatch.setattr("cdpify.shared.models.get_type_hints", _raise_type_hints)
    monkeypatch.setattr("builtins.eval", _raise_eval)

    model = _StringHintsModel.from_cdp({"value": 1, "known": 2})

    assert model.value == 1
    assert model.known == 2
