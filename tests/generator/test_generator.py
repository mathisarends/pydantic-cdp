from pathlib import Path

import pytest

from cdpify.generator import formatting, generator
from cdpify.generator.schemas import Domain


def test_render_domain_includes_available_modules(simple_domain: Domain) -> None:
    files = generator._render_domain(simple_domain)
    directory = Path("sample")

    assert set(files) == {
        directory / "__init__.py",
        directory / "client.py",
        directory / "commands.py",
        directory / "events.py",
        directory / "types.py",
    }


def test_render_domain_omits_empty_optional_modules(empty_domain: Domain) -> None:
    files = generator._render_domain(empty_domain)
    directory = Path("empty")

    assert set(files) == {
        directory / "__init__.py",
        directory / "client.py",
    }


def test_missing_ruff_has_actionable_error(monkeypatch: pytest.MonkeyPatch) -> None:
    def raise_missing(*args: object, **kwargs: object) -> None:
        raise FileNotFoundError

    monkeypatch.setattr(formatting.subprocess, "run", raise_missing)

    with pytest.raises(RuntimeError, match=r"install cdpify\[generator\]"):
        formatting.format_python_tree(Path("generated"))
