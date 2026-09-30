"""Run the self-contained SQL Learning laboratory."""
from __future__ import annotations
import argparse
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SQL_DIR = ROOT / "learning" / "sql"
LESSONS = {
    1: ("SELECT, WHERE, ORDER BY", "demo_01_select.sql"),
    2: ("JOIN és aggregáció", "demo_02_join.sql"),
    3: ("CTE és ablakfüggvény", "demo_03_advanced.sql"),
    4: ("NULL és COALESCE", "demo_04_null.sql"),
    5: ("HAVING", "demo_05_having.sql"),
    6: ("Al-lekérdezések", "demo_06_subqueries.sql"),
    7: ("CASE", "demo_07_case.sql"),
    8: ("Biztonságos módosítás", "demo_08_modification.sql"),
    9: ("Index és EXPLAIN QUERY PLAN", "demo_09_index.sql"),
}

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


def statements(text: str):
    """Yield simple semicolon-terminated statements from a learner SQL file."""
    current = []
    for line in text.splitlines():
        if line.strip().startswith("--"):
            continue
        current.append(line)
        if sqlite3.complete_statement("\n".join(current)):
            statement = "\n".join(current).strip()
            if statement:
                yield statement
            current = []
    remainder = "\n".join(current).strip()
    if remainder:
        yield remainder

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


def run_file(path: Path) -> None:
    with sqlite3.connect(":memory:") as db:
        db.executescript((SQL_DIR / "schema.sql").read_text(encoding="utf-8"))
        print(f"\n=== Saját SQL: {path} ===")
        for statement in statements(path.read_text(encoding="utf-8")):
            cursor = db.execute(statement)
            if cursor.description:
                print("SQL:", " ".join(statement.split()))
                for row in cursor.fetchall():
                    print("  ", tuple(row))
            else:
                changed = f" ({cursor.rowcount} módosított sor)" if cursor.rowcount >= 0 else ""
                print(f"OK{changed}:", " ".join(statement.split()))

def main() -> int:
    parser = argparse.ArgumentParser(description="Futtasd a SQL Learning SQLite laborját")
    parser.add_argument("--lesson", type=int, choices=sorted(LESSONS))
    parser.add_argument("--file", type=Path, help="saját SQL-fájl futtatása a laboradaton")
    parser.add_argument("--list", action="store_true")
    args = parser.parse_args()
    if args.file and args.lesson:
        parser.error("a --file és --lesson együtt nem használható")
    if args.list:
        for number, (title, _) in LESSONS.items():
            print(f"{number}: {title}")
        return 0
    if args.file:
        run_file(args.file)
    else:
        run(args.lesson)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
