"""EJERCICIO 01 — dedup preservando orden.

Objetivo:
  Implementar `dedup(xs)` que devuelve una lista con los elementos únicos
  de `xs` en el orden de primera aparición.

Reglas:
  - No usar `dict.fromkeys` (es la forma idiomática, pero este ejercicio
    es sobre el patrón "set visto + list acumuladora").
  - Debe funcionar con cualquier tipo hashable.
  - No debe mutar la entrada.

Ejemplos:
  dedup([1, 2, 1, 3, 2, 4]) -> [1, 2, 3, 4]
  dedup(["a", "a", "b"])    -> ["a", "b"]
  dedup([])                 -> []
"""
from __future__ import annotations

from typing import TypeVar

T = TypeVar("T")


# TODO: tu codigo aqui


def dedup(xs: list[T]) -> list[T]:
    raise NotImplementedError
