from __future__ import annotations

from labhelp import load_exercise

mod = load_exercise("02_run_ok.py", __file__)


def test_echo_ok() -> None:
    rc, out, err = mod.run_ok(["echo", "hola"])
    assert rc == 0
    assert out.strip() == "hola"
    assert err == ""


def test_falso_rc_1() -> None:
    rc, _out, _err = mod.run_ok(["false"])
    assert rc == 1


def test_stderr_capturado() -> None:
    rc, _out, err = mod.run_ok(["sh", "-c", "echo oops >&2; exit 3"])
    assert rc == 3
    assert "oops" in err


def test_timeout() -> None:
    rc, out, err = mod.run_ok(["sleep", "2"], timeout=1)
    assert rc == 124
    assert out == ""
    assert "timeout" in err.lower()
