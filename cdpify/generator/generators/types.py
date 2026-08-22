from cdpify.generator.generators.base import FUTURE_ANNOTATIONS, BaseGenerator
from cdpify.generator.generators.context import GenerationContext
from cdpify.generator.generators.utils import (
    format_docstring,
    map_cdp_type,
    resolve_type,
    to_snake_case,
)
from cdpify.generator.generators.views import FieldView, TypeDefinitionView
from cdpify.generator.rendering import render_template
from cdpify.generator.schemas import Domain, Parameter, TypeDefinition

OPTIONAL_OVERRIDES: dict[str, set[str]] = {
    "DocumentSnapshot": {"documentURL", "baseURL"},
    "AXRelatedNode": {"backendDOMNodeId"},
}


class TypesGenerator(BaseGenerator):
    filename = "types.py"

    def generate(self, domain: Domain) -> str:
        ctx = GenerationContext()
        definitions = tuple(
            self._build_type_view(type_def, ctx) for type_def in domain.types
        )
        return render_template(
            "types.py.jinja2",
            header=self.HEADER,
            future_annotations=FUTURE_ANNOTATIONS,
            typing_names=ctx.sorted_typing_names,
            cross_domain_modules=ctx.cross_domain_modules,
            definitions=definitions,
        )

    def _build_type_view(
        self, type_def: TypeDefinition, ctx: GenerationContext
    ) -> TypeDefinitionView:
        if type_def.enum:
            return self._build_enum_view(type_def, ctx)
        if type_def.properties:
            return self._build_object_view(type_def, ctx)
        return self._build_alias_view(type_def, ctx)

    def _build_enum_view(
        self, type_def: TypeDefinition, ctx: GenerationContext
    ) -> TypeDefinitionView:
        ctx.use_typing("Literal")
        values = ", ".join(f'"{v}"' for v in type_def.enum)
        return TypeDefinitionView(
            kind="enum",
            name=type_def.id,
            annotation=f"Literal[{values}]",
            docstring=self._docstring(type_def.description, indent=0),
        )

    def _build_object_view(
        self, type_def: TypeDefinition, ctx: GenerationContext
    ) -> TypeDefinitionView:
        return TypeDefinitionView(
            kind="object",
            name=type_def.id,
            docstring=self._docstring(type_def.description, indent=4),
            fields=tuple(
                self._build_field_view(prop, type_def.id, ctx)
                for prop in type_def.properties
            ),
        )

    def _build_alias_view(
        self, type_def: TypeDefinition, ctx: GenerationContext
    ) -> TypeDefinitionView:
        py_type = map_cdp_type(
            Parameter(name=type_def.id, type=type_def.type, optional=False)
        )
        ctx.track_type_string(py_type)
        return TypeDefinitionView(
            kind="alias",
            name=type_def.id,
            annotation=py_type,
            docstring=self._docstring(type_def.description, indent=0),
        )

    def _build_field_view(
        self, param: Parameter, type_id: str, ctx: GenerationContext
    ) -> FieldView:
        field_name = to_snake_case(param.name)
        py_type = resolve_type(param)

        if param.ref and "." in param.ref:
            ctx.cross_domain_refs.add(param.ref)
        ctx.track_type_string(py_type)

        is_optional = param.optional or param.name in OPTIONAL_OVERRIDES.get(
            type_id, set()
        )
        return FieldView(field_name, py_type, optional=is_optional)

    def _docstring(self, text: str | None, *, indent: int) -> str | None:
        return format_docstring(text, indent=indent) if text else None
