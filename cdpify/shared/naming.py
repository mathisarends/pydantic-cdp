import re
from functools import lru_cache

_ACRONYMS: frozenset[str] = frozenset(
    {
        "api",
        "ax",
        "cpu",
        "css",
        "dom",
        "gpu",
        "html",
        "http",
        "https",
        "io",
        "js",
        "json",
        "os",
        "pdf",
        "spc",
        "ssl",
        "ui",
        "uri",
        "url",
        "usb",
        "uuid",
        "wasm",
        "xhr",
        "xml",
    }
)

_CAMEL_PATTERN_1 = re.compile(r"(.)([A-Z][a-z]+)")
_CAMEL_PATTERN_2 = re.compile(r"([a-z0-9])([A-Z])")


@lru_cache(maxsize=512)
def to_cdp_case(name: str) -> str:
    parts = name.split("_")
    if not parts:
        return name

    result = [parts[0].lower()]
    for part in parts[1:]:
        lower = part.lower()
        result.append(part.upper() if lower in _ACRONYMS else part.capitalize())
    return "".join(result)


@lru_cache(maxsize=512)
def to_snake_case(name: str) -> str:
    """Convert camelCase/PascalCase to snake_case, keeping acronyms intact."""
    partly_split = _CAMEL_PATTERN_1.sub(r"\1_\2", name)
    return _CAMEL_PATTERN_2.sub(r"\1_\2", partly_split).lower()
