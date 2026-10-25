#!/usr/bin/env python3
"""grep mini: substring, -n, -i, stdin, multi-file."""
from __future__ import annotations

import argparse
import sys
from collections.abc import Iterator
from pathlib import Path


def _lines(name: str) -> Iterator[str]:
    if name == "-":
        yield from sys.stdin
    else:
        with Path(name).open(encoding="utf-8") as f:
            yield from f


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="grep_mini")
    p.add_argument("-n", action="store_true", help="prefija numero de linea")
    p.add_argument("-i", action="store_true", help="ignore case")
    p.add_argument("pattern")
    p.add_argument("files", nargs="*")
    args = p.parse_args(argv)

    files = args.files or ["-"]
    needle = args.pattern.lower() if args.i else args.pattern
    multi = len(files) > 1
    found = False

    for name in files:
        if name != "-" and not Path(name).is_file():
            print(f"grep_mini: {name}: no such file", file=sys.stderr)
            return 2
        for lineno, raw in enumerate(_lines(name), start=1):
            hay = raw.lower() if args.i else raw
            if needle in hay:
                found = True
                prefix = ""
                if multi:
                    prefix += f"{name}:"
                if args.n:
                    prefix += f"{lineno}:"
                print(f"{prefix}{raw}", end="" if raw.endswith("\n") else "\n")

    return 0 if found else 1


if __name__ == "__main__":
    raise SystemExit(main())
