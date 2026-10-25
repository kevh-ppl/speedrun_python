"""to_bool: tabla explícita de strings a bool."""
from __future__ import annotations

_TRUE = {"1", "true", "yes", "y", "on"}
_FALSE = {"0", "false", "no", "n", "off"}


def to_bool(s: str) -> bool:
    key = s.strip().lower()
    if key in _TRUE:
        return True
    if key in _FALSE:
        return False
    raise ValueError(f"no boolean: {s!r}")
