#!/usr/bin/env python3
"""RETO 00 — safe_rm.

Wrapper de borrado que mueve a papelera por defecto. Lee la ficha en
`retos/README.md`.

API testeable:
  safe_rm(
      paths: list[str],
      *,
      dry_run: bool,
      force: bool,
      trash_root: pathlib.Path,
      home_root: pathlib.Path,
  ) -> int

Devuelve exit code: 0 ok, 1 si algún path falló (y procesa el resto),
2 si se rechazó un path peligroso.

Y después un main() que parsea argparse y llama a safe_rm con los defaults
reales (home=Path.home(), trash=~/.trash).
"""
from __future__ import annotations

import sys
from pathlib import Path


# TODO: tu codigo aqui


def safe_rm(
    paths: list[str],
    *,
    dry_run: bool,
    force: bool,
    trash_root: Path,
    home_root: Path,
) -> int:
    raise NotImplementedError


def main(argv: list[str] | None = None) -> int:
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main())
