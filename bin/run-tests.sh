#!/usr/bin/env bash
# Runner de tests pytest. Uso: bin/run-tests.sh [modulo]
set -euo pipefail

mod="${1:-}"
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

if [[ -n "$mod" ]]; then
  dirs=("$mod")
else
  mapfile -t dirs < <(find . -maxdepth 1 -type d -regex '\./[0-9]+-.*' | sort)
  dirs+=("retos")
fi

fail=0
for d in "${dirs[@]}"; do
  d="${d#./}"
  if [[ ! -d "$d/tests" ]]; then
    echo "[skip] $d (sin tests/)"
    continue
  fi
  echo "=== $d ==="
  if ! PYTHONPATH="$root/lib:$root/$d" pytest -q --rootdir="$root" "$d/tests"; then
    fail=1
  fi
done

exit "$fail"
