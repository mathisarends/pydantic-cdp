import re
from dataclasses import dataclass, field

from cdpify.generator.schemas import Parameter

_CROSS_DOMAIN_PATTERN = re.compile(r"\b([a-z]+)\.([A-Z][a-zA-Z0-9]*)\b")


@dataclass
class GenerationContext:
    """Tracks imports and type references discovered while generating one file.

    A fresh context is created per `generate()` call, so generators stay
    effectively stateless across domains.
    """

    cross_domain_refs: set[str] = field(default_factory=set)
    local_type_refs: set[str] = field(default_factory=set)
    typing_names: set[str] = field(default_factory=set)

    def use_typing(self, name: str) -> None:
        self.typing_names.add(name)

    def track_type_string(self, type_str: str) -> None:
        if "Any" in type_str:
            self.use_typing("Any")
        if "Literal" in type_str:
            self.use_typing("Literal")
        for domain, type_name in _CROSS_DOMAIN_PATTERN.findall(type_str):
            self.cross_domain_refs.add(f"{domain}.{type_name}")

    def scan_param(self, param: Parameter) -> None:
        self._add_ref(param.ref)
        if param.type == "array" and param.items:
            self._add_ref(param.items.get("$ref"))

    def _add_ref(self, ref: str | None) -> None:
        if not ref:
            return
        if "." in ref:
            self.cross_domain_refs.add(ref)
        else:
            self.local_type_refs.add(ref)

    def typing_import(self) -> str:
        if not self.typing_names:
            return ""
        return f"from typing import {', '.join(sorted(self.typing_names))}"

    def local_type_import(self, aliases: dict[str, str] | None = None) -> str:
        if not self.local_type_refs:
            return ""

        aliases = aliases or {}
        lines = ["from .types import ("]
        for name in sorted(self.local_type_refs):
            alias = aliases.get(name)
            lines.append(f"    {name} as {alias}," if alias else f"    {name},")
        lines.append(")")
        return "\n".join(lines)

    def cross_domain_import(self, *, type_checking: bool) -> str:
        if not self.cross_domain_refs:
            return ""

        domains = sorted({ref.split(".")[0].lower() for ref in self.cross_domain_refs})

        if type_checking:
            self.use_typing("TYPE_CHECKING")
            joined = ", ".join(domains)
            return f"if TYPE_CHECKING:\n    from cdpify.domains import {joined}"

        return "\n".join(f"from cdpify.domains import {d}" for d in domains)
