from pydantic_cpd.generator.models import Domain, TypeDefinition, Parameter
from pydantic_cpd.generator.type_mapper import map_cdp_type, to_snake_case


class TypesGenerator:
    def __init__(self):
        self.cross_domain_refs: set[str] = set()

    def generate(self, domain: Domain) -> str:
        self.cross_domain_refs.clear()

        sections = [
            self._header(domain),
            self._imports(),
        ]

        if self.cross_domain_refs:
            sections.append(self._cross_domain_imports())

        type_defs = self._generate_type_definitions(domain)
        if type_defs:
            sections.append(type_defs)

        return "\n\n".join(sections)

    def _header(self, domain: Domain) -> str:
        lines = ['"""Generated from CDP specification"""', f"# Domain: {domain.domain}"]

        if domain.description:
            lines.extend(self._format_comment(domain.description))

        return "\n".join(lines)

    def _imports(self) -> str:
        return """from typing import Any, Literal
from pydantic_cpd.cdp.base import CDPModel"""

    def _cross_domain_imports(self) -> str:
        lines = []
        for ref in sorted(self.cross_domain_refs):
            domain_name = ref.split(".")[0].lower()
            lines.append(f"from pydantic_cpd.cdp import {domain_name}")
        return "\n".join(lines)

    def _generate_type_definitions(self, domain: Domain) -> str:
        if not domain.types:
            return ""

        type_defs = []
        for type_def in domain.types:
            code = self._generate_single_type(type_def)
            if code:
                type_defs.append(code)

        return "\n\n".join(type_defs)

    def _generate_single_type(self, type_def: TypeDefinition) -> str:
        if type_def.enum:
            return self._create_enum_type(type_def)

        if type_def.properties:
            return self._create_object_model(type_def)

        return self._create_type_alias(type_def)

    def _create_enum_type(self, type_def: TypeDefinition) -> str:
        lines = []

        if type_def.description:
            lines.extend(self._format_comment(type_def.description))

        values = ", ".join(f'"{v}"' for v in type_def.enum)
        lines.append(f"{type_def.id} = Literal[{values}]")

        return "\n".join(lines)

    def _create_object_model(self, type_def: TypeDefinition) -> str:
        lines = [f"class {type_def.id}(CDPModel):"]

        if type_def.description:
            lines.append(f'    """{type_def.description}"""')

        for prop in type_def.properties:
            lines.append(f"    {self._create_field(prop)}")

        return "\n".join(lines)

    def _create_field(self, param: Parameter) -> str:
        field_name = to_snake_case(param.name)
        py_type = self._resolve_type(param)

        if param.ref and "." in param.ref:
            self.cross_domain_refs.add(param.ref)

        return f"{field_name}: {py_type}" + (" = None" if param.optional else "")

    def _resolve_type(self, param: Parameter) -> str:
        if param.ref and "." in param.ref:
            parts = param.ref.split(".")
            domain_lower = parts[0].lower()
            type_name = parts[1]
            base_type = f"{domain_lower}.{type_name}"
        else:
            base_type = map_cdp_type(param)

        if param.optional and " | None" not in base_type:
            return f"{base_type} | None"

        return base_type

    def _format_comment(self, text: str, max_length: int = 88) -> list[str]:
        """Format description text as Python comments with line wrapping."""
        words = text.split()
        lines = []
        current_line = "# "

        for word in words:
            if len(current_line) + len(word) + 1 <= max_length:
                current_line += word + " "
            else:
                lines.append(current_line.rstrip())
                current_line = "# " + word + " "

        if current_line.strip() != "#":
            lines.append(current_line.rstrip())

        return lines

    def _create_type_alias(self, type_def: TypeDefinition) -> str:
        lines = []

        if type_def.description:
            lines.extend(self._format_comment(type_def.description))

        py_type = map_cdp_type(
            Parameter(name=type_def.id, type=type_def.type, optional=False)
        )
        lines.append(f"{type_def.id} = {py_type}")

        return "\n".join(lines)
