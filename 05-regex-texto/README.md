# 05 · Regex y texto

## 1. El módulo `re`

```python
import re

re.search(r"\d+", s)              # primer match (o None)
re.match(r"\d+", s)               # match al INICIO (anchored at start)
re.fullmatch(r"\d+", s)           # debe matchear el string entero
re.findall(r"\d+", s)             # lista de strings matcheados
re.finditer(r"\d+", s)            # iter de Match (más info que findall)
re.sub(r"\s+", " ", s)            # replace
re.split(r"[,;]\s*", s)           # split con regex
```

Compilar si lo usás muchas veces:
```python
_IP = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
for m in _IP.finditer(log):
    ...
```

## 2. Flags

```python
re.IGNORECASE  # re.I
re.MULTILINE   # re.M → ^/$ matchean cada línea
re.DOTALL      # re.S → . matchea newlines
re.VERBOSE     # re.X → ignora whitespace y # comentarios en el pattern

re.search(r"foo", s, re.I | re.M)
# o inline:
re.search(r"(?im)foo", s)
```

## 3. Grupos

```python
m = re.search(r"(\w+)@(\w+\.\w+)", s)
if m:
    user, domain = m.group(1), m.group(2)
    user, domain = m.groups()
    user         = m[1]                      # subscript también

# Named groups:
m = re.search(r"(?P<user>\w+)@(?P<domain>\S+)", s)
m.group("user"), m["domain"]

# Non-capturing: (?:...) → no cuenta como grupo
re.findall(r"(?:ab)+", s)
```

## 4. Replacements con backrefs

```python
re.sub(r"(\w+)@(\S+)", r"\2/\1", s)                     # swap
re.sub(r"(?P<u>\w+)@", r"\g<u>_AT_", s)                 # named
re.sub(r"\d+", lambda m: str(int(m.group()) * 2), s)    # función como repl
```

## 5. Patrones típicos

```python
r"\b\w+\b"             # palabra
r"\s+"                 # cualquier whitespace
r"^\s*#"               # línea comentada (con re.M)
r"https?://\S+"        # URL simple
r"\b(?:\d{1,3}\.){3}\d{1,3}\b"   # IPv4 (laxo)
r"[\w.+-]+@[\w-]+\.[\w.-]+"      # email laxo
r"'[^']*'|\"[^\"]*\""            # strings quoted
```

Regla: **no uses regex para parsear HTML, JSON ni shell**. Hay parsers.

## 6. Pitfalls

```python
# Backslash hell: SIEMPRE raw strings
re.search("\\d+", s)      # ok pero feo
re.search(r"\d+", s)      # mejor

# Greedy vs lazy
re.search(r"<(.+)>", "<a><b>")      # grupo = "a><b"  (greedy)
re.search(r"<(.+?)>", "<a><b>")     # grupo = "a"     (lazy)

# findall con grupos devuelve tuplas, no strings:
re.findall(r"(\w+)=(\w+)", "a=1 b=2")   # [('a','1'), ('b','2')]
```

---

## Ejercicios

1. **01_extract_ips.py** — `extract_ips(text)` devuelve lista de IPs únicas en orden de aparición. Valida 0-255 por octeto.
2. **02_redact_emails.py** — `redact_emails(text)` reemplaza cada email por `***@<dominio>`. Preserva el resto.
