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


class TestSortedTypingNames:
    def test_empty_returns_empty_tuple(self) -> None:
        assert GenerationContext().sorted_typing_names == ()

    def test_sorts_names(self) -> None:
        ctx = GenerationContext()
        ctx.use_typing("Literal")
        ctx.use_typing("Any")
        ctx.use_typing("TYPE_CHECKING")
        assert ctx.sorted_typing_names == ("Any", "Literal", "TYPE_CHECKING")


class TestSortedLocalTypes:
    def test_empty_returns_empty_tuple(self) -> None:
        assert GenerationContext().sorted_local_types() == ()

    def test_renders_sorted_block(self) -> None:
        ctx = GenerationContext()
        ctx.local_type_refs.update({"Box", "Node", "Color"})
        result = ctx.sorted_local_types()
        assert result == (("Box", None), ("Color", None), ("Node", None))

    def test_applies_aliases(self) -> None:
        ctx = GenerationContext()
        ctx.local_type_refs.add("PageEvent")
        result = ctx.sorted_local_types({"PageEvent": "PageEventType"})
        assert result == (("PageEvent", "PageEventType"),)


class TestCrossDomainModules:
    def test_empty_returns_empty_tuple(self) -> None:
        assert GenerationContext().cross_domain_modules == ()

    def test_returns_sorted_module_names(self) -> None:
        ctx = GenerationContext()
        ctx.cross_domain_refs.update({"DOM.NodeId", "Page.FrameId"})

        assert ctx.cross_domain_modules == ("dom", "page")

    def test_dedupes_domains_with_multiple_refs(self) -> None:
        ctx = GenerationContext()
        ctx.cross_domain_refs.update({"DOM.NodeId", "DOM.Box"})
        assert ctx.cross_domain_modules == ("dom",)
