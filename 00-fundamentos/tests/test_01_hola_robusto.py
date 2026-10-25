from __future__ import annotations

import subprocess
import sys

import pytest
from labhelp import pick_path

SCRIPT = pick_path("01_hola_robusto.py", __file__)


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True,
        text=True,
        check=False,
    )


def test_sin_args_saluda_a_mundo() -> None:
    r = run()
    assert r.returncode == 0
    assert r.stdout.strip() == "Hola, mundo!"


def test_name_cambia_el_saludo() -> None:
    r = run("--name", "Kevin")
    assert r.returncode == 0
    assert r.stdout.strip() == "Hola, Kevin!"


def test_help_sale_con_0() -> None:
    r = run("--help")
    assert r.returncode == 0
    assert "usage" in r.stdout.lower() or "uso" in r.stdout.lower()


def test_flag_desconocido_sale_con_2() -> None:
    r = run("--xyz")
    assert r.returncode == 2


@pytest.mark.parametrize("name", ["Ana", "Mundo cruel", "x"])
def test_varios_nombres(name: str) -> None:
    r = run("--name", name)
    assert r.returncode == 0
    assert r.stdout.strip() == f"Hola, {name}!"
