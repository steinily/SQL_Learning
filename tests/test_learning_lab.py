from pathlib import Path
import sqlite3

from scripts.learning_runner import statements

ROOT = Path(__file__).resolve().parents[1]


def test_learning_schema_is_executable_and_has_expected_tables():
    with sqlite3.connect(":memory:") as db:
        db.executescript((ROOT / "learning/sql/schema.sql").read_text(encoding="utf-8"))
        tables = {row[0] for row in db.execute("SELECT name FROM sqlite_master WHERE type = 'table'")}
        assert {"customers", "products", "orders", "order_items"} <= tables
        assert db.execute("SELECT COUNT(*) FROM customers").fetchone() == (4,)


def test_learning_demo_queries_return_deterministic_results():
    with sqlite3.connect(":memory:") as db:
        db.executescript((ROOT / "learning/sql/schema.sql").read_text(encoding="utf-8"))
        row = db.execute(
            "SELECT SUM(oi.quantity * p.unit_price) "
            "FROM orders o JOIN order_items oi ON oi.order_id = o.order_id "
            "JOIN products p ON p.product_id = oi.product_id "
            "WHERE o.order_id = 1001"
        ).fetchone()
        assert row == (17000,)


def test_learning_runner_splits_learner_sql_statements():
    sql = "-- feladat\nSELECT 1;\nSELECT 2;\n"
    assert list(statements(sql)) == ["SELECT 1;", "SELECT 2;"]
