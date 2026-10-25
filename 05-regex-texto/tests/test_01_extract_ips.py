from __future__ import annotations

from labhelp import load_exercise

mod = load_exercise("01_extract_ips.py", __file__)


def test_vacio() -> None:
    assert mod.extract_ips("") == []


def test_uno() -> None:
    assert mod.extract_ips("ip=10.0.0.1 ok") == ["10.0.0.1"]


def test_descarta_invalidos() -> None:
    r = mod.extract_ips("ok 1.2.3.4 malo 999.1.1.1 nope 256.0.0.0 bien 10.0.0.5")
    assert r == ["1.2.3.4", "10.0.0.5"]


def test_orden_y_dedup() -> None:
    r = mod.extract_ips("10.0.0.1 1.1.1.1 10.0.0.1 2.2.2.2 1.1.1.1")
    assert r == ["10.0.0.1", "1.1.1.1", "2.2.2.2"]


def test_bordes() -> None:
    assert mod.extract_ips("0.0.0.0 y 255.255.255.255") == ["0.0.0.0", "255.255.255.255"]
