#!/usr/bin/env python3
import csv
import hashlib
import json
import sys
from pathlib import Path

EXPECTED_MD5 = "866d36bc83ab21bdb5837ffa63dc5993"

def load(path):
    inventories = {}
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if row["Marginal"] == "TRUE":
                continue
            inv_id = int(row["InventoryID"])
            item = inventories.setdefault(inv_id, {
                "glottocode": row["Glottocode"],
                "ejective": False,
                "ng": False,
            })
            item["ejective"] |= row["raisedLarynxEjective"] == "+"
            item["ng"] |= row["Phoneme"] == "ŋ"
    return inventories

def table(items):
    counts = {(e, n): 0 for e in (False, True) for n in (False, True)}
    for item in items:
        counts[(item["ejective"], item["ng"])] += 1
    return {
        "ejective_ng": counts[(True, True)],
        "ejective_no_ng": counts[(True, False)],
        "no_ejective_ng": counts[(False, True)],
        "no_ejective_no_ng": counts[(False, False)],
    }

def main():
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "/data/phoible.csv")
    md5 = hashlib.md5(path.read_bytes()).hexdigest()
    if md5 != EXPECTED_MD5:
        raise SystemExit(f"wrong dataset md5: {md5}")
    inventories = load(path)
    table_a = table(inventories.values())
    by_language = {}
    for inv_id, item in inventories.items():
        if item["glottocode"] == "NA":
            continue
        old = by_language.get(item["glottocode"])
        if old is None or inv_id < old[0]:
            by_language[item["glottocode"]] = (inv_id, item)
    table_b = table(item for _, item in by_language.values())
    out = {
        "dataset_md5": md5,
        "inventory_count": len(inventories),
        "language_count": len(by_language),
        "table_a": table_a,
        "table_b": table_b,
    }
    print(json.dumps(out, sort_keys=True))

if __name__ == "__main__":
    main()
