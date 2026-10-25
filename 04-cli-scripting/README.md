# 04 · CLI scripting

Scripts que se portan bien en un pipeline UNIX: exit codes correctos,
stderr para logs, stdout para datos, señales respetadas.

## 1. argparse en serio

```python
import argparse

p = argparse.ArgumentParser(
    prog="mi-tool",
    description="hace cosas",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,  # muestra defaults en --help
)
p.add_argument("input", type=argparse.FileType("r"), help="archivo (o - para stdin)")
p.add_argument("-n", "--lines", type=int, default=10)
p.add_argument("-v", "--verbose", action="count", default=0)   # -vvv -> 3
p.add_argument("--format", choices=["json", "csv"], default="json")
p.add_argument("--dry-run", action="store_true")
args = p.parse_args()
```

- `argparse.FileType("r")` ya maneja `-` como stdin.
- `action="count"` acumula; útil para niveles de verbosidad.
- `choices` valida; cualquier otro valor sale con 2.

Subcomandos (patrón `git <cmd>`):
```python
sub = p.add_subparsers(dest="cmd", required=True)
up = sub.add_parser("up", help="arranca")
up.add_argument("--port", type=int, default=8080)
down = sub.add_parser("down")
# luego: if args.cmd == "up": ...
```

## 2. Exit codes

| Code | Significado           |
|------|-----------------------|
| 0    | ok                    |
| 1    | error genérico        |
| 2    | mal uso (argparse)    |
| 130  | Ctrl-C (SIGINT)       |

```python
def main() -> int:
    try:
        ...
        return 0
    except FileNotFoundError as e:
        print(f"no existe: {e.filename}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        return 130

raise SystemExit(main())
```

## 3. subprocess bien

```python
import subprocess

# Lo que querés el 90% de las veces:
r = subprocess.run(
    ["git", "status", "--porcelain"],
    capture_output=True,
    text=True,          # str, no bytes
    check=True,         # levanta CalledProcessError si exit != 0
    timeout=30,
)
print(r.stdout)
```

- **Nunca `shell=True` con input del usuario**: inyección de comandos.
- `text=True` + `encoding="utf-8"` para strings, si no obtenés bytes.
- Si necesitás streaming, usá `subprocess.Popen` con `stdout=PIPE` y leé línea a línea.

## 4. Logging > print

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    stream=sys.stderr,
)
log = logging.getLogger("mi-tool")
log.info("arrancando")
log.warning("algo raro: %s", x)        # lazy formatting, no f-string
log.error("falló %s", path, exc_info=True)  # incluye traceback
```

- Niveles: DEBUG < INFO < WARNING < ERROR < CRITICAL.
- Mapeá `-v` a `WARNING`, `-vv` a `INFO`, `-vvv` a `DEBUG`.
- `log.exception(...)` dentro de un `except` incluye el traceback automáticamente.

## 5. Señales

```python
import signal

def handle(sig, frame):
    print("adiós", file=sys.stderr)
    raise SystemExit(130)

signal.signal(signal.SIGTERM, handle)
```

Para la mayoría de scripts: dejá que `KeyboardInterrupt` haga su trabajo.

## 6. Environment

```python
import os

level = os.environ.get("LOG_LEVEL", "INFO")   # con default
token = os.environ["API_TOKEN"]                # KeyError si falta
```

Patrón: valida variables requeridas al arrancar, no en medio del código.

---

## Ejercicios

1. **01_grep_mini.py** — Mini-grep con argparse: `grep_mini.py PATTERN [FILE...]`, `-n` muestra línea, `-i` ignore-case, lee stdin si no hay files.
2. **02_run_ok.py** — Función `run_ok(cmd: list[str], timeout: int) -> tuple[int, str, str]` que corre subprocess y devuelve `(returncode, stdout, stderr)` sin levantar.
