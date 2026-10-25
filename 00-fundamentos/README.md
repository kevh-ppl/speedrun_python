# 00 · Fundamentos de Python para scripting

Refresco denso de lo que un script Python bien escrito debería tener.

## 1. Anatomía de un script robusto

```python
#!/usr/bin/env python3
"""Hace X. Uso: foo.py [--name NOMBRE]"""
from __future__ import annotations

import sys
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    ...
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- `from __future__ import annotations` — permite `list[int]`, `str | None` sin importar `typing`.
- `main() -> int` + `raise SystemExit(main())` — un único punto de salida; los tests pueden importar sin ejecutar.
- Nunca `import *`.
- Si el script tiene efectos secundarios al importar, los tests van a sufrir.

## 2. Tipos y verdades

```python
# Falsy: None, False, 0, 0.0, '', [], {}, set(), tuple()
# Todo lo demás es truthy.
if not users:        # vacío
    ...
if users is None:    # distinto a `if not users`
    ...
```

- `is` compara identidad, `==` igualdad. `None`, `True`, `False` → `is`.
- `==` entre tipos distintos no revienta: `1 == "1"` → `False`.
- Enteros chicos están internados: `256 is 256` → `True`, `257 is 257` → *puede* ser `False`. **Nunca uses `is` con enteros.**

## 3. Casting explícito

```python
int("42")            # 42
int("  42 ")         # 42 (strip-friendly)
int("0x2a", 16)      # 42
float(".5")          # 0.5
bool("False")        # True (!) — cualquier string no vacío es True
```

Para convertir strings a bool de verdad, escribe la tabla:

```python
def to_bool(s: str) -> bool:
    s = s.strip().lower()
    if s in {"1", "true", "yes", "y", "on"}:
        return True
    if s in {"0", "false", "no", "n", "off"}:
        return False
    raise ValueError(f"no boolean: {s!r}")
```

## 4. f-strings y formatting

```python
name, n = "Kevin", 42
f"{name=} {n:>5}"            # name='Kevin'    42
f"{3.14159:.2f}"             # 3.14
f"{255:08b}"                 # 11111111
f"{'x':*^10}"                # ****x*****
```

- `=` dentro de `{}` imprime nombre+valor (debug).
- `!r` → `repr`, `!s` → `str`.

## 5. Argparse mínimo

```python
import argparse

def parse(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="saluda")
    p.add_argument("--name", default="mundo")
    p.add_argument("--count", type=int, default=1)
    p.add_argument("-v", "--verbose", action="store_true")
    return p.parse_args(argv)
```

- argparse sale con exit code **2** ante flags inválidos (igual que bash convention).
- Testeable: pasa `argv` explícito en vez de leer `sys.argv`.

## 6. Pathlib > os.path

```python
from pathlib import Path

p = Path("/etc/hosts")
p.exists(), p.is_file(), p.is_dir()
p.read_text(encoding="utf-8")
p.write_text("hola\n", encoding="utf-8")
for f in Path(".").iterdir(): ...
for f in Path(".").rglob("*.py"): ...
Path("a") / "b" / "c.txt"   # construir paths
```

## 7. Errores

```python
try:
    risky()
except (OSError, ValueError) as e:
    print(f"falló: {e}", file=sys.stderr)
    return 1
except Exception:
    raise           # no silencies lo que no esperas
finally:
    cleanup()
```

- Nunca `except:` o `except Exception: pass` salvo que *de verdad* sepas por qué.
- Agrupa en tuplas: `except (A, B)`, no `except A: ... except B: ...` idénticos.

## 8. stdin / stdout / stderr

```python
import sys

for line in sys.stdin:              # iterar línea por línea
    print(line.rstrip())
print("error", file=sys.stderr)
sys.exit(2)
```

- `print()` escribe a stdout con `\n`. Usa `end=""` para no agregar newline.
- `sys.argv[0]` es el nombre del script.

---

## Ejercicios

Ver `ejercicios/`. Resuelve, luego:

```bash
make test MOD=00-fundamentos
```

1. **01_hola_robusto.py** — CLI con `--name` (default "mundo"), `--help`, exit 2 en flag desconocido. (Pista: deja que `argparse` haga lo del `--help`/error 2 por ti).
2. **02_to_bool.py** — Función `to_bool(s: str) -> bool` según la tabla del README; `ValueError` si no reconoce.
3. **03_contador.py** — Dados N paths como argumentos, imprime `files=X dirs=Y other=Z` según cuántos de cada tipo existan.

## Lecturas de 10 minutos

- `python -m pydoc argparse`
- `python -m pydoc pathlib`
- [PEP 8](https://peps.python.org/pep-0008/) — convenciones
- [PEP 257](https://peps.python.org/pep-0257/) — docstrings
