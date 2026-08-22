import pytest

from cdpify.generator.generators import (
    ClientGenerator,
    CommandsGenerator,
    EventsGenerator,
    InitGenerator,
    TypesGenerator,
)
from cdpify.generator.generators.base import BaseGenerator
from cdpify.generator.schemas import Domain


@pytest.mark.parametrize(
    "generator",
    [
        TypesGenerator(),
        CommandsGenerator(),
        EventsGenerator(),
        ClientGenerator(),
        InitGenerator(),
    ],
    ids=lambda generator: generator.filename,
)
def test_generated_domain_modules_compile(
    generator: BaseGenerator, simple_domain: Domain
) -> None:
    source = generator.generate(simple_domain)

    compile(source, generator.filename, "exec")
