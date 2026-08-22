from cdpify.generator.generators.context import GenerationContext
from cdpify.generator.schemas import Parameter


class TestTrackTypeString:
    def test_detects_any(self) -> None:
        ctx = GenerationContext()
        ctx.track_type_string("dict[str, Any]")
        assert "Any" in ctx.typing_names

    def test_detects_literal(self) -> None:
        ctx = GenerationContext()
        ctx.track_type_string('Literal["a", "b"]')
        assert "Literal" in ctx.typing_names

    def test_extracts_cross_domain_ref(self) -> None:
        ctx = GenerationContext()
        ctx.track_type_string("dom.NodeId")
        assert ctx.cross_domain_refs == {"dom.NodeId"}

    def test_extracts_multiple_cross_domain_refs(self) -> None:
        ctx = GenerationContext()
        ctx.track_type_string("dict[dom.NodeId, page.FrameId]")
        assert ctx.cross_domain_refs == {"dom.NodeId", "page.FrameId"}

    def test_ignores_plain_strings(self) -> None:
        ctx = GenerationContext()
        ctx.track_type_string("str")
        assert ctx.cross_domain_refs == set()
        assert ctx.typing_names == set()


class TestScanParam:
    def test_local_ref_goes_to_local_refs(self) -> None:
        ctx = GenerationContext()
        ctx.scan_param(Parameter(name="p", ref="NodeId"))
        assert ctx.local_type_refs == {"NodeId"}
        assert ctx.cross_domain_refs == set()

    def test_cross_domain_ref(self) -> None:
        ctx = GenerationContext()
        ctx.scan_param(Parameter(name="p", ref="DOM.NodeId"))
        assert ctx.cross_domain_refs == {"DOM.NodeId"}
        assert ctx.local_type_refs == set()

    def test_array_with_local_ref(self) -> None:
        ctx = GenerationContext()
        ctx.scan_param(Parameter(name="p", type="array", items={"$ref": "Box"}))
        assert ctx.local_type_refs == {"Box"}

    def test_array_with_cross_domain_ref(self) -> None:
        ctx = GenerationContext()
        ctx.scan_param(Parameter(name="p", type="array", items={"$ref": "DOM.NodeId"}))
        assert ctx.cross_domain_refs == {"DOM.NodeId"}

    def test_param_without_ref_or_array_is_ignored(self) -> None:
        ctx = GenerationContext()
        ctx.scan_param(Parameter(name="p", type="string"))
        assert ctx.local_type_refs == set()
        assert ctx.cross_domain_refs == set()


class TestTypingImport:
    def test_empty_returns_empty_string(self) -> None:
        assert GenerationContext().typing_import() == ""

    def test_sorts_names(self) -> None:
        ctx = GenerationContext()
        ctx.use_typing("Literal")
        ctx.use_typing("Any")
        ctx.use_typing("TYPE_CHECKING")
        assert ctx.typing_import() == "from typing import Any, Literal, TYPE_CHECKING"


class TestLocalTypeImport:
    def test_empty_returns_empty(self) -> None:
        assert GenerationContext().local_type_import() == ""

    def test_renders_sorted_block(self) -> None:
        ctx = GenerationContext()
        ctx.local_type_refs.update({"Box", "Node", "Color"})
        result = ctx.local_type_import()
        assert result == "from .types import (\n    Box,\n    Color,\n    Node,\n)"

    def test_applies_aliases(self) -> None:
        ctx = GenerationContext()
        ctx.local_type_refs.add("PageEvent")
        result = ctx.local_type_import({"PageEvent": "PageEventType"})
        assert "PageEvent as PageEventType" in result


class TestCrossDomainImport:
    def test_empty_returns_empty(self) -> None:
        assert GenerationContext().cross_domain_import(type_checking=True) == ""

    def test_type_checking_gates_block_and_flags_typing_name(self) -> None:
        ctx = GenerationContext()
        ctx.cross_domain_refs.update({"DOM.NodeId", "Page.FrameId"})

        result = ctx.cross_domain_import(type_checking=True)

        assert result == "if TYPE_CHECKING:\n    from cdpify.domains import dom, page"
        assert "TYPE_CHECKING" in ctx.typing_names

    def test_without_type_checking_uses_separate_imports(self) -> None:
        ctx = GenerationContext()
        ctx.cross_domain_refs.update({"DOM.NodeId", "Page.FrameId"})

        result = ctx.cross_domain_import(type_checking=False)

        expected = "from cdpify.domains import dom\nfrom cdpify.domains import page"
        assert result == expected
        assert "TYPE_CHECKING" not in ctx.typing_names

    def test_dedupes_domains_with_multiple_refs(self) -> None:
        ctx = GenerationContext()
        ctx.cross_domain_refs.update({"DOM.NodeId", "DOM.Box"})
        result = ctx.cross_domain_import(type_checking=True)
        assert result == "if TYPE_CHECKING:\n    from cdpify.domains import dom"
