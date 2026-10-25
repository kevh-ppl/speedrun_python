# 01 · Estructuras de datos

## 1. Las cuatro básicas

| Tipo       | Mutable | Ordenado | Dups | Lookup   | Uso                   |
|------------|---------|----------|------|----------|-----------------------|
| `list`     | sí      | sí       | sí   | O(n)     | secuencia de items    |
| `tuple`    | no      | sí       | sí   | O(n)     | registro inmutable    |
| `set`      | sí      | no*      | no   | O(1) avg | membership, dedup     |
| `dict`     | sí      | sí (3.7+)| no** | O(1) avg | mapeos                |

\* El orden de iteración no es garantizado; no asumas nada.
\*\* claves únicas; valores pueden repetirse.

```python
xs: list[int] = [1, 2, 3]
pt: tuple[int, int] = (3, 4)         # inmutable
ss: set[str] = {"a", "b"}
d: dict[str, int] = {"a": 1}
```

## 2. Slicing

```python
xs = [10, 20, 30, 40, 50]
xs[1:4]     # [20, 30, 40]
xs[:2]      # [10, 20]
xs[-2:]     # [40, 50]
xs[::-1]    # reverse
xs[::2]     # cada 2: [10, 30, 50]
```

Funciona en `list`, `tuple`, `str`, `bytes`. **No** en `set`/`dict`.

## 3. Comprehensions

```python
squares = [x*x for x in range(10)]
pares   = [x for x in xs if x % 2 == 0]
by_id   = {u.id: u for u in users}            # dict comp
unique  = {x.lower() for x in words}          # set comp
gen     = (x*x for x in range(10**6))         # GENERATOR (lazy, un uso)
```

Regla: si cabe en una línea legible, comprehension. Si necesita condicional
complejo o try/except, loop normal.

## 4. unpacking

```python
a, b, c = [1, 2, 3]
a, *rest = [1, 2, 3, 4]        # a=1, rest=[2,3,4]
first, *mid, last = range(5)   # first=0, mid=[1,2,3], last=4
d = {**base, "extra": 1}       # merge dicts
```

## 5. dict idioms

```python
d.get("k", default)                   # sin KeyError
d.setdefault("k", []).append(x)       # bucket por clave
from collections import defaultdict, Counter
by_tag: dict[str, list[int]] = defaultdict(list)
by_tag["a"].append(1)                 # ya existe la lista
Counter("mississippi")                # Counter({'i':4,'s':4,'p':2,'m':1})
Counter(words).most_common(3)
```

## 6. Generadores

```python
def chunks(xs, n):
    for i in range(0, len(xs), n):
        yield xs[i:i+n]

# Equivalente al "stream": no construye la lista entera en memoria.
total = sum(len(c) for c in chunks(big, 1000))
```

- Un generador se agota tras iterarlo una vez.
- `yield from otro_gen` para delegar.

## 7. Pitfalls comunes

```python
# Default mutable: TRAMPA
def bad(xs=[]): xs.append(1); return xs
bad(); bad()   # [1], [1, 1]  ← el default es compartido

# Fix:
def good(xs: list[int] | None = None) -> list[int]:
    xs = [] if xs is None else xs
    xs.append(1)
    return xs

# Copy shallow vs deep
import copy
b = a.copy()         # shallow: refs internos compartidos
b = copy.deepcopy(a) # deep: todo clonado
```

---

## Ejercicios

1. **01_dedup.py** — `dedup(xs: list[T]) -> list[T]` preservando orden; sin usar `dict.fromkeys` (hazlo con un `set` visto).
2. **02_wordcount.py** — `wordcount(text: str) -> dict[str, int]` normalizado a minúsculas, separando por whitespace y descartando puntuación básica.
3. **03_flatten.py** — `flatten(xs)` recursivo que aplana listas anidadas de cualquier profundidad.
