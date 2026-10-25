"""EJERCICIO 02 — wordcount.

Objetivo:
  `wordcount(text: str) -> dict[str, int]` que:
    - Normaliza a minúsculas.
    - Separa por whitespace (cualquier blank: espacio, tab, newline).
    - Descarta los chars de puntuación: . , ; : ! ? ( ) [ ] " '
    - Palabras vacías no cuentan.
    - Devuelve dict palabra -> frecuencia.

Ejemplos:
  wordcount("Hola, hola mundo!") -> {"hola": 2, "mundo": 1}
  wordcount("")                   -> {}

Pistas:
  - `collections.Counter` + `str.translate` o un `re.sub("[^\\w]", " ", ...)`.
  - La firma pide `dict`, pero `Counter` es un dict — ok devolverlo como tal.
"""
from __future__ import annotations


# TODO: tu codigo aqui


def wordcount(text: str) -> dict[str, int]:
    raise NotImplementedError
