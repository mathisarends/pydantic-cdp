import re

from pydantic_cpd.generator.models import Command, Domain
from pydantic_cpd.generator.type_mapper import (
    map_cdp_type,
    to_pascal_case,
    to_snake_case,
)


class LibraryGenerator:
    def __init__(self):
        self.cross_domain_refs: set[str] = set()

    def generate(self, domain: Domain) -> str:
        self.cross_domain_refs.clear()

        sections = [
            self._header(domain),
            self._imports(domain),
            self._client_class(domain),
        ]

        return "\n\n".join(sections)

    def _header(self, domain: Domain) -> str:
        return '"""Generated client library from CDP specification"""'

    def _imports(self, domain: Domain) -> str:
        lines = [
            "from __future__ import annotations",
            "",
            "from typing import TYPE_CHECKING, Any, Literal",
            "",
            "if TYPE_CHECKING:",
            "    from pydantic_cpd.client import CDPClient",
            "",
        ]

        if domain.commands:
            # Nur Params-Klassen importieren (intern verwendet)
            param_classes = {
                f"{to_pascal_case(cmd.name)}Params"
                for cmd in domain.commands
                if cmd.parameters
            }
            return_classes = {
                f"{to_pascal_case(cmd.name)}Result"
                for cmd in domain.commands
                if cmd.returns
            }

            all_classes = sorted(param_classes | return_classes)

            if all_classes:
                lines.append("from .commands import (")
                for cls in all_classes:
                    lines.append(f"    {cls},")
                lines.append(")")
                lines.append("")

            self._pre_scan_for_types(domain)

            type_imports = self._collect_type_imports(domain)
            if type_imports:
                lines.append("from .types import (")
                for type_name in sorted(type_imports):
                    lines.append(f"    {type_name},")
                lines.append(")")
                lines.append("")

            if self.cross_domain_refs:
                lines.append(self._cross_domain_imports())

        return "\n".join(lines)

    def _pre_scan_for_types(self, domain: Domain) -> None:
        for command in domain.commands:
            if not command.parameters:
                continue

            for param in command.parameters:
                param_type = map_cdp_type(param)
                self._track_cross_domain_refs(param_type)

    def _cross_domain_imports(self) -> str:
        unique_domains = set()
        for ref in self.cross_domain_refs:
            domain_name = ref.split(".")[0].lower()
            unique_domains.add(domain_name)

        lines = []
        for domain in sorted(unique_domains):
            lines.append(f"from pydantic_cpd.cdp import {domain}")

        return "\n".join(lines)

    def _collect_type_imports(self, domain: Domain) -> set[str]:
        type_imports = set()

        for command in domain.commands:
            if not command.parameters:
                continue

            for param in command.parameters:
                if param.ref and "." in param.ref:
                    continue

                if param.ref:
                    type_imports.add(param.ref)

                if param.type == "array" and param.items:
                    if "$ref" in param.items:
                        ref = param.items["$ref"]
                        if "." not in ref:
                            type_imports.add(ref)

        return type_imports

    def _track_cross_domain_refs(self, type_str: str) -> None:
        pattern = r"\b([a-z]+)\.([A-Z][a-zA-Z0-9]*)\b"
        matches = re.findall(pattern, type_str)

        for domain, type_name in matches:
            ref = f"{domain}.{type_name}"
            self.cross_domain_refs.add(ref)

    def _client_class(self, domain: Domain) -> str:
        class_name = f"{domain.domain}Client"

        lines = [f"class {class_name}:"]
        lines.append("    def __init__(self, client: CDPClient) -> None:")
        lines.append("        self._client = client")

        for command in domain.commands:
            lines.append("")
            lines.append(self._generate_method(command, domain.domain))

        return "\n".join(lines)

    def _generate_method(self, command: Command, domain_name: str) -> str:
        method_name = to_snake_case(command.name)
        cdp_method = f"{domain_name}.{command.name}"

        params = self._build_params(command)
        return_type = self._get_return_type(command)
        method_body = self._build_method_body(command, cdp_method)

        lines = [f"    async def {method_name}("]

        for param in params:
            lines.append(f"        {param},")

        lines.append(f"    ) -> {return_type}:")
        lines.extend(f"        {line}" for line in method_body)

        return "\n".join(lines)

    def _build_params(self, command: Command) -> list[str]:
        """Build parameter list - nur kwargs, kein params object!"""
        params = ["self"]

        if command.parameters:
            # Alle Parameter sind keyword-only
            params.append("*")

            for param in command.parameters:
                param_name = to_snake_case(param.name)

                # Handle session_id collision
                if param_name == "session_id":
                    param_name = f"{to_snake_case(command.name)}_session_id"

                param_type = map_cdp_type(param)
                self._track_cross_domain_refs(param_type)

                # Behalte die Optionalität wie im CDP-Spec
                # Optional parameters behalten " | None = None"
                # Required parameters bekommen kein Default
                if param.optional:
                    if not param_type.endswith(" | None"):
                        param_type = f"{param_type} | None"
                    params.append(f"{param_name}: {param_type} = None")
                else:
                    # Required - kein Default!
                    if param_type.endswith(" | None"):
                        param_type = param_type[:-7]  # Entferne | None
                    params.append(f"{param_name}: {param_type}")

        params.append("session_id: str | None = None")
        return params

    def _build_method_body(self, command: Command, cdp_method: str) -> list[str]:
        """Generate method body - konstruiere Params intern"""
        lines = []

        if command.parameters:
            param_class = f"{to_pascal_case(command.name)}Params"

            # Map snake_case kwargs zu camelCase Params
            param_mapping = {}
            for p in command.parameters:
                snake_name = to_snake_case(p.name)
                if snake_name == "session_id":
                    kwarg_name = f"{to_snake_case(command.name)}_session_id"
                else:
                    kwarg_name = snake_name

                # Original CDP name (camelCase) für Params-Konstruktor
                param_mapping[p.name] = kwarg_name

            # Konstruiere Params intern
            constructor_args = ", ".join(
                f"{original_name}={kwarg_name}"
                for original_name, kwarg_name in param_mapping.items()
            )
            lines.append(f"params = {param_class}({constructor_args})")
            lines.append("")

            lines.extend(
                [
                    "result = await self._client.send_raw(",
                    f'    method="{cdp_method}",',
                    "    params=params.to_cdp_params(),",
                    "    session_id=session_id,",
                    ")",
                ]
            )
        else:
            lines.extend(
                [
                    "result = await self._client.send_raw(",
                    f'    method="{cdp_method}",',
                    "    params=None,",
                    "    session_id=session_id,",
                    ")",
                ]
            )

        if command.returns:
            result_class = f"{to_pascal_case(command.name)}Result"
            lines.append(f"return {result_class}.model_validate(result)")
        else:
            lines.append("return result")

        return lines

    def _get_return_type(self, command: Command) -> str:
        if command.returns:
            return f"{to_pascal_case(command.name)}Result"
        return "dict[str, Any]"
