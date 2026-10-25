#!/usr/bin/env python3
"""EJERCICIO 01 — grep mini.

Objetivo:
  Script CLI: `grep_mini.py [-n] [-i] PATTERN [FILE...]`
    - PATTERN es un substring (NO regex).
    - Imprime en stdout cada línea que lo contenga (sin newline doble).
    - -n: prefija "N:" (número de línea, 1-based) por archivo.
    - -i: case-insensitive.
    - Si no se pasan FILE, lee stdin (nombre virtual "-").
    - Si hay varios FILE: prefija "FILE:" antes de cada match.
    - Exit code: 0 si hubo al menos un match, 1 si ninguno,
                 2 si argparse se enoja o archivo no existe.

Pistas:
  - Testeable: `main(argv)` + `raise SystemExit(main())` al final.
  - Para leer stdin: `sys.stdin`.
"""
from __future__ import annotations

import sys


# TODO: tu codigo aqui


def main(argv: list[str] | None = None) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main())
