from __future__ import annotations

from pathlib import Path

import pytest
from labhelp import load_exercise

mod = load_exercise("01_csv_stats.py", __file__)


def test_basico(tmp_path: Path) -> None:
    p = tmp_path / "x.csv"
    p.write_text("name,amount\nAna,10\nLuis,30\nMarta,20\n", encoding="utf-8")
    total, avg, name = mod.csv_stats(p)
    assert total == 60.0
    assert avg == 20.0
    assert name == "Luis"


def test_floats(tmp_path: Path) -> None:
    p = tmp_path / "x.csv"
    p.write_text("name,amount\nAna,0.5\nLuis,1.5\n", encoding="utf-8")
    total, avg, name = mod.csv_stats(p)
    assert total == 2.0
    assert avg == 1.0
    assert name == "Luis"


def test_vacio(tmp_path: Path) -> None:
    p = tmp_path / "x.csv"
    p.write_text("name,amount\n", encoding="utf-8")
    total, avg, name = mod.csv_stats(p)
    assert total == 0.0
    assert avg == 0.0
    assert name == ""


def test_columnas_mal(tmp_path: Path) -> None:
    p = tmp_path / "x.csv"
    p.write_text("foo,bar\n1,2\n", encoding="utf-8")
    with pytest.raises(ValueError):
        mod.csv_stats(p)
