"""Demonstrate a short SQLite lock wait using two isolated connections."""
from __future__ import annotations

import sqlite3
import tempfile
from pathlib import Path


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="sql-learning-lock-") as directory:
        database = Path(directory) / "locking.sqlite"
        setup = sqlite3.connect(database)
        setup.execute("CREATE TABLE accounts (account_id INTEGER PRIMARY KEY, balance INTEGER NOT NULL)")
        setup.execute("INSERT INTO accounts VALUES (1, 100)")
        setup.commit()
        setup.close()

        first = sqlite3.connect(database, timeout=1)
        second = sqlite3.connect(database, timeout=0.1)
        try:
            first.execute("BEGIN IMMEDIATE")
            first.execute("UPDATE accounts SET balance = balance - 10 WHERE account_id = 1")
            try:
                second.execute("UPDATE accounts SET balance = balance + 10 WHERE account_id = 1")
            except sqlite3.OperationalError as error:
                print("Második kapcsolat:", error)
                print("Tanulság: a második író várakozik az első tranzakció lockjára.")
            first.rollback()
        finally:
            first.close()
            second.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
