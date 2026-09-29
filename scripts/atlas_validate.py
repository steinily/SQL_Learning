from __future__ import annotations

import json
import sqlite3

try:
    from .kb_core import ROOT, load_yaml
except ImportError:  # direct script execution
    from kb_core import ROOT, load_yaml


EXPECTED_COUNTS = {
    "organization": 1,
    "customer": 3,
    "product": 3,
    "sales_order": 3,
    "sales_order_line": 4,
}


def validate_atlas() -> dict[str, object]:
    version = load_yaml(ROOT / "atlas" / "VERSION.yaml")
    connection = sqlite3.connect(":memory:")
    try:
        schema = (ROOT / "atlas/v1/canonical/schema.sql").read_text(encoding="utf-8")
        fixture = (ROOT / "atlas/v1/fixtures/atlas-tiny.sql").read_text(encoding="utf-8")
        connection.executescript(schema)
        connection.executescript(fixture)
        counts = {
            table: connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            for table in EXPECTED_COUNTS
        }
        violations = connection.execute("PRAGMA foreign_key_check").fetchall()
        order_total = connection.execute(
            "SELECT SUM(quantity * unit_price) FROM sales_order_line WHERE sales_order_id = 5001"
        ).fetchone()[0]
    finally:
        connection.close()
    return {
        "atlas_version": version["atlas_version"],
        "seed": version["seed"],
        "counts": counts,
        "expected_counts": EXPECTED_COUNTS,
        "foreign_key_violations": violations,
        "order_5001_total": order_total,
        "pass": counts == EXPECTED_COUNTS and not violations and order_total == 160.0,
    }


def main() -> int:
    result = validate_atlas()
    print(json.dumps(result, indent=2))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
