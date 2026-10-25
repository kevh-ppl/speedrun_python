"""csv_stats: total, avg, max_name."""
from __future__ import annotations

import csv
from pathlib import Path


def csv_stats(path: Path) -> tuple[float, float, str]:
    total = 0.0
    count = 0
    max_amount = float("-inf")
    max_name = ""
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None or {"name", "amount"} - set(reader.fieldnames):
            raise ValueError("CSV debe tener columnas 'name' y 'amount'")
        for row in reader:
            amt = float(row["amount"])
            total += amt
            count += 1
            if amt > max_amount:
                max_amount = amt
                max_name = row["name"]
    avg = total / count if count else 0.0
    return total, avg, max_name
