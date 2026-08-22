from cdpify.generator.generators.base import FUTURE_ANNOTATIONS, BaseGenerator
from cdpify.generator.generators.context import GenerationContext
from cdpify.generator.generators.utils import (
    format_docstring,
    resolve_type,
    to_enum_name,
    to_pascal_case,
    to_snake_case,
)
from cdpify.generator.schemas import Command, Domain, Parameter


class CommandsGenerator(BaseGenerator):
    filename = "commands.py"

    def generate(self, domain: Domain) -> str:
        ctx = GenerationContext()
        for command in domain.commands:
            self._scan_command(command, ctx)

        models = self._render_models(domain.commands, ctx)
        # Cross-domain imports must remain runtime imports so that
        # `get_type_hints()` (used by CDPModel.from_cdp) can resolve forward
        # references like `dom.Rect`. `from __future__ import annotations`
        # defers annotation evaluation, avoiding the circular-import problem
        # until first deserialization.
        cross_domain = ctx.cross_domain_import(type_checking=False)

        sections = [
            self.HEADER,
            FUTURE_ANNOTATIONS,
            self._build_imports(ctx),
            cross_domain,
            self._render_enum(domain),
            models or "# No commands defined",
        ]
        return "\n\n".join(filter(None, sections))

    def _scan_command(self, command: Command, ctx: GenerationContext) -> None:
        for param in command.parameters:
            ctx.scan_param(param)
        for param in command.returns:
            ctx.scan_param(param)

    def _build_imports(self, ctx: GenerationContext) -> str:
        return "\n".join(
            filter(
                None,
                [
                    ctx.typing_import(),
                    "from dataclasses import dataclass",
                    "from enum import StrEnum",
                    "from cdpify.shared.models import CDPModel",
                    "",
                    ctx.local_type_import(),
                ],
            )
        )

    def _render_enum(self, domain: Domain) -> str:
        if not domain.commands:
            return ""

        lines = [f"class {domain.domain}Command(StrEnum):"]
        for cmd in domain.commands:
            lines.append(f'    {to_enum_name(cmd.name)} = "{domain.domain}.{cmd.name}"')
        return "\n".join(lines)

    def _render_models(self, commands: list[Command], ctx: GenerationContext) -> str:
        models: list[str] = []
        for command in commands:
            if command.parameters:
                models.append(self._render_params_model(command, ctx))
            if command.returns:
                models.append(self._render_result_model(command, ctx))
        return "\n\n".join(models)

    def _render_params_model(self, command: Command, ctx: GenerationContext) -> str:
        lines = [
            "@dataclass(kw_only=True, slots=True)",
            f"class {to_pascal_case(command.name)}Params(CDPModel):",
        ]
        if command.description:
            lines.extend(
                format_docstring(command.description, indent=4).rstrip().splitlines()
            )
        for param in command.parameters:
            lines.append(f"    {self._render_field(param, ctx)}")
        return "\n".join(lines)

    def _render_result_model(self, command: Command, ctx: GenerationContext) -> str:
        lines = [
            "@dataclass(kw_only=True, slots=True)",
            f"class {to_pascal_case(command.name)}Result(CDPModel):",
        ]
        for param in command.returns:
            lines.append(f"    {self._render_field(param, ctx)}")
        return "\n".join(lines)

    def _render_field(self, param: Parameter, ctx: GenerationContext) -> str:
        field_name = to_snake_case(param.name)
        py_type = resolve_type(param)
        ctx.track_type_string(py_type)

        if param.optional:
            return f"{field_name}: {py_type} | None = None"
        return f"{field_name}: {py_type}"
