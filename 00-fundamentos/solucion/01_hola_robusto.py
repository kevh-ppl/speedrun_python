#!/usr/bin/env python3
"""Hola robusto: imprime "Hola, <nombre>!"."""
from __future__ import annotations

import argparse


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="saluda a alguien")
    p.add_argument("--name", default="mundo", help="nombre a saludar")
    args = p.parse_args(argv)
    print(f"Hola, {args.name}!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
