from cdpify.generator.generators.base import BaseGenerator
from cdpify.generator.generators.utils import to_snake_case
from cdpify.generator.schemas import Domain


class DomainAccessorsGenerator(BaseGenerator):
    filename = "accessors.py"

    def generate(self, domains: list[Domain]) -> str:
        sections = [
            self.HEADER,
            "from functools import cached_property",
            "from cdpify.shared.command_sender import CDPCommandSender",
            self._render_client_imports(domains),
            self._render_class(domains),
        ]
        return "\n\n".join(filter(None, sections))

    def _render_client_imports(self, domains: list[Domain]) -> str:
        return "\n".join(
            f"from .{domain.domain.lower()} import {domain.domain}Client"
            for domain in domains
        )

    def _render_class(self, domains: list[Domain]) -> str:
        lines = [
            "class CDPDomains(CDPCommandSender):",
            '    """Generated accessors for the configured CDP domains."""',
        ]
        for domain in domains:
            lines.extend(
                [
                    "",
                    "    @cached_property",
                    f"    def {to_snake_case(domain.domain)}(self) "
                    f"-> {domain.domain}Client:",
                    f"        return {domain.domain}Client(self)",
                ]
            )
        return "\n".join(lines)
