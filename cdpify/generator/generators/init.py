from cdpify.generator.generators.base import BaseGenerator
from cdpify.generator.generators.utils import to_pascal_case
from cdpify.generator.schemas import Domain


class InitGenerator(BaseGenerator):
    filename = "__init__.py"

    def generate(self, domain: Domain) -> str:
        type_names = [t.id for t in domain.types]
        command_names = self._command_names(domain)
        event_names = self._event_names(domain)
        client_name = f"{domain.domain}Client"

        all_names = sorted([*type_names, *command_names, *event_names, client_name])

        sections = [
            self.HEADER,
            f'"""CDP {domain.domain} Domain."""',
            self._import_block("types", type_names),
            self._import_block("commands", command_names),
            self._import_block("events", event_names),
            f"from .client import {client_name}",
            self._exports_block(all_names),
        ]
        return "\n\n".join(filter(None, sections))

    def _command_names(self, domain: Domain) -> list[str]:
        if not domain.commands:
            return []

        names = [f"{domain.domain}Command"]
        for cmd in domain.commands:
            pascal = to_pascal_case(cmd.name)
            if cmd.parameters:
                names.append(f"{pascal}Params")
            if cmd.returns:
                names.append(f"{pascal}Result")
        return sorted(names)

    def _event_names(self, domain: Domain) -> list[str]:
        if not domain.events:
            return []

        names = [f"{domain.domain}Event"]
        names.extend(f"{to_pascal_case(e.name)}Event" for e in domain.events)
        return sorted(names)

    def _import_block(self, module: str, names: list[str]) -> str:
        if not names:
            return ""
        if len(names) <= 3:
            return f"from .{module} import {', '.join(names)}"

        lines = [f"from .{module} import ("]
        lines.extend(f"    {name}," for name in names)
        lines.append(")")
        return "\n".join(lines)

    def _exports_block(self, names: list[str]) -> str:
        lines = ["__all__ = ["]
        lines.extend(f'    "{name}",' for name in names)
        lines.append("]")
        return "\n".join(lines)
