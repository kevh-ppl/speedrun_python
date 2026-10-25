# retos · katas integradoras

Cada reto combina varios módulos. Pensados para ~1-2h cada uno.

| Reto                           | Tema principal                            | Módulos tocados |
|--------------------------------|-------------------------------------------|-----------------|
| 00_safe_rm.py                  | wrapper seguro de rm con papelera         | 00, 03, 04      |
| 01_log_analyzer.py             | parse de access.log con top-N IPs          | 01, 03, 05      |
| 02_json_patch.py               | aplica un patch estilo JSON Pointer        | 03, 06          |
| 03_tcp_check.py                | health-check TCP + retry con backoff       | 02, 04, 06      |
| 04_dir_report.py               | reporte Markdown del tamaño de un árbol    | 03, 04, 06      |

Formato: igual que los módulos (ejercicio + solución + tests).
Cada reto empieza con una **ficha**: enunciado, criterios de éxito, pistas.

Hay uno completamente armado (`00_safe_rm.py`) como referencia. Los otros son tuyos:
copiá el molde, redactá la ficha y escribí tests antes de la solución.

---

## Ficha: 00_safe_rm

**Enunciado:**
Wrapper de borrado que mueve a papelera por defecto y rechaza paths peligrosos.

**CLI:**
```
safe_rm.py [--dry-run] [--force] PATH [PATH...]
```

**Criterios de éxito:**
- [ ] Rechaza `/`, `$HOME`, y rutas cuyo resolve termine en una de esas.
- [ ] Rechaza paths que no existen (exit 1).
- [ ] `--dry-run` no toca nada; imprime lo que haría.
- [ ] Sin `--force`: mueve a `~/.trash/<ISO-8601>/`.
- [ ] Con `--force`: borra de verdad (`unlink` o `rmtree`).
- [ ] Si varios paths tienen el mismo basename en la papelera, no se pisan.

**Pistas:**
- `Path.resolve()` antes de validar.
- `datetime.now().isoformat(timespec="seconds")` para el timestamp.
- `shutil.move` cruza filesystems; `shutil.rmtree` para dirs.
- Testeable: factorizá en `safe_rm(paths, dry_run, force, trash_root, home_root)`.
