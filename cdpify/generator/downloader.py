import json
import logging
from pathlib import Path
from typing import Any, cast
from urllib.request import urlopen

from cdpify.generator.schemas import CDPSpecs, ProtocolSpec

logger = logging.getLogger(__name__)

_BASE_URL = (
    "https://raw.githubusercontent.com/"
    "ChromeDevTools/devtools-protocol/refs/heads/master/json"
)
_SPECS_DIR = Path(__file__).parent.parent.parent / "specs"


def download_specs() -> CDPSpecs:
    _SPECS_DIR.mkdir(exist_ok=True)

    browser = _fetch("browser_protocol.json")
    js = _fetch("js_protocol.json")

    logger.info("✅ Specs downloaded and saved to specs/")

    return CDPSpecs(
        browser=ProtocolSpec.model_validate(browser),
        js=ProtocolSpec.model_validate(js),
    )


def _fetch(filename: str) -> dict[str, Any]:
    logger.info(f"📥 Downloading {filename}...")

    with urlopen(f"{_BASE_URL}/{filename}", timeout=30) as response:
        data = cast(dict[str, Any], json.load(response))

    (_SPECS_DIR / filename).write_text(json.dumps(data, indent=2), encoding="utf-8")
    return data
