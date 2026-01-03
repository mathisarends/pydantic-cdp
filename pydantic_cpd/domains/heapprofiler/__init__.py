"""CDP HeapProfiler Domain"""

from .commands import *
from .events import *
from .library import HeapProfilerClient
from .types import *

__all__ = ["HeapProfilerClient"]
