"""EJERCICIO 02 — memoize manual.

Objetivo:
  Decorador `memoize(fn)` que cachea resultados sin usar functools.cache.

Reglas:
  - Clave de cache: (args, frozenset(kwargs.items())).
  - Expone `fn.cache` (dict) y `fn.hits`, `fn.misses` (int).
  - Si los args no son hashables, dejá que levante TypeError natural.

Ejemplo:
  @memoize
  def slow(n): time.sleep(0.1); return n*n
  slow(3), slow(3)      # segunda es inmediata
  slow.hits             # 1
  slow.misses           # 1
"""
from __future__ import annotations

from collections.abc import Callable
from typing import Any


# TODO: tu codigo aqui


def memoize(fn: Callable[..., Any]) -> Callable[..., Any]:
    raise NotImplementedError
