"""@timing con last_ms."""
from __future__ import annotations

import functools
import time
from collections.abc import Callable
from typing import Any


def timing(fn: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(fn)
    def wrapped(*args: Any, **kwargs: Any) -> Any:
        t = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            wrapped.last_ms = (time.perf_counter() - t) * 1000  # type: ignore[attr-defined]

    wrapped.last_ms = 0.0  # type: ignore[attr-defined]
    return wrapped
