"""Run the self-contained SQL Learning laboratory."""
from __future__ import annotations
import argparse
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SQL_DIR = ROOT / "learning" / "sql"
LESSONS = {1: ("SELECT, WHERE, ORDER BY", "demo_01_select.sql"), 2: ("JOIN és aggregáció", "demo_02_join.sql"), 3: ("CTE és ablakfüggvény", "demo_03_advanced.sql")}

def queries(text: str):
    current = []
    for line in text.splitlines():
        if line.strip().lower().startswith("-- query:"):
            if current:
                yield "\n".join(current)
            current = []
        elif not line.strip().startswith("--"):
            current.append(line)
    if current:
        yield "\n".join(current)

def run(number: int | None) -> None:
    selected = LESSONS.items() if number is None else [(number, LESSONS[number])]
    with sqlite3.connect(":memory:") as db:
        db.executescript((SQL_DIR / "schema.sql").read_text(encoding="utf-8"))
        for lesson_no, (title, filename) in selected:
            print(f"\n=== {lesson_no}. {title} ===")
            for query in queries((SQL_DIR / filename).read_text(encoding="utf-8")):
                rows = db.execute(query).fetchall()
                print("SQL:", " ".join(query.split()))
                for row in rows:
                    print("  ", tuple(row))

def main() -> int:
    parser = argparse.ArgumentParser(description="Futtasd a SQL Learning SQLite laborját")
    parser.add_argument("--lesson", type=int, choices=sorted(LESSONS))
    parser.add_argument("--list", action="store_true")
    args = parser.parse_args()
    if args.list:
        for number, (title, _) in LESSONS.items():
            print(f"{number}: {title}")
        return 0
    run(args.lesson)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
