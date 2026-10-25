#!/usr/bin/env python3
"""safe_rm: wrapper de rm con papelera y lista negra."""
from __future__ import annotations

import argparse
import shutil
import sys
from datetime import datetime
from pathlib import Path


def _is_dangerous(p: Path, home_root: Path) -> bool:
    try:
        resolved = p.resolve()
    except OSError:
        return False
    if resolved == Path("/"):
        return True
    return resolved == home_root.resolve()


def safe_rm(
    paths: list[str],
    *,
    dry_run: bool,
    force: bool,
    trash_root: Path,
    home_root: Path,
) -> int:
    rc = 0
    stamp = datetime.now().isoformat(timespec="seconds")
    bucket = trash_root / stamp

    for raw in paths:
        p = Path(raw)
        if _is_dangerous(p, home_root):
            print(f"safe_rm: rechazado por peligroso: {raw}", file=sys.stderr)
            return 2
        if not p.exists() and not p.is_symlink():
            print(f"safe_rm: no existe: {raw}", file=sys.stderr)
            rc = 1
            continue

        if dry_run:
            action = "RM" if force else "TRASH"
            print(f"[dry-run] {action} {p}")
            continue

        if force:
            if p.is_dir() and not p.is_symlink():
                shutil.rmtree(p)
            else:
                p.unlink()
        else:
            bucket.mkdir(parents=True, exist_ok=True)
            # evitar colisiones de basename
            dst = bucket / p.name
            i = 1
            while dst.exists():
                dst = bucket / f"{p.name}.{i}"
                i += 1
            shutil.move(str(p), str(dst))
    return rc


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="safe_rm")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true", help="omite papelera")
    parser.add_argument("paths", nargs="+")
    args = parser.parse_args(argv)
    home = Path.home()
    return safe_rm(
        args.paths,
        dry_run=args.dry_run,
        force=args.force,
        trash_root=home / ".trash",
        home_root=home,
    )


if __name__ == "__main__":
    raise SystemExit(main())
