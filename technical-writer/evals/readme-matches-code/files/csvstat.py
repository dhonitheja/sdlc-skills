#!/usr/bin/env python3
"""csvstat: print simple statistics for one numeric column of a CSV file."""
import argparse
import csv
import json
import os
import statistics
import sys


def main():
    p = argparse.ArgumentParser(description="Statistics for a CSV column")
    p.add_argument("file")
    p.add_argument("--column", required=True, help="column name")
    p.add_argument("--format", choices=["table", "json"], default="table")
    args = p.parse_args()

    delim = os.environ.get("CSVSTAT_DELIM", ",")
    with open(args.file, newline="") as f:
        rows = list(csv.DictReader(f, delimiter=delim))
    if not rows or args.column not in rows[0]:
        print(f"error: column {args.column!r} not found", file=sys.stderr)
        sys.exit(2)
    vals = [float(r[args.column]) for r in rows if r[args.column] != ""]
    out = {
        "count": len(vals),
        "mean": statistics.mean(vals),
        "median": statistics.median(vals),
        "min": min(vals),
        "max": max(vals),
    }
    if args.format == "json":
        print(json.dumps(out))
    else:
        for k, v in out.items():
            print(f"{k:<7}{v}")


if __name__ == "__main__":
    main()
