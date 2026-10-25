from __future__ import annotations

from labhelp import load_exercise

mod = load_exercise("02_redact_emails.py", __file__)


def test_simple() -> None:
    assert mod.redact_emails("hola kevin@acme.com saludos") == "hola ***@acme.com saludos"


def test_varios() -> None:
    r = mod.redact_emails("multi: a@x.com b@y.com")
    assert r == "multi: ***@x.com ***@y.com"


def test_sin_emails() -> None:
    assert mod.redact_emails("sin emails aqui") == "sin emails aqui"


def test_vacio() -> None:
    assert mod.redact_emails("") == ""


def test_preserva_dominio_con_subdominios() -> None:
    assert mod.redact_emails("x@sub.dom.co") == "***@sub.dom.co"
