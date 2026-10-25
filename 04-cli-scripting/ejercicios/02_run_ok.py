"""EJERCICIO 02 — run_ok.

Objetivo:
  `run_ok(cmd, timeout=5)` corre `cmd` (list[str]) con subprocess:
    - Devuelve `(returncode, stdout, stderr)` como `(int, str, str)`.
    - stdout/stderr capturados como texto (utf-8).
    - Si el proceso tarda más que `timeout` segundos: devolver (124, "", "timeout").
    - NO levantar aunque el comando falle.
    - NO usar shell=True.
"""
from __future__ import annotations


# TODO: tu codigo aqui


def run_ok(cmd: list[str], timeout: int = 5) -> tuple[int, str, str]:
    raise NotImplementedError
