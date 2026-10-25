from __future__ import annotations

import pytest
from labhelp import load_exercise

mod = load_exercise("02_to_bool.py", __file__)


@pytest.mark.parametrize("s", ["1", "true", "True", " YES ", "y", "on"])
def test_true(s: str) -> None:
    assert mod.to_bool(s) is True


@pytest.mark.parametrize("s", ["0", "false", "FALSE", " no ", "n", "off"])
def test_false(s: str) -> None:
    assert mod.to_bool(s) is False


@pytest.mark.parametrize("s", ["", "   ", "maybe", "2", "truthy", "si"])
def test_invalido_levanta(s: str) -> None:
    with pytest.raises(ValueError):
        mod.to_bool(s)
