"""EJERCICIO 01 — @timing decorador.

Objetivo:
  Escribir el decorador `timing` tal que:
    - Preserva __name__ y __doc__ de la función original (usa functools.wraps).
    - Expone `fn.last_ms` con el tiempo (ms) de la última ejecución.
    - Si la función levanta, igualmente se registra el tiempo y la excepción se re-levanta.

Ejemplo:
  @timing
  def square(x): return x*x
  square(5)       # 25
  square.last_ms  # ~0.0x
"""
from __future__ import annotations

from collections.abc import Callable
from typing import Any


# TODO: tu codigo aqui


def timing(fn: Callable[..., Any]) -> Callable[..., Any]:
    raise NotImplementedError
