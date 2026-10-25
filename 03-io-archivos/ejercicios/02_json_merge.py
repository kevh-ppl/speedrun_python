"""EJERCICIO 02 — JSON merge recursivo.

Objetivo:
  `merge(a, b)` combina dos dicts como si fueran JSON:
    - Si ambas claves tienen dict como valor, se mergean recursivamente.
    - Si ambas tienen list, se concatenan (a + b).
    - En cualquier otro conflicto, b gana.
    - Las claves que están solo en uno, pasan tal cual.

Ejemplos:
  merge({"a": 1}, {"b": 2})                         -> {"a": 1, "b": 2}
  merge({"a": 1}, {"a": 2})                         -> {"a": 2}
  merge({"n": {"x": 1}}, {"n": {"y": 2}})           -> {"n": {"x": 1, "y": 2}}
  merge({"xs": [1]}, {"xs": [2, 3]})                -> {"xs": [1, 2, 3]}
  merge({"n": {"x": 1}}, {"n": 5})                  -> {"n": 5}

No debe mutar `a` ni `b`.
"""
from __future__ import annotations

from typing import Any


# TODO: tu codigo aqui


def merge(a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
    raise NotImplementedError
