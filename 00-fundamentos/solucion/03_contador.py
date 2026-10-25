#!/usr/bin/env python3
"""Contador de files vs dirs vs other."""
from __future__ import annotations

import sys
from pathlib import Path


def count(paths: list[str]) -> tuple[int, int, int]:
    files = dirs = other = 0
    for raw in paths:
        p = Path(raw)
        if p.is_file():
            files += 1
        elif p.is_dir():
            dirs += 1
        else:
            other += 1
    return files, dirs, other


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    files, dirs, other = count(argv)
    print(f"files={files} dirs={dirs} other={other}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
