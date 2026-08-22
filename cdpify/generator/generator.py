import logging
import shutil
import subprocess
from collections.abc import Callable
from pathlib import Path

from cdpify.generator.generators import accessors, client, commands, events, init, types
from cdpify.generator.schemas import Domain

logger = logging.getLogger(__name__)

_CDP_DIR = Path(__file__).parent.parent / "domains"

type DomainRenderer = Callable[[Domain], str]
type ContentPredicate = Callable[[Domain], bool]


def _always(_: Domain) -> bool:
    return True


# Empty types, commands, and events modules are omitted entirely.
_GENERATORS: dict[str, tuple[DomainRenderer, ContentPredicate]] = {
    "types.py": (types.generate, lambda domain: bool(domain.types)),
    "commands.py": (commands.generate, lambda domain: bool(domain.commands)),
    "events.py": (events.generate, lambda domain: bool(domain.events)),
    "client.py": (client.generate, _always),
    "__init__.py": (init.generate, _always),
}

_RUFF_COMMANDS: tuple[list[str], ...] = (
    ["ruff", "format", str(_CDP_DIR)],
    ["ruff", "check", "--fix", str(_CDP_DIR)],
)


def generate_all_domains(domains: list[Domain]) -> None:
    _reset_output_dir()

    logger.info(f"\n📝 Generating {len(domains)} domains...")
    for domain in domains:
        _generate_domain(domain)

    (_CDP_DIR / "accessors.py").write_text(
        accessors.generate(domains), encoding="utf-8"
    )
    (_CDP_DIR / "__init__.py").write_text(init.generate_root(domains), encoding="utf-8")
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

    for filename, (render, has_content) in _GENERATORS.items():
        if not has_content(domain):
            continue
        (domain_dir / filename).write_text(render(domain), encoding="utf-8")


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
