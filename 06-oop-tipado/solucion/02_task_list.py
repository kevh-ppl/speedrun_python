"""Task + TaskList."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


class TaskList:
    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def add(self, title: str) -> Task:
        t = Task(id=self._next_id, title=title)
        self._tasks[t.id] = t
        self._next_id += 1
        return t

    def complete(self, id: int) -> None:
        self._tasks[id].done = True  # KeyError si no existe

    @property
    def pending(self) -> list[Task]:
        return [t for t in self._tasks.values() if not t.done]

    def __len__(self) -> int:
        return len(self._tasks)
