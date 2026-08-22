from cdpify.generator.generators.base import FUTURE_ANNOTATIONS, BaseGenerator
from cdpify.generator.generators.context import GenerationContext
from cdpify.generator.generators.utils import (
    format_docstring,
    resolve_type,
    to_enum_name,
    to_pascal_case,
    to_snake_case,
)
from cdpify.generator.generators.views import EnumMemberView, FieldView, ModelView
from cdpify.generator.rendering import render_template
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
        models = tuple(self._build_models(domain, aliases, ctx))

        return render_template(
            "events.py.jinja2",
            header=self.HEADER,
            future_annotations=FUTURE_ANNOTATIONS,
            typing_names=ctx.sorted_typing_names,
            local_type_names=tuple(
                f"{name} as {alias}" if alias else name
                for name, alias in ctx.sorted_local_types(aliases)
            ),
            cross_domain_modules=ctx.cross_domain_modules,
            domain_name=domain.domain,
            event_members=tuple(
                EnumMemberView(
                    name=to_enum_name(event.name),
                    value=f"{domain.domain}.{event.name}",
                )
                for event in domain.events
            ),
            models=models,
        )

    def _aliases_for(self, domain: Domain, ctx: GenerationContext) -> dict[str, str]:
        enum_name = f"{domain.domain}Event"
        if enum_name in ctx.local_type_refs:
            return {enum_name: f"{enum_name}Type"}
        return {}

    def _build_models(
        self,
        domain: Domain,
        aliases: dict[str, str],
        ctx: GenerationContext,
    ) -> list[ModelView]:
        return [
            self._build_event_model(event, domain.domain, aliases, ctx)
            for event in domain.events
        ]

    def _build_event_model(
        self,
        event: Event,
        domain_name: str,
        aliases: dict[str, str],
        ctx: GenerationContext,
    ) -> ModelView:
        event_fqn = f"{domain_name}.{event.name}"
        class_name = f"{to_pascal_case(event.name)}Event"
        return ModelView(
            name=class_name,
            base="CDPEvent",
            docstring=(
                format_docstring(event.description, indent=4)
                if event.description
                else None
            ),
            fields=tuple(
                self._build_field_view(param, event_fqn, aliases, ctx)
                for param in event.parameters
            ),
        )

    def _build_field_view(
        self,
        param: Parameter,
        event_fqn: str,
        aliases: dict[str, str],
        ctx: GenerationContext,
    ) -> FieldView:
        field_name = to_snake_case(param.name)
        py_type = aliases.get(resolve_type(param), resolve_type(param))
        ctx.track_type_string(py_type)

        is_optional = param.optional or param.name in OPTIONAL_OVERRIDES.get(
            event_fqn, set()
        )
        return FieldView(field_name, py_type, optional=is_optional)
