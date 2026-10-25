"""EJERCICIO 02 — Task + TaskList (dataclasses).

Objetivo:
  - `@dataclass` `Task` con campos: `id: int`, `title: str`, `done: bool = False`.
  - Clase `TaskList` con:
      - `add(title: str) -> Task`  → asigna id autoincremental desde 1.
      - `complete(id: int) -> None` → marca done=True; KeyError si no existe.
      - `pending` como @property → lista de tasks no completadas, en orden.
      - `__len__` → total de tasks.

Pistas:
  - from dataclasses import dataclass
  - La lista interna puede ser un list[Task] o un dict[int, Task].
"""
from __future__ import annotations

from dataclasses import dataclass


# TODO: tu codigo aqui


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


class TaskList:
    def __init__(self) -> None:
        raise NotImplementedError
