from cdpify.generator.generators.base import BaseGenerator
from cdpify.generator.generators.context import GenerationContext
from cdpify.generator.generators.utils import (
    format_docstring,
    map_cdp_type,
    resolve_type,
    to_enum_name,
    to_pascal_case,
    to_snake_case,
)
from cdpify.generator.schemas import Command, Domain, Parameter

_DEPRECATED_DECORATOR = "    @deprecated()"


class ClientGenerator(BaseGenerator):
    filename = "client.py"

    def generate(self, domain: Domain) -> str:
        ctx = GenerationContext()
        self._scan_commands(domain, ctx)

        sections = [
            self.HEADER,
            self._build_imports(domain, ctx),
            self._render_class(domain, ctx),
        ]
        return "\n\n".join(filter(None, sections))

    def _scan_commands(self, domain: Domain, ctx: GenerationContext) -> None:
        for command in domain.commands:
            if not command.returns:
                ctx.use_typing("Any")
            for param in command.parameters:
                ctx.scan_param(param)
                ctx.track_type_string(map_cdp_type(param))

    def _build_imports(self, domain: Domain, ctx: GenerationContext) -> str:
        cross_domain = ctx.cross_domain_import(type_checking=True)

        sections: list[str] = [
            ctx.typing_import(),
            "from cdpify.shared.command_sender import CDPCommandSender",
        ]

        if self._has_deprecated(domain):
            sections.append("")
            sections.append("from cdpify.shared.decorators import deprecated")

        if domain.commands:
            sections.append("")
            sections.append(self._render_command_imports(domain))

            local_imports = ctx.local_type_import()
            if local_imports:
                sections.append(local_imports)

            if cross_domain:
                sections.append("")
                sections.append(cross_domain)

        return "\n".join(sections)

    def _has_deprecated(self, domain: Domain) -> bool:
        return any(cmd.deprecated for cmd in domain.commands)

    def _render_command_imports(self, domain: Domain) -> str:
        param_classes = {
            f"{to_pascal_case(c.name)}Params" for c in domain.commands if c.parameters
        }
        return_classes = {
            f"{to_pascal_case(c.name)}Result" for c in domain.commands if c.returns
        }
        names = [f"{domain.domain}Command", *sorted(param_classes | return_classes)]

        lines = ["from .commands import ("]
        lines.extend(f"    {name}," for name in names)
        lines.append(")")
        return "\n".join(lines)

    def _render_class(self, domain: Domain, ctx: GenerationContext) -> str:
        lines = [
            f"class {domain.domain}Client:",
            "    def __init__(self, command_sender: CDPCommandSender) -> None:",
            "        self._command_sender = command_sender",
        ]
        for command in domain.commands:
            lines.append("")
            lines.append(self._render_method(command, domain.domain, ctx))
        return "\n".join(lines)

    def _render_method(
        self, command: Command, domain_name: str, ctx: GenerationContext
    ) -> str:
        lines: list[str] = []
        if command.deprecated:
            lines.append(_DEPRECATED_DECORATOR)

        lines.append(f"    async def {to_snake_case(command.name)}(")
        for param in self._render_params(command, ctx):
            lines.append(f"        {param},")
        lines.append(f"    ) -> {self._return_type(command, ctx)}:")

        if command.description:
            lines.extend(
                format_docstring(command.description, indent=8).rstrip().splitlines()
            )

        body = self._render_body(command, domain_name)
        lines.extend(f"        {line}" for line in body)
        return "\n".join(lines)

    def _render_params(self, command: Command, ctx: GenerationContext) -> list[str]:
        params = ["self"]
        if not command.parameters:
            params.append("session_id: str | None = None")
            return params

        params.append("*")
        for param in command.parameters:
            params.append(self._render_param_signature(command, param, ctx))
        params.append("session_id: str | None = None")
        return params

    def _render_param_signature(
        self, command: Command, param: Parameter, ctx: GenerationContext
    ) -> str:
        name = self._param_name(command, param)
        py_type = resolve_type(param)
        ctx.track_type_string(py_type)

        if param.optional:
            return f"{name}: {py_type} | None = None"
        return f"{name}: {py_type}"

    def _param_name(self, command: Command, param: Parameter) -> str:
        name = to_snake_case(param.name)
        if name == "session_id":
            return f"{to_snake_case(command.name)}_session_id"
        return name

    def _return_type(self, command: Command, ctx: GenerationContext) -> str:
        if command.returns:
            return f"{to_pascal_case(command.name)}Result"
        ctx.use_typing("Any")
        return "dict[str, Any]"

    def _render_body(self, command: Command, domain_name: str) -> list[str]:
        lines: list[str] = []
        if command.parameters:
            lines.extend(self._render_params_construction(command))
            lines.append("")
        lines.extend(self._render_send(command, domain_name))
        lines.append(self._render_return(command))
        return lines

    def _render_params_construction(self, command: Command) -> list[str]:
        param_class = f"{to_pascal_case(command.name)}Params"
        constructor_args = ", ".join(
            f"{to_snake_case(p.name)}={self._param_name(command, p)}"
            for p in command.parameters
        )
        return [f"params = {param_class}({constructor_args})"]

    def _render_send(self, command: Command, domain_name: str) -> list[str]:
        method_ref = f"{domain_name}Command.{to_enum_name(command.name)}"
        params_arg = "params.to_cdp_params()" if command.parameters else "None"
        return [
            "result = await self._command_sender.send_raw(",
            f"    method={method_ref},",
            f"    params={params_arg},",
            "    session_id=session_id,",
            ")",
        ]

    def _render_return(self, command: Command) -> str:
        if command.returns:
            return f"return {to_pascal_case(command.name)}Result.from_cdp(result)"
        return "return result"
