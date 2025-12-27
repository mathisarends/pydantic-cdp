from pydantic_cpd.generator.models import Domain, Command


class LibraryGenerator:
    def generate(self, domain: Domain) -> str:
        sections = [
            self._header(domain),
            self._imports(domain),
            self._client_class(domain),
        ]

        return "\n\n".join(sections)

    def _header(self, domain: Domain) -> str:
        return f'''"""Generated client library from CDP specification"""
# Domain: {domain.domain} Client'''

    def _imports(self, domain: Domain) -> str:
        lines = [
            "from typing import TYPE_CHECKING, Any",
            "",
            "if TYPE_CHECKING:",
            "    from pydantic_cpd.client import CDPClient",
        ]

        if domain.commands:
            param_classes = {
                f"{cmd.name.capitalize()}Params"
                for cmd in domain.commands
                if cmd.parameters
            }
            return_classes = {
                f"{cmd.name.capitalize()}Result"
                for cmd in domain.commands
                if cmd.returns
            }

            all_classes = sorted(param_classes | return_classes)
            if all_classes:
                if len(all_classes) <= 3:
                    lines.append(f"    from .commands import {', '.join(all_classes)}")
                else:
                    lines.append("    from .commands import (")
                    for cls in all_classes:
                        lines.append(f"        {cls},")
                    lines.append("    )")

        return "\n".join(lines)

    def _client_class(self, domain: Domain) -> str:
        class_name = f"{domain.domain}Client"

        lines = [f"class {class_name}:"]

        if domain.description:
            lines.append(f'    """{domain.description}"""')
        else:
            lines.append(f'    """CDP {domain.domain} domain client."""')

        lines.append("")
        lines.append("    def __init__(self, client: 'CDPClient') -> None:")
        lines.append("        self._client = client")

        for command in domain.commands:
            lines.append("")
            lines.append(self._generate_method(command, domain.domain))

        return "\n".join(lines)

    def _generate_method(self, command: Command, domain_name: str) -> str:
        method_name = self._to_snake_case(command.name)
        cdp_method = f"{domain_name}.{command.name}"

        params = self._build_params(command)
        return_type = self._get_return_type(command)

        lines = [
            f"    async def {method_name}(",
            f"        {', '.join(params)}",
            f"    ) -> {return_type}:",
        ]

        if command.description:
            lines.append(f'        """{command.description}"""')

        lines.extend(
            [
                "        result = await self._client.send_raw(",
                f'            method="{cdp_method}",',
                "            params=params.to_cdp_params() if params else None,",
                "            session_id=session_id,",
                "        )",
            ]
        )

        if command.returns:
            lines.append(
                f"        return {command.name.capitalize()}Result.model_validate(result)"
            )
        else:
            lines.append("        return result")

        return "\n".join(lines)

    def _build_params(self, command: Command) -> list[str]:
        params = ["self"]

        if command.parameters:
            all_optional = all(p.optional for p in command.parameters)
            param_class = f"{command.name.capitalize()}Params"

            if all_optional:
                params.append(f"params: '{param_class} | None' = None")
            else:
                params.append(f"params: '{param_class}'")
        else:
            params.append("params: None = None")

        params.append("session_id: str | None = None")
        return params

    def _get_return_type(self, command: Command) -> str:
        if command.returns:
            return f"'{command.name.capitalize()}Result'"
        return "dict[str, Any]"

    def _to_snake_case(self, name: str) -> str:
        chars = []
        for i, char in enumerate(name):
            if char.isupper() and i > 0:
                chars.append("_")
            chars.append(char.lower())
        return "".join(chars)
