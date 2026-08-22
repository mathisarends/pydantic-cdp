from enum import StrEnum


class _CDPDomain(StrEnum):
    PAGE = "Page"
    DOM = "DOM"
    INPUT = "Input"
    NETWORK = "Network"
    TARGET = "Target"
    RUNTIME = "Runtime"
    CONSOLE = "Console"

    DEBUGGER = "Debugger"
    PROFILER = "Profiler"
    HEAP_PROFILER = "HeapProfiler"
    PERFORMANCE = "Performance"

    CSS = "CSS"
    OVERLAY = "Overlay"
    ANIMATION = "Animation"
    LAYER_TREE = "LayerTree"

    STORAGE = "Storage"
    DATABASE = "Database"
    INDEXED_DB = "IndexedDB"
    CACHE_STORAGE = "CacheStorage"
    DOM_STORAGE = "DOMStorage"
    APPLICATION_CACHE = "ApplicationCache"

    FETCH = "Fetch"
    WEB_AUDIO = "WebAudio"
    WEB_AUTHN = "WebAuthn"
    MEDIA = "Media"
    SERVICE_WORKER = "ServiceWorker"
    BACKGROUND_SERVICE = "BackgroundService"

    EMULATION = "Emulation"
    DEVICE_ORIENTATION = "DeviceOrientation"

    BROWSER = "Browser"
    SYSTEM_INFO = "SystemInfo"
    SECURITY = "Security"
    LOG = "Log"
    TETHERING = "Tethering"

    ACCESSIBILITY = "Accessibility"
    AUDITS = "Audits"

    TRACING = "Tracing"
    SCHEMA = "Schema"
    CAST = "Cast"
    DOM_SNAPSHOT = "DOMSnapshot"
    DOM_DEBUGGER = "DOMDebugger"
    EVENT_BREAKPOINTS = "EventBreakpoints"
    IO = "IO"
    MEMORY = "Memory"


DOMAINS_TO_GENERATE: tuple[_CDPDomain, ...] = (
    _CDPDomain.PAGE,
    _CDPDomain.DOM,
    _CDPDomain.INPUT,
    _CDPDomain.NETWORK,
    _CDPDomain.TARGET,
    _CDPDomain.RUNTIME,
    _CDPDomain.CONSOLE,
    _CDPDomain.DEBUGGER,
    _CDPDomain.PROFILER,
    _CDPDomain.HEAP_PROFILER,
    _CDPDomain.PERFORMANCE,
    _CDPDomain.CSS,
    _CDPDomain.OVERLAY,
    _CDPDomain.ANIMATION,
    _CDPDomain.LAYER_TREE,
    _CDPDomain.STORAGE,
    _CDPDomain.DATABASE,
    _CDPDomain.INDEXED_DB,
    _CDPDomain.CACHE_STORAGE,
    _CDPDomain.DOM_STORAGE,
    _CDPDomain.APPLICATION_CACHE,
    _CDPDomain.FETCH,
    _CDPDomain.WEB_AUDIO,
    _CDPDomain.WEB_AUTHN,
    _CDPDomain.MEDIA,
    _CDPDomain.SERVICE_WORKER,
    _CDPDomain.BACKGROUND_SERVICE,
    _CDPDomain.EMULATION,
    _CDPDomain.DEVICE_ORIENTATION,
    _CDPDomain.BROWSER,
    _CDPDomain.SYSTEM_INFO,
    _CDPDomain.SECURITY,
    _CDPDomain.LOG,
    _CDPDomain.TETHERING,
    _CDPDomain.ACCESSIBILITY,
    _CDPDomain.AUDITS,
    _CDPDomain.TRACING,
    _CDPDomain.SCHEMA,
    _CDPDomain.CAST,
    _CDPDomain.DOM_SNAPSHOT,
    _CDPDomain.DOM_DEBUGGER,
    _CDPDomain.EVENT_BREAKPOINTS,
    _CDPDomain.IO,
    _CDPDomain.MEMORY,
)
