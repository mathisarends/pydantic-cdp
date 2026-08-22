# cdpify

🚀 **An async, typed Python client for the Chrome DevTools Protocol.**

`cdpify` turns the Chrome DevTools Protocol (CDP) into a Pythonic, IDE-friendly
API. Commands, results, events, and protocol types are generated from the
official CDP specifications, so you get autocomplete and typed responses
without working with raw JSON messages.

## Contents

- [Why cdpify?](#why-cdpify)
- [Installation](#installation)
- [Quick start](#quick-start)
- [Supported domains](#supported-domains)
- [Listening for events](#listening-for-events)
- [Working with target sessions](#working-with-target-sessions)
- [Configuration](#configuration)
- [Development](#development)
- [Resources](#resources)

## Why cdpify?

- **Typed by default** — generated models for commands, results, events, and
  shared protocol types
- **Complete domain coverage** — access all 58 generated CDP domains through
  properties such as `client.page`, `client.network`, and `client.runtime`
- **Async throughout** — transport-neutral core with an optional WebSocket
  implementation
- **Typed event streams** — consume CDP events with async iterators
- **Multi-target support** — route commands through an active CDP session
- **Low-level protocol access** — execute any CDP method through `execute()`
  when needed

## Installation

```bash
pip install "cdpify[websocket]"
```

Requires Python 3.12 or newer. The WebSocket extra provides the recommended
default transport used by `Client(url)`. Install `cdpify` without an extra when
supplying your own `Transport` implementation.

Install the generator dependencies only when regenerating protocol modules:

```bash
pip install "cdpify[generator]"
```

## Quick start

Start Chrome or Chromium with remote debugging enabled, then obtain a page's
`webSocketDebuggerUrl` from `http://localhost:9222/json`.

```python
import asyncio
import json
from urllib.request import urlopen

from cdpify import Client


def get_websocket_url() -> str:
    with urlopen("http://localhost:9222/json", timeout=5) as response:
        return json.load(response)[0]["webSocketDebuggerUrl"]


async def main() -> None:
    ws_url = get_websocket_url()

    async with Client(ws_url) as client:
        await client.page.navigate(url="https://example.com")

        result = await client.runtime.evaluate(
            expression="document.title",
            return_by_value=True,
        )
        print(result.result.value)


asyncio.run(main())
```

Domains are available as lazy properties on `Client`. Parameters use
Python's `snake_case`; `cdpify` handles conversion to and from CDP's wire format.

## Supported domains

The generated client currently includes all 58 domains from the bundled CDP
specifications. Each domain is available as a lazy property on `Client` and
`ActiveSessionCDPClient`:

| CDP domain | Python accessor | CDP domain | Python accessor |
| --- | --- | --- | --- |
| `Accessibility` | `client.accessibility` | `IndexedDB` | `client.indexed_db` |
| `Ads` | `client.ads` | `Input` | `client.input` |
| `Animation` | `client.animation` | `Inspector` | `client.inspector` |
| `Audits` | `client.audits` | `IO` | `client.io` |
| `Autofill` | `client.autofill` | `LayerTree` | `client.layer_tree` |
| `BackgroundService` | `client.background_service` | `Log` | `client.log` |
| `BluetoothEmulation` | `client.bluetooth_emulation` | `Media` | `client.media` |
| `Browser` | `client.browser` | `Memory` | `client.memory` |
| `CacheStorage` | `client.cache_storage` | `Network` | `client.network` |
| `Cast` | `client.cast` | `Overlay` | `client.overlay` |
| `Console` | `client.console` | `Page` | `client.page` |
| `CrashReportContext` | `client.crash_report_context` | `Performance` | `client.performance` |
| `CSS` | `client.css` | `PerformanceTimeline` | `client.performance_timeline` |
| `Debugger` | `client.debugger` | `Preload` | `client.preload` |
| `DeviceAccess` | `client.device_access` | `Profiler` | `client.profiler` |
| `DeviceOrientation` | `client.device_orientation` | `PWA` | `client.pwa` |
| `DigitalCredentials` | `client.digital_credentials` | `Runtime` | `client.runtime` |
| `DOM` | `client.dom` | `Schema` | `client.schema` |
| `DOMDebugger` | `client.dom_debugger` | `Security` | `client.security` |
| `DOMSnapshot` | `client.dom_snapshot` | `ServiceWorker` | `client.service_worker` |
| `DOMStorage` | `client.dom_storage` | `SmartCardEmulation` | `client.smart_card_emulation` |
| `Emulation` | `client.emulation` | `Storage` | `client.storage` |
| `EventBreakpoints` | `client.event_breakpoints` | `SystemInfo` | `client.system_info` |
| `Extensions` | `client.extensions` | `Target` | `client.target` |
| `FedCm` | `client.fed_cm` | `Tethering` | `client.tethering` |
| `Fetch` | `client.fetch` | `Tracing` | `client.tracing` |
| `FileSystem` | `client.file_system` | `WebAudio` | `client.web_audio` |
| `HeadlessExperimental` | `client.headless_experimental` | `WebAuthn` | `client.web_authn` |
| `HeapProfiler` | `client.heap_profiler` | `WebMCP` | `client.web_mcp` |

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
from cdpify import ActiveSessionCDPClient, Client


async with Client(browser_ws_url) as root_client:
    session = ActiveSessionCDPClient(root_client)
    session.switch_to("session-id")

    await session.page.enable()
    await session.runtime.evaluate(expression="console.log('Hello from CDP')")
```

The `Browser` and `Target` domains remain bound to the root connection. You can
also pass `session_id` explicitly to generated commands or to `execute()`.

## Configuration

```python
client = Client(
    url="ws://localhost:9222/devtools/browser/...",
    additional_headers={"Authorization": "Bearer token"},
    max_frame_size=100 * 1024 * 1024,
    default_timeout=30.0,
)
```

For another transport protocol, implement the exported `Transport` protocol
and inject it directly:

```python
from cdpify import Client

client = Client(transport=my_transport)
```

For methods not covered by the generated API, use the low-level escape hatch:

```python
result = await client.execute(
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

Generate only selected domains by repeating `--domain`:

```bash
uv run python -m cdpify.generator --domain Page --domain Runtime
```

Use `--spec-dir` and `--output-dir` to override where downloaded specifications
and generated modules are written.

The generated output lives in `cdpify/domains/` and should not be edited by
hand. The repository also refreshes the upstream specification automatically
once a week and opens a pull request when generated code changes.

## Resources

- [Chrome DevTools Protocol documentation](https://chromedevtools.github.io/devtools-protocol/)
- [Chrome DevTools Protocol repository](https://github.com/ChromeDevTools/devtools-protocol)
- [Examples](examples)

The code-generation approach was inspired by
[`cdp-use`](https://github.com/browser-use/cdp-use).
