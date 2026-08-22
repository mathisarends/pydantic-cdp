from collections.abc import Callable

import pytest

from cdpify.generator.generators import commands, domain, events, init, types
from cdpify.generator.schemas import Domain


@pytest.mark.parametrize(
    ("filename", "render"),
    [
        ("types.py", types.generate),
        ("commands.py", commands.generate),
        ("events.py", events.generate),
        ("domain.py", domain.generate),
        ("__init__.py", init.generate),
    ],
)
def test_generated_domain_modules_compile(
    filename: str,
    render: Callable[[Domain], str],
    simple_domain: Domain,
) -> None:
    source = render(simple_domain)

    compile(source, filename, "exec")
