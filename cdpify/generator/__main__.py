import sys

from cdpify.generator.config import DOMAINS_TO_GENERATE
from cdpify.generator.downloader import download_specs
from cdpify.generator.generator import generate_all_domains
from cdpify.generator.schemas import CDPSpecs, Domain


def main() -> None:
    print("Downloading CDP specifications...")
    specs = download_specs()

    domains = _select_domains(specs)
    print(
        f"CDP {specs.version_string}: "
        f"generating {len(domains)} of {len(specs.all_domains)} domains..."
    )

    generate_all_domains(domains)
    print("Generation complete.")


def _select_domains(specs: CDPSpecs) -> list[Domain]:
    selected: list[Domain] = []

    for name in DOMAINS_TO_GENERATE:
        domain = specs.get_domain(name)
        if domain is None:
            print(f"Warning: CDP domain {name} was not found.", file=sys.stderr)
            continue
        selected.append(domain)

    return selected


if __name__ == "__main__":
    main()
