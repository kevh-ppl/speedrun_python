"""EJERCICIO 02 — redact_emails.

Objetivo:
  `redact_emails(text: str) -> str` reemplaza cada email por `***@<dominio>`.
  El resto del texto queda igual.

Reglas:
  - Email laxo: [\\w.+-]+@[\\w-]+\\.[\\w.-]+
  - Preserva el dominio original.

Ejemplos:
  redact_emails("hola kevin@acme.com saludos")           -> "hola ***@acme.com saludos"
  redact_emails("multi: a@x.com b@y.com")                -> "multi: ***@x.com ***@y.com"
  redact_emails("sin emails aqui")                       -> "sin emails aqui"
"""
from __future__ import annotations


# TODO: tu codigo aqui


def redact_emails(text: str) -> str:
    raise NotImplementedError
