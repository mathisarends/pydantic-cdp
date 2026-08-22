import logging
import shutil
import subprocess
from collections.abc import Callable
from pathlib import Path

from cdpify.generator.generators import (
    BaseGenerator,
    ClientGenerator,
    CommandsGenerator,
    DomainAccessorsGenerator,
    EventsGenerator,
    InitGenerator,
    TypesGenerator,
)
from cdpify.generator.generators.base import HEADER
from cdpify.generator.generators.utils import to_snake_case
from cdpify.generator.generators.views import DomainView
from cdpify.generator.rendering import render_template
from cdpify.generator.schemas import Domain

logger = logging.getLogger(__name__)

_CDP_DIR = Path(__file__).parent.parent / "domains"

_GENERATORS: tuple[BaseGenerator, ...] = (
    TypesGenerator(),
    CommandsGenerator(),
    EventsGenerator(),
    ClientGenerator(),
    InitGenerator(),
)

# A generator is skipped entirely for a domain that has nothing for it to
# render, instead of emitting a placeholder file like "# No types defined".
_HAS_CONTENT: dict[type[BaseGenerator], Callable[[Domain], bool]] = {
    TypesGenerator: lambda d: bool(d.types),
    CommandsGenerator: lambda d: bool(d.commands),
    EventsGenerator: lambda d: bool(d.events),
}

_DOMAIN_ACCESSORS_GENERATOR = DomainAccessorsGenerator()

_RUFF_COMMANDS: tuple[list[str], ...] = (
    ["ruff", "format", str(_CDP_DIR)],
    ["ruff", "check", "--fix", str(_CDP_DIR)],
)


def generate_all_domains(domains: list[Domain]) -> None:
    _reset_output_dir()

    logger.info(f"\n📝 Generating {len(domains)} domains...")
    for domain in domains:
        _generate_domain(domain)

    (_CDP_DIR / _DOMAIN_ACCESSORS_GENERATOR.filename).write_text(
        _DOMAIN_ACCESSORS_GENERATOR.generate(domains), encoding="utf-8"
    )
    (_CDP_DIR / "__init__.py").write_text(_build_root_init(domains), encoding="utf-8")
    _format_with_ruff()

    logger.info("\n✅ Generation complete!")


def _reset_output_dir() -> None:
    shutil.rmtree(_CDP_DIR, ignore_errors=True)
    _CDP_DIR.mkdir(parents=True, exist_ok=True)


def _generate_domain(domain: Domain) -> None:
    domain_dir = _CDP_DIR / domain.domain.lower()
    domain_dir.mkdir(exist_ok=True)

    logger.info(
        f"  ✓ {domain.domain} "
        f"({len(domain.types)} types, "
        f"{len(domain.commands)} commands, "
        f"{len(domain.events)} events)"
    )

    for generator in _GENERATORS:
        has_content = _HAS_CONTENT.get(type(generator))
        if has_content and not has_content(domain):
            continue
        (domain_dir / generator.filename).write_text(
            generator.generate(domain), encoding="utf-8"
        )


def _build_root_init(domains: list[Domain]) -> str:
    return render_template(
        "root_init.py.jinja2",
        header=HEADER,
        domains=tuple(
            DomainView(
                name=domain.domain,
                module=domain.domain.lower(),
                property_name=to_snake_case(domain.domain),
            )
            for domain in domains
        ),
    )


def _format_with_ruff() -> None:
    logger.info("\n✨ Formatting generated code with Ruff...")

    try:
        for cmd in _RUFF_COMMANDS:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            if result.returncode != 0:
                details = (result.stderr or result.stdout).strip()
                raise RuntimeError(f"{' '.join(cmd)} failed:\n{details}")
        logger.info("  ✓ Code formatted successfully")
    except FileNotFoundError:
        logger.warning("  ⚠️  Ruff not found – install with: uv add ruff")
