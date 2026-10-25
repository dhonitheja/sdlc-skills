#!/usr/bin/env bash
# Run every skill's evals with and without the skill using Claude Code's `claude plugin eval`.
# Usage: ./evals/run-baseline.sh [skill-name ...]
# Requires Claude Code v2.1.269+. These are real, billed model runs.
set -eu

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
command -v claude >/dev/null || { echo "claude CLI not found"; exit 1; }

if [ "$#" -gt 0 ]; then
  SKILLS=("$@")
else
  SKILLS=()
  for d in "$ROOT"/*/evals; do SKILLS+=("$(basename "$(dirname "$d")")"); done
fi

for s in "${SKILLS[@]}"; do
  dir="$ROOT/$s"
  [ -d "$dir/evals" ] || { echo "skip $s (no evals)"; continue; }
  echo "=== $s ==="
  (cd "$dir" && claude plugin eval . --allow-tools Write,Edit,Bash --scaffold)
done

echo "Reports are under <skill>/evals/results/. Summarize them in evals/RESULTS.md."
