import logging

from cdpify.generator.config import DOMAINS_TO_GENERATE
from cdpify.generator.downloader import download_specs
from cdpify.generator.generator import generate_all_domains
from cdpify.generator.schemas import CDPSpecs, Domain

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info("🚀 CDP Pydantic Generator\n")

    specs = download_specs()
    logger.info(f"✓ CDP Version: {specs.version_string}")
    logger.info(f"✓ Total domains: {len(specs.all_domains)}")

    domains = _select_domains(specs)
    logger.info(f"✓ Selected: {len(domains)} domains")

    generate_all_domains(domains)


def _select_domains(specs: CDPSpecs) -> list[Domain]:
    selected: list[Domain] = []

    for name in DOMAINS_TO_GENERATE:
        domain = specs.get_domain(name)
        if domain is None:
            logger.warning(f"  ✗ {name}: NOT FOUND")
            continue

        selected.append(domain)
        logger.info(
            f"  ✓ {name}: {len(domain.commands)} commands, {len(domain.events)} events"
        )

    return selected


if __name__ == "__main__":
    main()
