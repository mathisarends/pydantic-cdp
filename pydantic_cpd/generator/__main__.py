import asyncio

from pydantic_cpd.generator.downloader import download_specs
from pydantic_cpd.generator.parser import filter_domains
from pydantic_cpd.generator.generator import generate_all_domains


async def main() -> None:
    print("🚀 CDP Pydantic Generator\n")

    specs = await download_specs()
    print(f"✓ CDP Version: {specs.version_string}")
    print(f"✓ Total domains: {len(specs.all_domains)}")

    # Filter domains
    domains = filter_domains(specs)
    print(f"✓ Selected: {len(domains)} domains")

    # Generate code
    generate_all_domains(domains)
    print("\n✅ Generation complete!")


if __name__ == "__main__":
    asyncio.run(main())
