"""Helpers compartidos para los tests pytest.

Carga: `from labhelp import load_exercise, exercise_path, solution_path`

load_exercise:
    Carga como módulo el archivo del ejercicio. Si el archivo está vacío o
    contiene el marcador `# TODO: tu codigo aqui`, cae a la solución de
    referencia para que los tests pasen y veas el "verde" base.

exercise_path / solution_path:
    Devuelven el Path. Útil para tests de scripts CLI que se ejecutan por
    subprocess.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType

TODO_MARKER = "# TODO: tu codigo aqui"


def _module_root(test_file: str) -> Path:
    # tests/<x>.py -> módulo (p.ej. 00-fundamentos/)
    return Path(test_file).resolve().parent.parent


def exercise_path(filename: str, test_file: str) -> Path:
    return _module_root(test_file) / "ejercicios" / filename


def solution_path(filename: str, test_file: str) -> Path:
    return _module_root(test_file) / "solucion" / filename


def pick_path(filename: str, test_file: str) -> Path:
    """Decide si usar el ejercicio o la solución según el contenido."""
    ex = exercise_path(filename, test_file)
    sol = solution_path(filename, test_file)
    if not ex.exists():
        return sol
    text = ex.read_text(encoding="utf-8")
    if not text.strip() or TODO_MARKER in text:
        return sol
    return ex


def load_exercise(filename: str, test_file: str) -> ModuleType:
    path = pick_path(filename, test_file)
    # Nombre único por path para no chocar en sys.modules.
    mod_name = f"lab_{path.parent.parent.name}_{path.stem}".replace("-", "_")
    spec = importlib.util.spec_from_file_location(mod_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"no se pudo cargar {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[mod_name] = mod
    spec.loader.exec_module(mod)
    return mod
