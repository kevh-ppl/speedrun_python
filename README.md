# speedrun_python

Lab de refresco y profundización en **Python 3 para scripting** con enfoque mixto:
módulos cortos (teoría densa + ejercicios con tests automáticos) y retos integradores al cierre.

Mismo espíritu que `speedrun_linux`: cheat sheet ejecutable, no un libro.

## Filosofía

- **Práctica sobre teoría**: cada README es una referencia densa, no un tutorial.
- **Fallos reproducibles**: todo corre dentro de un contenedor Docker descartable.
- **Verificación**: cada ejercicio tiene su `test_*.py` (pytest) que te dice si pasa o no.
- **Progresión intermedia**: asume que ya escribiste Python, pero no que recuerdas `__slots__`, `functools.cache`, o la diferencia entre `is` y `==`.
- **Scripting idiomático**: nada de "cómo instalar Python". Esto es sobre `argparse`, `pathlib`, generadores, decoradores, dataclasses y typing bien usados.

## Estructura

```
speedrun_python/
├── docker/                      Dockerfile del entorno (python 3.12 + pytest + ruff + mypy)
├── lib/                         helpers compartidos (carga ejercicio o solución)
├── bin/                         runner de tests y lint
├── 00-fundamentos/              tipos, control flow, strict scripting
├── 01-estructuras-datos/        list/dict/set, comprehensions, generadores
├── 02-funciones-decoradores/    *args/**kwargs, closures, decoradores, functools
├── 03-io-archivos/              pathlib, context managers, csv, json
├── 04-cli-scripting/            argparse, subprocess, logging, stdin/stdout
├── 05-regex-texto/              re, parsing, formatting
├── 06-oop-tipado/               clases, dataclasses, typing, excepciones custom
└── retos/                       katas integradoras
```

Cada módulo:
```
NN-tema/
├── README.md          teoría + guía
├── ejercicios/        esqueletos para que completes (con marcador TODO)
├── solucion/          referencia (NO mires antes)
└── tests/             test_*.py que valida tu solución
```

El runner de tests busca primero el `ejercicio/`; si está vacío o tiene el marcador
`# TODO: tu codigo aqui`, cae al `solucion/`. Así puedes correr `make test` desde
el minuto cero y ver el verde de referencia, y luego ir reemplazando con tu versión.

## Uso rápido

```bash
# Construir imagen (una vez)
make build

# Entrar al contenedor
make shell

# Dentro del contenedor:
cd 00-fundamentos
cat README.md
$EDITOR ejercicios/01_hola_robusto.py   # resuelves
make test MOD=00-fundamentos            # verificas
```

También desde el host:
```bash
make test MOD=00-fundamentos
make test                   # corre todos
make lint                   # ruff + mypy sobre ejercicios y solucion
```

## Roadmap sugerido

| Semana | Módulos                      | Horas aprox. |
|--------|------------------------------|--------------|
| 1      | 00 + 01                      | 4-6          |
| 2      | 02 + 03                      | 6-8          |
| 3      | 04 + 05                      | 6-8          |
| 4      | 06                           | 4-5          |
| 5      | retos/                       | abierto      |

Salta si un tema te resulta trivial; profundiza con `python -m pydoc` si no.

## Convenciones

- Shebang en scripts ejecutables: `#!/usr/bin/env python3`
- `from __future__ import annotations` arriba cuando usas typing moderno en 3.9/3.10.
- Snake_case en nombres de archivo (`hola_robusto.py`), kebab-case solo en los directorios de módulo (`00-fundamentos`).
- Lint con `ruff check` y type-check con `mypy --strict` sobre `solucion/`.
- Nada de dependencias externas salvo lo que trae la imagen. Si un ejercicio
  necesita una lib, se dice en su README.

## Próximos pasos

1. `make build`
2. `make shell`
3. Abre `00-fundamentos/README.md` y empieza.
