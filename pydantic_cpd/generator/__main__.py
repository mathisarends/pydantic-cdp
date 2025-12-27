import asyncio
from pydantic_cpd.generator.downloader import download_specs


async def main() -> None:
    print("🚀 Starting CDP Pydantic Generator\n")

    specs = await download_specs()

    print(f"\n📊 Browser Protocol: {specs.version_string}")
    print(f"📊 Total domains: {len(specs.all_domains)}")
    print(f"   - Browser domains: {len(specs.browser.domains)}")
    print(f"   - JS domains: {len(specs.js.domains)}")

    print("\n✅ Generation complete!")


if __name__ == "__main__":
    asyncio.run(main())
