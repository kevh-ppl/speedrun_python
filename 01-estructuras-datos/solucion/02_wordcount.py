"""wordcount: counter con normalización mínima."""
from __future__ import annotations

from collections import Counter

_PUNCT = str.maketrans({c: " " for c in ".,;:!?()[]\"'"})


def wordcount(text: str) -> dict[str, int]:
    cleaned = text.lower().translate(_PUNCT)
    return dict(Counter(w for w in cleaned.split() if w))
