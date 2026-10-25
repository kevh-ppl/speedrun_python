from __future__ import annotations

import pytest
from labhelp import load_exercise

mod = load_exercise("02_task_list.py", __file__)


def test_add_asigna_id_incremental() -> None:
    tl = mod.TaskList()
    a = tl.add("comprar pan")
    b = tl.add("escribir code")
    assert a.id == 1
    assert b.id == 2
    assert a.done is False


def test_len() -> None:
    tl = mod.TaskList()
    assert len(tl) == 0
    tl.add("x")
    tl.add("y")
    assert len(tl) == 2


def test_complete() -> None:
    tl = mod.TaskList()
    a = tl.add("x")
    b = tl.add("y")
    tl.complete(a.id)
    assert [t.title for t in tl.pending] == ["y"]
    tl.complete(b.id)
    assert tl.pending == []


def test_complete_inexistente() -> None:
    tl = mod.TaskList()
    with pytest.raises(KeyError):
        tl.complete(999)


def test_task_es_dataclass() -> None:
    t1 = mod.Task(id=1, title="x")
    t2 = mod.Task(id=1, title="x")
    assert t1 == t2
