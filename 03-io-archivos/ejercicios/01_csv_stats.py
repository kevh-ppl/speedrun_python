"""EJERCICIO 01 — CSV stats.

Objetivo:
  `csv_stats(path)` lee un CSV con header `name,amount` donde amount es un
  número (int o float) y devuelve una tupla `(total, avg, max_name)`:
    - total: suma de amounts (float).
    - avg:   promedio (float). Si el archivo está vacío (sin filas), 0.0.
    - max_name: nombre con mayor amount; si vacío, cadena vacía.
  Si el CSV no tiene esas columnas, levantar ValueError.

Pistas:
  - csv.DictReader con `newline=""`.
  - float(row["amount"]) para convertir.
"""
from __future__ import annotations

from pathlib import Path


# TODO: tu codigo aqui


def csv_stats(path: Path) -> tuple[float, float, str]:
    raise NotImplementedError
