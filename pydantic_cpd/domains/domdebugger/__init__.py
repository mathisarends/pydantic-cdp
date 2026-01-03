"""CDP DOMDebugger Domain"""

from .commands import *
from .events import *
from .library import DOMDebuggerClient
from .types import *

__all__ = ["DOMDebuggerClient"]
