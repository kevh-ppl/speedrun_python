from __future__ import annotations

from pathlib import Path

from labhelp import load_exercise

mod = load_exercise("00_safe_rm.py", __file__)


def test_mueve_a_papelera(tmp_path: Path) -> None:
    home = tmp_path / "home"
    home.mkdir()
    trash = tmp_path / "trash"
    victim = tmp_path / "doc.txt"
    victim.write_text("x")

    rc = mod.safe_rm(
        [str(victim)], dry_run=False, force=False, trash_root=trash, home_root=home
    )
    assert rc == 0
    assert not victim.exists()
    moved = list(trash.rglob("doc.txt"))
    assert len(moved) == 1


def test_force_borra(tmp_path: Path) -> None:
    home = tmp_path / "home"
    home.mkdir()
    trash = tmp_path / "trash"
    victim = tmp_path / "doc.txt"
    victim.write_text("x")

    rc = mod.safe_rm(
        [str(victim)], dry_run=False, force=True, trash_root=trash, home_root=home
    )
    assert rc == 0
    assert not victim.exists()
    assert not trash.exists()  # con --force no tocamos papelera


def test_dry_run_no_toca(tmp_path: Path) -> None:
    home = tmp_path / "home"
    home.mkdir()
    trash = tmp_path / "trash"
    victim = tmp_path / "doc.txt"
    victim.write_text("x")

    rc = mod.safe_rm(
        [str(victim)], dry_run=True, force=False, trash_root=trash, home_root=home
    )
    assert rc == 0
    assert victim.exists()
    assert not trash.exists()


def test_rechaza_slash(tmp_path: Path) -> None:
    home = tmp_path / "home"
    home.mkdir()
    rc = mod.safe_rm(
        ["/"], dry_run=False, force=True, trash_root=tmp_path / "t", home_root=home
    )
    assert rc == 2


def test_rechaza_home(tmp_path: Path) -> None:
    home = tmp_path / "home"
    home.mkdir()
    rc = mod.safe_rm(
        [str(home)], dry_run=False, force=True, trash_root=tmp_path / "t", home_root=home
    )
    assert rc == 2


def test_path_inexistente_rc_1(tmp_path: Path) -> None:
    home = tmp_path / "home"
    home.mkdir()
    rc = mod.safe_rm(
        [str(tmp_path / "nope")],
        dry_run=False,
        force=False,
        trash_root=tmp_path / "t",
        home_root=home,
    )
    assert rc == 1


def test_dir_recursivo_con_force(tmp_path: Path) -> None:
    home = tmp_path / "home"
    home.mkdir()
    d = tmp_path / "d"
    (d / "sub").mkdir(parents=True)
    (d / "sub" / "x").write_text("y")
    rc = mod.safe_rm(
        [str(d)], dry_run=False, force=True, trash_root=tmp_path / "t", home_root=home
    )
    assert rc == 0
    assert not d.exists()


def test_colision_basename(tmp_path: Path) -> None:
    home = tmp_path / "home"
    home.mkdir()
    trash = tmp_path / "t"
    a = tmp_path / "a" / "doc.txt"
    b = tmp_path / "b" / "doc.txt"
    a.parent.mkdir()
    b.parent.mkdir()
    a.write_text("1")
    b.write_text("2")
    rc = mod.safe_rm(
        [str(a), str(b)], dry_run=False, force=False, trash_root=trash, home_root=home
    )
    assert rc == 0
    moved = sorted(p.name for p in trash.rglob("doc.txt*"))
    assert len(moved) == 2  # ambos sobreviven, el segundo con sufijo
