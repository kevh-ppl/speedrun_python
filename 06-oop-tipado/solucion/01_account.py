"""Account con InsufficientFunds."""
from __future__ import annotations


class InsufficientFunds(Exception):
    """Fondos insuficientes para la operación solicitada."""


class Account:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self._balance = float(balance)

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self._balance:
            raise InsufficientFunds(f"balance={self._balance} < amount={amount}")
        self._balance -= amount

    def __repr__(self) -> str:
        return f"Account(owner={self.owner!r}, balance={self._balance!r})"
