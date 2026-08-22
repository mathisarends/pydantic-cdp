from cdpify.generator.generators.base import FUTURE_ANNOTATIONS, BaseGenerator
from cdpify.generator.generators.context import GenerationContext
from cdpify.generator.generators.utils import (
    format_docstring,
    map_cdp_type,
    resolve_type,
    to_snake_case,
)
from cdpify.generator.schemas import Domain, Parameter, TypeDefinition

OPTIONAL_OVERRIDES: dict[str, set[str]] = {
    "DocumentSnapshot": {"documentURL", "baseURL"},
    "AXRelatedNode": {"backendDOMNodeId"},
}


class TypesGenerator(BaseGenerator):
    filename = "types.py"

    def generate(self, domain: Domain) -> str:
        ctx = GenerationContext()
        type_defs = self._generate_type_defs(domain.types, ctx)
        cross_domain = ctx.cross_domain_import(type_checking=False)

        sections = [
            self.HEADER,
            FUTURE_ANNOTATIONS,
            self._build_imports(ctx),
            cross_domain,
            type_defs or "# No types defined",
        ]
        return "\n\n".join(filter(None, sections))

    def _build_imports(self, ctx: GenerationContext) -> str:
        return "\n".join(
            filter(
                None,
                [
                    ctx.typing_import(),
                    "from dataclasses import dataclass",
                    "from cdpify.shared.models import CDPModel",
                ],
            )
        )

    def _generate_type_defs(
        self, types: list[TypeDefinition], ctx: GenerationContext
    ) -> str:
        return "\n\n".join(self._render_type_def(t, ctx) for t in types)

    def _render_type_def(self, type_def: TypeDefinition, ctx: GenerationContext) -> str:
        if type_def.enum:
            return self._render_enum(type_def, ctx)
        if type_def.properties:
            return self._render_object(type_def, ctx)
        return self._render_alias(type_def, ctx)

    def _render_enum(self, type_def: TypeDefinition, ctx: GenerationContext) -> str:
        ctx.use_typing("Literal")
        values = ", ".join(f'"{v}"' for v in type_def.enum)

        lines = []
        if type_def.description:
            lines.append(format_docstring(type_def.description, indent=0))
        lines.append(f"{type_def.id} = Literal[{values}]")
        return "\n".join(lines)

    def _render_object(self, type_def: TypeDefinition, ctx: GenerationContext) -> str:
        lines = [
            "@dataclass(kw_only=True, slots=True)",
            f"class {type_def.id}(CDPModel):",
        ]

        if type_def.description:
            lines.extend(
                format_docstring(type_def.description, indent=4).rstrip().splitlines()
            )

        for prop in type_def.properties:
            lines.append(f"    {self._render_field(prop, type_def.id, ctx)}")

        return "\n".join(lines)

    def _render_alias(self, type_def: TypeDefinition, ctx: GenerationContext) -> str:
        py_type = map_cdp_type(
            Parameter(name=type_def.id, type=type_def.type, optional=False)
        )
        ctx.track_type_string(py_type)

        lines = []
        if type_def.description:
            lines.append(format_docstring(type_def.description, indent=0))
        lines.append(f"{type_def.id} = {py_type}")
        return "\n".join(lines)

    def _render_field(
        self, param: Parameter, type_id: str, ctx: GenerationContext
    ) -> str:
        field_name = to_snake_case(param.name)
        py_type = resolve_type(param)

        if param.ref and "." in param.ref:
            ctx.cross_domain_refs.add(param.ref)
        ctx.track_type_string(py_type)

        is_optional = param.optional or param.name in OPTIONAL_OVERRIDES.get(
            type_id, set()
        )
        if is_optional:
            return f"{field_name}: {py_type} | None = None"
        return f"{field_name}: {py_type}"
