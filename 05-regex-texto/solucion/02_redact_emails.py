"""redact_emails con backref al dominio."""
from __future__ import annotations

import re

_EMAIL_RE = re.compile(r"[\w.+-]+@([\w-]+\.[\w.-]+)")


def redact_emails(text: str) -> str:
    return _EMAIL_RE.sub(r"***@\1", text)
