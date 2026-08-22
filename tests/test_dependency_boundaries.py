import ast
import tomllib
from pathlib import Path

_PROJECT_ROOT = Path(__file__).parents[1]
_PACKAGE_ROOT = _PROJECT_ROOT / "cdpify"
_GENERATOR_ONLY_PACKAGES = {"jinja2", "pydantic", "ruff"}


def test_generator_dependencies_are_optional() -> None:
    with (_PROJECT_ROOT / "pyproject.toml").open("rb") as pyproject_file:
        project = tomllib.load(pyproject_file)["project"]

    runtime_dependencies = {
        dependency.split("[", 1)[0].split(">", 1)[0].split("=", 1)[0]
        for dependency in project["dependencies"]
    }
    generator_dependencies = {
        dependency.split("[", 1)[0].split(">", 1)[0].split("=", 1)[0]
        for dependency in project["optional-dependencies"]["generator"]
    }

    assert runtime_dependencies.isdisjoint(_GENERATOR_ONLY_PACKAGES)
    assert _GENERATOR_ONLY_PACKAGES <= generator_dependencies


def test_runtime_does_not_import_generator_code_or_dependencies() -> None:
    violations: list[str] = []

    for source_path in _PACKAGE_ROOT.rglob("*.py"):
        if "generator" in source_path.relative_to(_PACKAGE_ROOT).parts:
            continue

        for imported_name in _imported_names(source_path):
            top_level_name = imported_name.split(".", 1)[0]
            if imported_name.startswith("cdpify.generator") or (
                top_level_name in _GENERATOR_ONLY_PACKAGES
            ):
                relative_path = source_path.relative_to(_PROJECT_ROOT)
                violations.append(f"{relative_path}: {imported_name}")

    assert violations == []


def _imported_names(source_path: Path) -> set[str]:
    tree = ast.parse(source_path.read_text(encoding="utf-8"))
    imported_names: set[str] = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_names.add(node.module)

    return imported_names
