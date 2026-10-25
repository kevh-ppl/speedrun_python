"""dedup preservando orden con set+list."""
from __future__ import annotations

from typing import TypeVar

T = TypeVar("T")


def dedup(xs: list[T]) -> list[T]:
    seen: set[T] = set()
    out: list[T] = []
    for x in xs:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out
