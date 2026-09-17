#!/usr/bin/env python3
import csv
import hashlib
import json
import sys
from pathlib import Path

EXPECTED_MD5 = "60f1ae344334037c5064ce532300fae5"
FEATURES = {"GB147", "GB155", "GB302"}

def load(path):
    by_language = {}
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            feature = row["Parameter_ID"]
            if feature not in FEATURES:
                continue
            by_language.setdefault(row["Language_ID"], {})[feature] = row["Value"]
    return by_language

def cross(by_language, row_feature, col_feature):
    counts = {(r, c): 0 for r in ("0", "1") for c in ("0", "1")}
    for values in by_language.values():
        r = values.get(row_feature)
        c = values.get(col_feature)
        if r in ("0", "1") and c in ("0", "1"):
            counts[(r, c)] += 1
    return {
        "0_0": counts[("0", "0")],
        "0_1": counts[("0", "1")],
        "1_0": counts[("1", "0")],
        "1_1": counts[("1", "1")],
        "n": sum(counts.values()),
    }

def main():
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "/data/grambank-values.csv")
    md5 = hashlib.md5(path.read_bytes()).hexdigest()
    if md5 != EXPECTED_MD5:
        raise SystemExit(f"wrong dataset md5: {md5}")
    by_language = load(path)
    out = {
        "dataset_md5": md5,
        "table_a": cross(by_language, "GB147", "GB155"),
        "table_b": cross(by_language, "GB302", "GB155"),
    }
    print(json.dumps(out, sort_keys=True))

if __name__ == "__main__":
    main()
