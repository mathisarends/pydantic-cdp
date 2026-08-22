from pathlib import Path

import pytest

from cdpify.generator import __main__ as cli
from cdpify.generator.schemas import CDPSpecs, Domain


def test_selects_all_domains_when_none_are_requested(
    sample_protocol_spec,
) -> None:
    specs = CDPSpecs(browser=sample_protocol_spec, js=sample_protocol_spec)

    assert cli._select_domains(specs, None) == specs.all_domains


def test_selects_requested_domains_in_order(sample_protocol_spec) -> None:
    specs = CDPSpecs(browser=sample_protocol_spec, js=sample_protocol_spec)

    selected = cli._select_domains(specs, ["Sample", "Sample"])

    assert [domain.domain for domain in selected] == ["Sample"]


def test_rejects_unknown_domains(sample_protocol_spec) -> None:
    specs = CDPSpecs(browser=sample_protocol_spec, js=sample_protocol_spec)

    with pytest.raises(ValueError, match="Unknown CDP domain.*Missing"):
        cli._select_domains(specs, ["Missing"])


def test_main_passes_explicit_paths_and_selection(
    monkeypatch: pytest.MonkeyPatch,
    sample_protocol_spec,
    tmp_path: Path,
) -> None:
    specs = CDPSpecs(browser=sample_protocol_spec, js=sample_protocol_spec)
    spec_dir = tmp_path / "specs"
    output_dir = tmp_path / "domains"
    downloaded: list[Path] = []
    generated: list[tuple[list[Domain], Path]] = []

    def download(destination: Path) -> CDPSpecs:
        downloaded.append(destination)
        return specs

    monkeypatch.setattr(cli, "download_specs", download)
    monkeypatch.setattr(
        cli,
        "generate_domains",
        lambda domains, destination: generated.append((domains, destination)),
    )

    cli.main(
        [
            "--domain",
            "Sample",
            "--spec-dir",
            str(spec_dir),
            "--output-dir",
            str(output_dir),
        ]
    )

    assert downloaded == [spec_dir]
    assert generated == [([sample_protocol_spec.domains[0]], output_dir)]
