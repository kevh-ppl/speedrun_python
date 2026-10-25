from __future__ import annotations

from labhelp import load_exercise

mod = load_exercise("02_json_merge.py", __file__)


def test_claves_disjuntas() -> None:
    assert mod.merge({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}


def test_escalar_b_gana() -> None:
    assert mod.merge({"a": 1}, {"a": 2}) == {"a": 2}


def test_dict_recursivo() -> None:
    r = mod.merge({"n": {"x": 1}}, {"n": {"y": 2}})
    assert r == {"n": {"x": 1, "y": 2}}


def test_dict_profundo() -> None:
    a = {"n": {"m": {"x": 1}}}
    b = {"n": {"m": {"y": 2}, "z": 3}}
    assert mod.merge(a, b) == {"n": {"m": {"x": 1, "y": 2}, "z": 3}}


def test_lista_se_concatena() -> None:
    assert mod.merge({"xs": [1]}, {"xs": [2, 3]}) == {"xs": [1, 2, 3]}


def test_tipos_distintos_b_gana() -> None:
    assert mod.merge({"n": {"x": 1}}, {"n": 5}) == {"n": 5}


def test_no_muta_entradas() -> None:
    a = {"n": {"x": 1}, "xs": [1]}
    b = {"n": {"y": 2}, "xs": [2]}
    _ = mod.merge(a, b)
    assert a == {"n": {"x": 1}, "xs": [1]}
    assert b == {"n": {"y": 2}, "xs": [2]}
