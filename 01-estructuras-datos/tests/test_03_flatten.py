from __future__ import annotations

from labhelp import load_exercise

mod = load_exercise("03_flatten.py", __file__)


def test_vacio() -> None:
    assert mod.flatten([]) == []


def test_plano() -> None:
    assert mod.flatten([1, 2, 3]) == [1, 2, 3]


def test_un_nivel() -> None:
    assert mod.flatten([1, [2, 3], 4]) == [1, 2, 3, 4]


def test_profundo() -> None:
    assert mod.flatten([1, [2, [3, [4, [5]]]]]) == [1, 2, 3, 4, 5]


def test_strings_no_se_rompen() -> None:
    assert mod.flatten(["ab", ["cd", ["ef"]]]) == ["ab", "cd", "ef"]


def test_tuplas() -> None:
    assert mod.flatten([1, (2, 3), [4, (5, [6])]]) == [1, 2, 3, 4, 5, 6]
