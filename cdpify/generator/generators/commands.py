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
from cdpify.generator.schemas import Command, Domain, Parameter


class CommandsGenerator(BaseGenerator):
    filename = "commands.py"

    def generate(self, domain: Domain) -> str:
        ctx = GenerationContext()
        for command in domain.commands:
            self._scan_command(command, ctx)

        models = tuple(self._build_models(domain.commands, ctx))
        # Cross-domain imports must remain runtime imports so that
        # `get_type_hints()` (used by CDPModel.from_cdp) can resolve forward
        # references like `dom.Rect`. `from __future__ import annotations`
        # defers annotation evaluation, avoiding the circular-import problem
        # until first deserialization.
        return render_template(
            "commands.py.jinja2",
            header=self.HEADER,
            future_annotations=FUTURE_ANNOTATIONS,
            typing_names=ctx.sorted_typing_names,
            local_type_names=tuple(name for name, _ in ctx.sorted_local_types()),
            cross_domain_modules=ctx.cross_domain_modules,
            domain_name=domain.domain,
            command_members=tuple(
                EnumMemberView(
                    name=to_enum_name(command.name),
                    value=f"{domain.domain}.{command.name}",
                )
                for command in domain.commands
            ),
            models=models,
        )

    def _scan_command(self, command: Command, ctx: GenerationContext) -> None:
        for param in command.parameters:
            ctx.scan_param(param)
        for param in command.returns:
            ctx.scan_param(param)

    def _build_models(
        self, commands: list[Command], ctx: GenerationContext
    ) -> list[ModelView]:
        models: list[ModelView] = []
        for command in commands:
            if command.parameters:
                models.append(self._build_params_model(command, ctx))
            if command.returns:
                models.append(self._build_result_model(command, ctx))
        return models

    def _build_params_model(
        self, command: Command, ctx: GenerationContext
    ) -> ModelView:
        return ModelView(
            name=f"{to_pascal_case(command.name)}Params",
            base="CDPModel",
            docstring=(
                format_docstring(command.description, indent=4)
                if command.description
                else None
            ),
            fields=tuple(
                self._build_field_view(param, ctx) for param in command.parameters
            ),
        )

    def _build_result_model(
        self, command: Command, ctx: GenerationContext
    ) -> ModelView:
        return ModelView(
            name=f"{to_pascal_case(command.name)}Result",
            base="CDPModel",
            fields=tuple(
                self._build_field_view(param, ctx) for param in command.returns
            ),
        )

    def _build_field_view(self, param: Parameter, ctx: GenerationContext) -> FieldView:
        field_name = to_snake_case(param.name)
        py_type = resolve_type(param)
        ctx.track_type_string(py_type)
        return FieldView(field_name, py_type, optional=param.optional)
