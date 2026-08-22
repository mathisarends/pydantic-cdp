from cdpify.generator.generators.base import FUTURE_ANNOTATIONS, BaseGenerator
from cdpify.generator.generators.context import GenerationContext
from cdpify.generator.generators.utils import (
    format_docstring,
    resolve_type,
    to_enum_name,
    to_pascal_case,
    to_snake_case,
)
from cdpify.generator.schemas import Domain, Event, Parameter

OPTIONAL_OVERRIDES: dict[str, set[str]] = {
    "Network.requestWillBeSent": {"documentURL"},
}


class EventsGenerator(BaseGenerator):
    filename = "events.py"

    def generate(self, domain: Domain) -> str:
        ctx = GenerationContext()
        for event in domain.events:
            for param in event.parameters:
                ctx.scan_param(param)

        aliases = self._aliases_for(domain, ctx)

        models = self._render_models(domain, aliases, ctx)
        cross_domain = ctx.cross_domain_import(type_checking=False)

        sections = [self.HEADER, FUTURE_ANNOTATIONS]
        if models:
            sections.append(
                self._build_imports(
                    ctx,
                    aliases,
                )
            )
        if cross_domain:
            sections.append(cross_domain)
        if domain.events:
            sections.append(self._render_enum(domain))
        sections.append(models or "# No events defined")

        return "\n\n".join(filter(None, sections))

    def _aliases_for(self, domain: Domain, ctx: GenerationContext) -> dict[str, str]:
        enum_name = f"{domain.domain}Event"
        if enum_name in ctx.local_type_refs:
            return {enum_name: f"{enum_name}Type"}
        return {}

    def _build_imports(
        self,
        ctx: GenerationContext,
        aliases: dict[str, str],
    ) -> str:
        local_imports = ctx.local_type_import(aliases)

        return "\n".join(
            filter(
                None,
                [
                    ctx.typing_import(),
                    "from dataclasses import dataclass",
                    "from enum import StrEnum",
                    "from cdpify.shared.models import CDPEvent",
                    "",
                    local_imports,
                ],
            )
        )

    def _render_enum(self, domain: Domain) -> str:
        lines = [f"class {domain.domain}Event(StrEnum):"]
        for event in domain.events:
            lines.append(
                f'    {to_enum_name(event.name)} = "{domain.domain}.{event.name}"'
            )
        return "\n".join(lines)

    def _render_models(
        self,
        domain: Domain,
        aliases: dict[str, str],
        ctx: GenerationContext,
    ) -> str:
        if not domain.events:
            return ""
        return "\n\n".join(
            self._render_event_model(event, domain.domain, aliases, ctx)
            for event in domain.events
        )

    def _render_event_model(
        self,
        event: Event,
        domain_name: str,
        aliases: dict[str, str],
        ctx: GenerationContext,
    ) -> str:
        event_fqn = f"{domain_name}.{event.name}"
        class_name = f"{to_pascal_case(event.name)}Event"

        lines = [
            "@dataclass(kw_only=True, slots=True)",
            f"class {class_name}(CDPEvent):",
        ]

        if event.description:
            lines.extend(
                format_docstring(event.description, indent=4).rstrip().splitlines()
            )

        if not event.parameters:
            lines.append("    pass")
            return "\n".join(lines)

        for param in event.parameters:
            lines.append(f"    {self._render_field(param, event_fqn, aliases, ctx)}")
        return "\n".join(lines)

    def _render_field(
        self,
        param: Parameter,
        event_fqn: str,
        aliases: dict[str, str],
        ctx: GenerationContext,
    ) -> str:
        field_name = to_snake_case(param.name)
        py_type = aliases.get(resolve_type(param), resolve_type(param))
        ctx.track_type_string(py_type)

        is_optional = param.optional or param.name in OPTIONAL_OVERRIDES.get(
            event_fqn, set()
        )
        if is_optional:
            return f"{field_name}: {py_type} | None = None"
        return f"{field_name}: {py_type}"
