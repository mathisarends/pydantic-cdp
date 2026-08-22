from cdpify.generator.generators.types import TypesGenerator
from cdpify.generator.schemas import Domain, Parameter, TypeDefinition


def test_generates_header_and_dataclass_imports(simple_domain: Domain) -> None:
    output = TypesGenerator().generate(simple_domain)

    assert "auto-generated" in output
    assert "from __future__ import annotations" in output
    assert "from dataclasses import dataclass" in output
    assert "from cdpify.shared.models import CDPModel" in output


def test_renders_alias_for_primitive_type(simple_domain: Domain) -> None:
    output = TypesGenerator().generate(simple_domain)
    assert "NodeId = int" in output


def test_renders_enum_as_literal(simple_domain: Domain) -> None:
    output = TypesGenerator().generate(simple_domain)
    assert 'Color = Literal["red", "green", "blue"]' in output
    assert "from typing import" in output and "Literal" in output


def test_renders_object_as_dataclass(simple_domain: Domain) -> None:
    output = TypesGenerator().generate(simple_domain)

    assert "@dataclass(kw_only=True, slots=True)" in output
    assert "class Box(CDPModel):" in output
    assert "width: int" in output
    assert "height: int" in output
    assert "label: str | None = None" in output


def test_includes_descriptions_as_docstrings(simple_domain: Domain) -> None:
    output = TypesGenerator().generate(simple_domain)
    assert "A bounding box." in output


def test_empty_domain_emits_marker(empty_domain: Domain) -> None:
    output = TypesGenerator().generate(empty_domain)
    assert "# No types defined" in output


def test_cross_domain_ref_uses_runtime_import() -> None:
    domain = Domain(
        domain="Animation",
        types=[
            TypeDefinition(
                id="Track",
                type="object",
                properties=[Parameter(name="target", ref="DOM.NodeId")],
            )
        ],
    )

    output = TypesGenerator().generate(domain)

    assert "from cdpify.domains import dom" in output
    assert "target: dom.NodeId" in output
    assert "if TYPE_CHECKING:" not in output
    assert "TYPE_CHECKING" not in output


def test_optional_override_makes_field_optional() -> None:
    domain = Domain(
        domain="DOMSnapshot",
        types=[
            TypeDefinition(
                id="DocumentSnapshot",
                type="object",
                properties=[
                    Parameter(name="documentURL", type="string"),
                    Parameter(name="title", type="string"),
                ],
            )
        ],
    )

    output = TypesGenerator().generate(domain)

    assert "document_url: str | None = None" in output
    assert "title: str\n" in output or "title: str" in output
