from __future__ import annotations

import pytest
from labhelp import load_exercise

mod = load_exercise("02_memoize.py", __file__)


def test_cachea_resultado() -> None:
    calls = 0

    @mod.memoize
    def f(x: int) -> int:
        nonlocal calls
        calls += 1
        return x * 2

    assert f(3) == 6
    assert f(3) == 6
    assert f(3) == 6
    assert calls == 1


def test_hits_y_misses() -> None:
    @mod.memoize
    def f(x: int) -> int:
        return x

    for x in [1, 1, 2, 2, 2]:
        f(x)
    assert f.misses == 2
    assert f.hits == 3


def test_kwargs() -> None:
    @mod.memoize
    def f(a: int, b: int = 10) -> int:
        return a + b

    assert f(1, b=2) == 3
    assert f(1, b=2) == 3
    assert f.hits == 1


def test_unhashable_levanta() -> None:
    @mod.memoize
    def f(x: object) -> object:
        return x

    with pytest.raises(TypeError):
        f([1, 2])


def test_preserva_nombre() -> None:
    @mod.memoize
    def pepe() -> int:
        return 1

    assert pepe.__name__ == "pepe"
