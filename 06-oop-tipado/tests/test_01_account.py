from __future__ import annotations

import pytest
from labhelp import load_exercise

mod = load_exercise("01_account.py", __file__)


def test_balance_inicial() -> None:
    a = mod.Account("Ana", 10)
    assert a.balance == 10.0
    assert a.owner == "Ana"


def test_deposit() -> None:
    a = mod.Account("Ana")
    a.deposit(5)
    a.deposit(2.5)
    assert a.balance == 7.5


def test_deposit_cero_o_negativo() -> None:
    a = mod.Account("Ana", 10)
    with pytest.raises(ValueError):
        a.deposit(0)
    with pytest.raises(ValueError):
        a.deposit(-1)


def test_withdraw() -> None:
    a = mod.Account("Ana", 10)
    a.withdraw(3)
    assert a.balance == 7


def test_withdraw_insufficient() -> None:
    a = mod.Account("Ana", 5)
    with pytest.raises(mod.InsufficientFunds):
        a.withdraw(10)
    assert a.balance == 5


def test_balance_es_readonly() -> None:
    a = mod.Account("Ana", 5)
    with pytest.raises(AttributeError):
        a.balance = 999  # type: ignore[misc]


def test_repr() -> None:
    a = mod.Account("Ana", 5)
    r = repr(a)
    assert "Ana" in r and "5" in r
