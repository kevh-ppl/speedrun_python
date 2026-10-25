#!/usr/bin/env python3
"""EJERCICIO 01 — Hola robusto.

Objetivo:
  - CLI con argparse.
  - Flag --name NOMBRE (default: "mundo").
  - Imprimir exactamente: "Hola, <nombre>!"
  - --help: exit 0 con texto de ayuda (argparse lo hace solo).
  - flag desconocido: exit 2 (argparse lo hace solo también).

Pistas:
  - Pon la lógica en `main(argv)` para que los tests puedan llamarla.
  - `raise SystemExit(main())` al final.
"""
from __future__ import annotations


# TODO: tu codigo aqui


def main(argv: list[str] | None = None) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main())
