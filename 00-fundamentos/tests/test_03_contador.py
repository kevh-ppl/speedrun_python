from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from labhelp import load_exercise, pick_path

mod = load_exercise("03_contador.py", __file__)
SCRIPT = pick_path("03_contador.py", __file__)


def test_count_vacio() -> None:
    assert mod.count([]) == (0, 0, 0)


def test_count_mix(tmp_path: Path) -> None:
    f = tmp_path / "a.txt"
    f.write_text("x")
    d = tmp_path / "d"
    d.mkdir()
    missing = tmp_path / "nope"
    assert mod.count([str(f), str(d), str(missing)]) == (1, 1, 1)


def test_count_dos_files(tmp_path: Path) -> None:
    (tmp_path / "a").write_text("")
    (tmp_path / "b").write_text("")
    assert mod.count([str(tmp_path / "a"), str(tmp_path / "b")]) == (2, 0, 0)


def test_cli_sin_args() -> None:
    r = subprocess.run(
        [sys.executable, str(SCRIPT)], capture_output=True, text=True, check=False
    )
    assert r.returncode == 0
    assert r.stdout.strip() == "files=0 dirs=0 other=0"


def test_cli_con_args(tmp_path: Path) -> None:
    (tmp_path / "a.txt").write_text("")
    r = subprocess.run(
        [sys.executable, str(SCRIPT), str(tmp_path / "a.txt"), str(tmp_path)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert r.returncode == 0
    assert r.stdout.strip() == "files=1 dirs=1 other=0"
