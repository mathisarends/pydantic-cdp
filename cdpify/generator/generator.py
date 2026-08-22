import shutil
from pathlib import Path

from cdpify.generator.formatting import format_python_tree
from cdpify.generator.generators import accessors, client, commands, events, init, types
from cdpify.generator.schemas import Domain

_CDP_DIR = Path(__file__).parent.parent / "domains"


def generate_all_domains(domains: list[Domain]) -> None:
    generated_files = _render_files(domains)
    _replace_output(generated_files)
    format_python_tree(_CDP_DIR)


def _render_files(domains: list[Domain]) -> dict[Path, str]:
    files = {
        Path("accessors.py"): accessors.generate(domains),
        Path("__init__.py"): init.generate_root(domains),
    }

    for domain in domains:
        files.update(_render_domain(domain))

    return files


def _render_domain(domain: Domain) -> dict[Path, str]:
    directory = Path(domain.domain.lower())
    files = {
        directory / "client.py": client.generate(domain),
        directory / "__init__.py": init.generate(domain),
    }

    if domain.types:
        files[directory / "types.py"] = types.generate(domain)
    if domain.commands:
        files[directory / "commands.py"] = commands.generate(domain)
    if domain.events:
        files[directory / "events.py"] = events.generate(domain)

    return files


def _replace_output(files: dict[Path, str]) -> None:
    shutil.rmtree(_CDP_DIR, ignore_errors=True)

    for relative_path, source in files.items():
        output_path = _CDP_DIR / relative_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(source, encoding="utf-8")
