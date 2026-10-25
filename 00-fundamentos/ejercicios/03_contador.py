#!/usr/bin/env python3
"""EJERCICIO 03 — Contador de files/dirs.

Objetivo:
  Dados N paths como argumentos de CLI, imprimir en stdout:
      files=X dirs=Y other=Z
  Donde:
    - files  = cantidad de paths que existen y son archivo regular.
    - dirs   = cantidad que existen y son directorio.
    - other  = cantidad que existen pero no son ni archivo ni dir
               (links rotos cuentan como other), MÁS los que no existen.
  Si no se pasa ningún path: imprime "files=0 dirs=0 other=0" y sale con 0.
  Exit code: siempre 0 salvo error interno.

Pistas:
  - pathlib.Path.is_file(), is_dir(), exists().
  - Un symlink roto: exists() es False.
  - Testea con `main(["a", "b"])` para no depender de sys.argv.
"""
from __future__ import annotations

import sys


# TODO: tu codigo aqui


def count(paths: list[str]) -> tuple[int, int, int]:
    raise NotImplementedError


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    files, dirs, other = count(argv)
    print(f"files={files} dirs={dirs} other={other}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
