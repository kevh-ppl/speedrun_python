from __future__ import annotations

import time

import pytest
from labhelp import load_exercise

mod = load_exercise("01_decorador_timing.py", __file__)


def test_preserva_nombre_y_doc() -> None:
    @mod.timing
    def square(x: int) -> int:
        """eleva al cuadrado."""
        return x * x

    assert square.__name__ == "square"
    assert square.__doc__ == "eleva al cuadrado."


def test_devuelve_mismo_valor() -> None:
    @mod.timing
    def add(a: int, b: int) -> int:
        return a + b

    assert add(2, 3) == 5


def test_registra_last_ms() -> None:
    @mod.timing
    def slow() -> int:
        time.sleep(0.02)
        return 1

    slow()
    assert slow.last_ms >= 15.0  # ~20ms, con margen


def test_registra_last_ms_aunque_levante() -> None:
    @mod.timing
    def boom() -> None:
        raise RuntimeError("x")

    with pytest.raises(RuntimeError):
        boom()
    assert boom.last_ms >= 0.0
