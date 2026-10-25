# 06 · OOP + tipado

## 1. Clases básicas

```python
class Account:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self._balance = balance   # convencion: _foo = "privado"

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    @property
    def balance(self) -> float:
        return self._balance

    def __repr__(self) -> str:
        return f"Account(owner={self.owner!r}, balance={self._balance!r})"
```

- `__init__` NO devuelve nada (`-> None`).
- `_name` es convención ("no toques"); `__name` dispara name mangling (raro, evitalo).
- `@property` convierte método en atributo de lectura.
- Definí `__repr__` para debug legible; `__str__` opcional.

## 2. Dunder methods útiles

```python
__eq__(self, other)        # ==
__hash__(self)             # para usar en sets/dicts (default: id)
__lt__ / __le__ / ...      # ordenamiento (con @functools.total_ordering ahorrás)
__len__(self) -> int       # len(x)
__iter__(self) / __next__  # for x in obj
__enter__ / __exit__       # with obj: ...
__add__(self, other)       # x + y
```

## 3. dataclasses

```python
from dataclasses import dataclass, field

@dataclass(frozen=True, slots=True)
class Point:
    x: float
    y: float
    tags: list[str] = field(default_factory=list)   # NO: tags: list[str] = []  (TRAMPA)

p = Point(1.0, 2.0)
p.x; p == Point(1.0, 2.0)      # __eq__ gratis
# p.x = 9  # FrozenInstanceError (porque frozen=True)
```

- `frozen=True` → inmutable + hasheable.
- `slots=True` → menos memoria, pero no se puede agregar atributos ad-hoc.
- `field(default_factory=list)` para defaults mutables (evita la trampa del default compartido).

## 4. Excepciones custom

```python
class LabError(Exception):
    """base del dominio."""

class ValidationError(LabError):
    def __init__(self, field: str, reason: str) -> None:
        super().__init__(f"{field}: {reason}")
        self.field = field
        self.reason = reason

try:
    ...
except ValidationError as e:
    log.error("campo invalido %s: %s", e.field, e.reason)
except LabError:
    log.error("falló algo del dominio")
```

- Heredá siempre de `Exception` (nunca de `BaseException`).
- Hacé una base por dominio: facilita el `except LabError` catch-all.
- `raise X from y` para encadenar causas.

## 5. Typing moderno

```python
from __future__ import annotations
from collections.abc import Iterable, Callable
from typing import Any, Protocol, TypeVar, Literal, TypedDict

T = TypeVar("T")

def head(xs: Iterable[T]) -> T | None:
    for x in xs:
        return x
    return None

Mode = Literal["r", "w", "a"]

class Config(TypedDict):
    host: str
    port: int

class HasName(Protocol):
    name: str

def greet(x: HasName) -> str:                 # structural typing (duck typing con types)
    return f"hola {x.name}"
```

- `|` en vez de `Union` (3.10+).
- `list[int]` en vez de `List[int]` (3.9+, con `__future__ annotations` en 3.8+).
- `Protocol` = interfaz implícita (no hace falta heredar).
- `Any` cuando lo necesitás, pero cada `Any` es un bug esperando.

## 6. mypy en modo paranoia

```bash
mypy --strict solucion/
```

- Fuerza anotar todo, prohibe `Any` implícito, exige `Optional` explícito.
- Si una lib externa no tiene stubs: `# type: ignore[import]` en el `import`.

---

## Ejercicios

1. **01_account.py** — `Account(owner, balance)` con `deposit`, `withdraw`, property `balance`, excepción `InsufficientFunds`.
2. **02_task_list.py** — `@dataclass` `Task(id, title, done)` + `TaskList` que soporta `add`, `complete(id)` y property `pending`.
