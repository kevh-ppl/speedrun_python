"""extract_ips con validación de octetos."""
from __future__ import annotations

import re

_IP_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")


def _valid(ip: str) -> bool:
    return all(0 <= int(o) <= 255 for o in ip.split("."))


def extract_ips(text: str) -> list[str]:
    found = (m.group() for m in _IP_RE.finditer(text) if _valid(m.group()))
    return list(dict.fromkeys(found))
