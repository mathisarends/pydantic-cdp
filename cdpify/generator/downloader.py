import json
import logging
from pathlib import Path

import httpx

from cdpify.generator.schemas import CDPSpecs, ProtocolSpec

logger = logging.getLogger(__name__)

_BASE_URL = (
    "https://raw.githubusercontent.com/"
    "ChromeDevTools/devtools-protocol/refs/heads/master/json"
)
_SPECS_DIR = Path(__file__).parent.parent.parent / "specs"


async def download_specs() -> CDPSpecs:
    _SPECS_DIR.mkdir(exist_ok=True)

    async with httpx.AsyncClient() as client:
        browser = await _fetch(client, "browser_protocol.json")
        js = await _fetch(client, "js_protocol.json")

    logger.info("✅ Specs downloaded and saved to specs/")

    return CDPSpecs(
        browser=ProtocolSpec.model_validate(browser),
        js=ProtocolSpec.model_validate(js),
    )


async def _fetch(client: httpx.AsyncClient, filename: str) -> dict:
    logger.info(f"📥 Downloading {filename}...")

    response = await client.get(f"{_BASE_URL}/{filename}")
    response.raise_for_status()
    data = response.json()

    (_SPECS_DIR / filename).write_text(json.dumps(data, indent=2), encoding="utf-8")
    return data
