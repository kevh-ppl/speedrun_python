"""memoize manual con hits/misses."""
from __future__ import annotations

import functools
from collections.abc import Callable
from typing import Any


def memoize(fn: Callable[..., Any]) -> Callable[..., Any]:
    cache: dict[tuple[Any, ...], Any] = {}

    @functools.wraps(fn)
    def wrapped(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            wrapped.hits += 1  # type: ignore[attr-defined]
            return cache[key]
        wrapped.misses += 1  # type: ignore[attr-defined]
        value = fn(*args, **kwargs)
        cache[key] = value
        return value

    wrapped.cache = cache  # type: ignore[attr-defined]
    wrapped.hits = 0  # type: ignore[attr-defined]
    wrapped.misses = 0  # type: ignore[attr-defined]
    return wrapped
