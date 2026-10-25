"""EJERCICIO 01 — Account.

Objetivo:
  Clase `Account(owner: str, balance: float = 0.0)` con:
    - `deposit(amount)`: suma; ValueError si amount <= 0.
    - `withdraw(amount)`: resta; ValueError si amount <= 0;
      InsufficientFunds (excepción propia que hereda de Exception) si no alcanza.
    - `balance` como @property (solo lectura).
    - `__repr__` útil: `Account(owner='X', balance=10.0)`.

Pistas:
  - El atributo interno puede llamarse `_balance`.
  - La excepción custom debe estar definida en el mismo módulo.
"""
from __future__ import annotations


# TODO: tu codigo aqui


class InsufficientFunds(Exception):
    ...


class Account:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        raise NotImplementedError
