"""EJERCICIO 03 — flatten recursivo.

Objetivo:
  `flatten(xs)` aplana listas anidadas de cualquier profundidad.
  Un string NO se trata como iterable (si no, "ab" se partiría en 'a','b').

Ejemplos:
  flatten([1, [2, [3, [4]]], 5])        -> [1, 2, 3, 4, 5]
  flatten([])                            -> []
  flatten(["ab", ["cd", ["ef"]]])        -> ["ab", "cd", "ef"]
  flatten([1, (2, 3), [4, [5]]])         -> [1, 2, 3, 4, 5]  # tuplas también

Pistas:
  - `isinstance(x, (list, tuple))`.
  - Puedes usar un generador interno + list(gen).
"""
from __future__ import annotations

from typing import Any


# TODO: tu codigo aqui


def flatten(xs: list[Any]) -> list[Any]:
    raise NotImplementedError
