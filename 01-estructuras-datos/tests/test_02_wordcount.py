from __future__ import annotations

from labhelp import load_exercise

mod = load_exercise("02_wordcount.py", __file__)


def test_vacio() -> None:
    assert mod.wordcount("") == {}


def test_simple() -> None:
    assert mod.wordcount("hola mundo") == {"hola": 1, "mundo": 1}


def test_case_insensitive() -> None:
    assert mod.wordcount("Hola HOLA hola") == {"hola": 3}


def test_puntuacion() -> None:
    r = mod.wordcount("Hola, hola! un, dos; tres: cuatro.")
    assert r == {"hola": 2, "un": 1, "dos": 1, "tres": 1, "cuatro": 1}


def test_multilinea() -> None:
    text = "a b\nc\ta\na"
    assert mod.wordcount(text) == {"a": 3, "b": 1, "c": 1}
