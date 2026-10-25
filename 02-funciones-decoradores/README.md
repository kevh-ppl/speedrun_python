# 02 · Funciones y decoradores

## 1. Firmas

```python
def f(a, b, /, c, d, *, e, f):
    ...
# a, b -> solo posicional   (/)
# c, d -> posicional o keyword
# e, f -> solo keyword      (*)
```

- `/` fija "solo posicional" (añadido en 3.8).
- `*` fija "lo que viene después es solo keyword".
- Útil para `def connect(host, port, /, *, timeout=10):` — forzás keyword en lo opcional.

## 2. *args / **kwargs

```python
def log(level, *args, **kwargs):
    msg = " ".join(str(a) for a in args)
    for k, v in kwargs.items():
        msg += f" {k}={v}"
    print(f"[{level}] {msg}")

log("info", "user", "logged in", id=42)
```

- `*args` → tupla de posicionales extra.
- `**kwargs` → dict de keyword extra.
- Forwarding: `f(*args, **kwargs)` pasa todo a otra función.

## 3. Closures

```python
def multiplier(k):
    def inner(x):
        return x * k    # k capturada del enclosing
    return inner

doble = multiplier(2)
doble(5)  # 10
```

Gotcha clásico (late binding):
```python
fns = [lambda x: x + i for i in range(3)]
[f(10) for f in fns]  # [12, 12, 12]  ← todas ven i=2 al final

# Fix: capturar como default
fns = [lambda x, i=i: x + i for i in range(3)]
[f(10) for f in fns]  # [10, 11, 12]
```

## 4. Decoradores

```python
import functools, time

def timing(fn):
    @functools.wraps(fn)       # preserva __name__/__doc__
    def wrapped(*args, **kwargs):
        t = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            dt = time.perf_counter() - t
            print(f"{fn.__name__} took {dt*1000:.2f}ms")
    return wrapped

@timing
def heavy(): ...
```

Decorador con parámetros (dos niveles):
```python
def retry(attempts: int):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapped(*args, **kwargs):
            for i in range(attempts):
                try:
                    return fn(*args, **kwargs)
                except Exception:
                    if i == attempts - 1:
                        raise
        return wrapped
    return decorator

@retry(attempts=3)
def flaky(): ...
```

## 5. functools útil

```python
from functools import cache, lru_cache, partial, reduce

@cache                      # memoiza sin límite (3.9+)
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

f10 = partial(round, ndigits=10)   # fija kwargs
sum_   = reduce(lambda a,b: a+b, nums, 0)
```

## 6. Protocolo callable

```python
class Multiplier:
    def __init__(self, k): self.k = k
    def __call__(self, x): return x * self.k

doble = Multiplier(2)
doble(5)  # 10 — es "callable" como una función
```

---

## Ejercicios

1. **01_decorador_timing.py** — Decorador `@timing` que mide y almacena el último tiempo en `fn.last_ms`. Usar `functools.wraps`.
2. **02_memoize.py** — `memoize(fn)` manual (sin usar `functools.cache`). Cachea por `(args, frozenset(kwargs.items()))`.
