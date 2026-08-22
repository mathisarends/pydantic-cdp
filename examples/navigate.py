import asyncio
import json
from urllib.request import urlopen

from cdpify import CDPClient


def get_ws_url() -> str:
    with urlopen("http://localhost:9222/json", timeout=5) as response:
        pages = json.load(response)
    if not pages:
        raise RuntimeError(
            "No pages found. Is Chrome running with --remote-debugging-port=9222?"
        )
    return pages[0]["webSocketDebuggerUrl"]


async def test_basic():
    print("=== Test 1: Basic Navigation ===")

    ws_url = get_ws_url()
    print(f"Connecting to: {ws_url}")

    async with CDPClient(ws_url) as client:
        result = await client.page.navigate(url="https://example.com")

        print(f"Navigation Result: {result}")


if __name__ == "__main__":
    asyncio.run(test_basic())
