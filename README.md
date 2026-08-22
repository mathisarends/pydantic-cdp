<div align="center">

# cdpify

**An async, typed Python client for the Chrome DevTools Protocol.**

[![PyPI](https://img.shields.io/pypi/v/cdpify?style=flat-square)](https://pypi.org/project/cdpify/)
[![Python](https://img.shields.io/pypi/pyversions/cdpify?style=flat-square)](https://pypi.org/project/cdpify/)
[![CI](https://img.shields.io/github/actions/workflow/status/mathisarends/pydantic-cdp/ci.yml?branch=main&style=flat-square&label=CI)](https://github.com/mathisarends/pydantic-cdp/actions/workflows/ci.yml)

</div>

`cdpify` turns the Chrome DevTools Protocol (CDP) into a Pythonic, IDE-friendly
API. Commands, results, events, and protocol types are generated from the
official CDP specifications, so you get autocomplete and typed responses
without working with raw JSON messages.

## Why cdpify?

- **Typed by default** — generated models for commands, results, events, and
  shared protocol types
- **Ergonomic domain access** — use `client.page`, `client.network`,
  `client.runtime`, and 39 more CDP domains directly
- **Async throughout** — built on `asyncio` and `websockets`
- **Typed event streams** — consume CDP events with async iterators
- **Multi-target support** — route commands through an active CDP session
- **Raw protocol access** — call any CDP method through `send_raw()` when needed

## Installation

```bash
pip install cdpify
```

Requires Python 3.12 or newer.

## Quick start

Start Chrome or Chromium with remote debugging enabled, then obtain a page's
`webSocketDebuggerUrl` from `http://localhost:9222/json`.

```python
import asyncio

import httpx

from cdpify import CDPClient


async def get_websocket_url() -> str:
    async with httpx.AsyncClient() as http:
        response = await http.get("http://localhost:9222/json")
        response.raise_for_status()
        return response.json()[0]["webSocketDebuggerUrl"]


async def main() -> None:
    ws_url = await get_websocket_url()

    async with CDPClient(ws_url) as client:
        await client.page.navigate(url="https://example.com")

        result = await client.runtime.evaluate(
            expression="document.title",
            return_by_value=True,
        )
        print(result.result.value)


asyncio.run(main())
```

Domain clients are available as lazy properties on `CDPClient`. Parameters use
Python's `snake_case`; `cdpify` handles conversion to and from CDP's wire format.

## Listening for events

Events are exposed as typed async streams:

```python
from cdpify.domains.network.events import NetworkEvent, RequestWillBeSentEvent


await client.network.enable()

async for event in client.listen(
    event_name=NetworkEvent.REQUEST_WILL_BE_SENT,
    event_type=RequestWillBeSentEvent,
):
    print(event.request.method, event.request.url)
```

`client.listen()` also accepts an optional `timeout` in seconds. Every event
includes `cdp_session_id`, which is useful when working with multiple targets.

## Working with target sessions

`ActiveSessionCDPClient` keeps the same domain-based API while routing commands
to the selected target session:

```python
from cdpify import ActiveSessionCDPClient, CDPClient


async with CDPClient(browser_ws_url) as root_client:
    session = ActiveSessionCDPClient(root_client)
    session.switch_to("session-id")

    await session.page.enable()
    await session.runtime.evaluate(expression="console.log('Hello from CDP')")
```

The `Browser` and `Target` domains remain bound to the root connection. You can
also pass `session_id` explicitly to generated commands or to `send_raw()`.

## Configuration

```python
client = CDPClient(
    url="ws://localhost:9222/devtools/browser/...",
    additional_headers={"Authorization": "Bearer token"},
    max_frame_size=100 * 1024 * 1024,
    default_timeout=30.0,
)
```

For methods not covered by the generated API, use the low-level escape hatch:

```python
result = await client.send_raw(
    "Runtime.evaluate",
    {"expression": "1 + 1", "returnByValue": True},
)
```

## Development

Install the project and its development dependencies with
[uv](https://docs.astral.sh/uv/):

```bash
uv sync --dev
uv run pytest
uv run ruff check . --exclude cdpify/domains
```

To download the latest protocol definitions and regenerate all domain clients:

```bash
uv run python -m cdpify.generator
```

The generated output lives in `cdpify/domains/` and should not be edited by
hand. The repository also refreshes the upstream specification automatically
once a week and opens a pull request when generated code changes.

## Resources

- [Chrome DevTools Protocol documentation](https://chromedevtools.github.io/devtools-protocol/)
- [Chrome DevTools Protocol repository](https://github.com/ChromeDevTools/devtools-protocol)
- [Examples](examples)

The code-generation approach was inspired by
[`cdp-use`](https://github.com/browser-use/cdp-use).
