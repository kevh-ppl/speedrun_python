from __future__ import annotations

from labhelp import load_exercise

mod = load_exercise("01_dedup.py", __file__)


def test_vacio() -> None:
    assert mod.dedup([]) == []


def test_sin_duplicados() -> None:
    assert mod.dedup([1, 2, 3]) == [1, 2, 3]


def test_con_duplicados() -> None:
    assert mod.dedup([1, 2, 1, 3, 2, 4]) == [1, 2, 3, 4]


def test_strings() -> None:
    assert mod.dedup(["a", "a", "b", "a", "c"]) == ["a", "b", "c"]


def test_no_muta_entrada() -> None:
    xs = [1, 1, 2]
    _ = mod.dedup(xs)
    assert xs == [1, 1, 2]


def test_todos_iguales() -> None:
    assert mod.dedup([7, 7, 7, 7]) == [7]
