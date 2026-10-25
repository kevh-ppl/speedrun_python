"""flatten recursivo con generador."""
from __future__ import annotations

from collections.abc import Iterator
from typing import Any


def _walk(xs: Any) -> Iterator[Any]:
    if isinstance(xs, (list, tuple)):
        for item in xs:
            yield from _walk(item)
    else:
        yield xs


def flatten(xs: list[Any]) -> list[Any]:
    return list(_walk(xs))
