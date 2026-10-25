"""EJERCICIO 01 — extract_ips.

Objetivo:
  `extract_ips(text: str) -> list[str]` devuelve las IPv4 únicas que aparecen
  en text, en orden de PRIMERA aparición. Valida que cada octeto esté en 0..255.

Ejemplos:
  extract_ips("algo 10.0.0.1 y 999.1.1.1 y 10.0.0.1")  -> ["10.0.0.1"]
  extract_ips("1.2.3.4, 255.255.255.255")              -> ["1.2.3.4", "255.255.255.255"]
  extract_ips("")                                      -> []

Pistas:
  - Regex laxo (`\b(?:\d{1,3}\.){3}\d{1,3}\b`), luego valida los octetos en Python.
  - dedup preservando orden (dict.fromkeys sirve ahora, no estamos en el ejercicio 01).
"""
from __future__ import annotations


# TODO: tu codigo aqui


def extract_ips(text: str) -> list[str]:
    raise NotImplementedError
