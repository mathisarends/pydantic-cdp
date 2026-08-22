from functools import lru_cache

from jinja2 import Environment, PackageLoader, StrictUndefined


@lru_cache(maxsize=1)
def _environment() -> Environment:
    environment = Environment(
        loader=PackageLoader("cdpify.generator", "templates"),
        autoescape=False,
        keep_trailing_newline=True,
        lstrip_blocks=True,
        trim_blocks=True,
        undefined=StrictUndefined,
    )
    environment.filters["prefix_domain_import"] = (
        lambda module: f"from cdpify.domains import {module}"
    )
    return environment


def render_template(template_name: str, **context: object) -> str:
    """Render a generator template with strict variable validation."""
    rendered = _environment().get_template(template_name).render(**context)
    return f"{rendered.rstrip()}\n"
