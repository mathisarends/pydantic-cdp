from pydantic_cpd.generator.models import Domain, Event, Parameter
from pydantic_cpd.generator.type_mapper import map_cdp_type, to_snake_case


class EventsGenerator:
    def __init__(self):
        self.cross_domain_refs: set[str] = set()

    def generate(self, domain: Domain) -> str:
        self.cross_domain_refs.clear()

        event_models = self._generate_event_models(domain)

        sections = [
            self._header(domain),
            self._imports(bool(event_models)),
        ]

        if self.cross_domain_refs:
            sections.append(self._cross_domain_imports())

        sections.append(event_models if event_models else "# No events defined")

        return "\n\n".join(sections)

    def _header(self, domain: Domain) -> str:
        return f'''"""Generated event models from CDP specification"""
# Domain: {domain.domain} Events'''

    def _imports(self, has_models: bool) -> str:
        lines = [
            "from typing import Any, Literal",
            "from pydantic_cpd.cdp.base import CDPModel",
        ]

        if has_models:
            lines.append("")
            lines.append("from .types import *")

        return "\n".join(lines)

    def _cross_domain_imports(self) -> str:
        domains = {ref.split(".")[0].lower() for ref in self.cross_domain_refs}
        return "\n".join(
            f"from pydantic_cpd.cdp import {domain}" for domain in sorted(domains)
        )

    def _generate_event_models(self, domain: Domain) -> str:
        if not domain.events:
            return ""

        return "\n\n".join(self._create_event_model(event) for event in domain.events)

    def _create_event_model(self, event: Event) -> str:
        class_name = f"{event.name.capitalize()}Event"

        lines = [f"class {class_name}(CDPModel):"]

        if event.description:
            lines.append(f'    """{event.description}"""')

        if event.parameters:
            for param in event.parameters:
                lines.append(f"    {self._create_field(param)}")
        else:
            lines.append("    pass")

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
