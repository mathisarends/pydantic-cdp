import subprocess
from pathlib import Path


def format_python_tree(directory: Path) -> None:
    """Format and lint-fix a generated Python source tree with Ruff."""
    _run_ruff(directory, "format")
    _run_ruff(directory, "check", "--fix")


def _run_ruff(directory: Path, *arguments: str) -> None:
    command = ["ruff", *arguments, str(directory)]

    try:
        subprocess.run(command, capture_output=True, text=True, check=True)
    except FileNotFoundError as error:
        raise RuntimeError(
            "Ruff is required for generation; install cdpify[generator]"
        ) from error
    except subprocess.CalledProcessError as error:
        details = (error.stderr or error.stdout).strip()
        raise RuntimeError(f"{' '.join(command)} failed:\n{details}") from error
