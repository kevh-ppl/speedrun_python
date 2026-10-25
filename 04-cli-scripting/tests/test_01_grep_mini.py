from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from labhelp import pick_path

SCRIPT = pick_path("01_grep_mini.py", __file__)


def run(args: list[str], stdin: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        input=stdin,
        capture_output=True,
        text=True,
        check=False,
    )


def test_match_basico(tmp_path: Path) -> None:
    f = tmp_path / "a.txt"
    f.write_text("foo\nbar\nfoobar\n")
    r = run(["foo", str(f)])
    assert r.returncode == 0
    assert r.stdout == "foo\nfoobar\n"


def test_sin_match(tmp_path: Path) -> None:
    f = tmp_path / "a.txt"
    f.write_text("foo\nbar\n")
    r = run(["xyz", str(f)])
    assert r.returncode == 1
    assert r.stdout == ""


def test_flag_n(tmp_path: Path) -> None:
    f = tmp_path / "a.txt"
    f.write_text("foo\nbar\nfoo\n")
    r = run(["-n", "foo", str(f)])
    assert r.returncode == 0
    assert r.stdout == "1:foo\n3:foo\n"


def test_flag_i(tmp_path: Path) -> None:
    f = tmp_path / "a.txt"
    f.write_text("Foo\nbar\n")
    r = run(["-i", "foo", str(f)])
    assert r.returncode == 0
    assert r.stdout == "Foo\n"


def test_stdin() -> None:
    r = run(["ho"], stdin="hola\nchau\nhombre\n")
    assert r.returncode == 0
    assert r.stdout == "hola\nhombre\n"


def test_multi_file_prefija(tmp_path: Path) -> None:
    a = tmp_path / "a.txt"
    b = tmp_path / "b.txt"
    a.write_text("foo\n")
    b.write_text("foo\nbar\n")
    r = run(["foo", str(a), str(b)])
    assert r.returncode == 0
    assert f"{a}:foo\n{b}:foo\n" == r.stdout


def test_archivo_inexistente(tmp_path: Path) -> None:
    r = run(["x", str(tmp_path / "nope.txt")])
    assert r.returncode == 2
