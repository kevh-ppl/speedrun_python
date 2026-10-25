# 03 · I/O y archivos

## 1. open + context manager

```python
with open("file.txt", encoding="utf-8") as f:
    for line in f:                 # itera sin cargar todo
        print(line.rstrip())

with open("out.txt", "w", encoding="utf-8") as f:
    f.write("hola\n")
```

Modes:
- `"r"` lectura (default), `"w"` write (trunca), `"a"` append.
- `"rb"`/`"wb"` binario → devuelve `bytes`, no `str`.
- `"x"` write exclusivo (falla si existe).
- `encoding="utf-8"` **siempre** en texto; el default depende del locale y es un bug esperando.

## 2. pathlib

```python
from pathlib import Path

p = Path("~/notes.md").expanduser()
p.read_text(encoding="utf-8")
p.write_text("...", encoding="utf-8")
p.read_bytes()
p.stem, p.suffix, p.parent, p.name
p.with_suffix(".bak")
p.exists(); p.is_file(); p.is_dir()
p.mkdir(parents=True, exist_ok=True)
p.unlink(missing_ok=True)

for py in Path("src").rglob("*.py"):
    print(py)
```

Preferilo sobre `os.path.join` / `os.listdir`.

## 3. tempfile

```python
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as d:
    p = Path(d) / "x.txt"
    p.write_text("hola")
    # al salir: el dir se borra entero
```

Para tests, `tmp_path` (fixture de pytest) ya te da uno.

## 4. CSV

```python
import csv
from pathlib import Path

with Path("datos.csv").open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):     # cada row es dict por header
        print(row["name"], row["age"])

with Path("out.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["name", "age"])
    w.writeheader()
    w.writerow({"name": "Ana", "age": "30"})
```

- `newline=""` es **obligatorio** en csv; si no, en Windows duplica \r.
- Los valores son siempre strings. Convertí a int/float vos.

## 5. JSON

```python
import json

data = json.loads('{"a": 1}')         # str -> dict
Path("x.json").write_text(json.dumps(data, indent=2, ensure_ascii=False))

with open("x.json") as f:
    data = json.load(f)
with open("y.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False, sort_keys=True)
```

- `ensure_ascii=False` para dejar los acentos como son.
- `sort_keys=True` para diffs reproducibles.

## 6. stdin / stdout en scripts

```python
import sys

# Patrón UNIX: si no hay archivos, leer de stdin
for line in sys.stdin:
    print(line.upper(), end="")

# fileinput: itera files + stdin unificado
import fileinput
for line in fileinput.input():       # args o stdin
    print(line.rstrip())
```

## 7. Encodings y bytes

```python
"café".encode("utf-8")      # b'caf\xc3\xa9'
b'caf\xc3\xa9'.decode()     # "café"

# Detectar fallos al leer archivo con encoding raro:
Path("x").read_text(encoding="utf-8", errors="replace")  # ← con cuidado
```

---

## Ejercicios

1. **01_csv_stats.py** — Lee CSV con columnas `name,amount`, devuelve `(total, avg, max_name)`.
2. **02_json_merge.py** — Merge recursivo de dos dicts (JSON). Último gana en conflicto escalar; dicts se mergean; listas se concatenan.
