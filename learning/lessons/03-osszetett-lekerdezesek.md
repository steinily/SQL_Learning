# 3. Összetett lekérdezések

## Cél

Bonts összetett problémát olvasható részekre CTE-vel (`WITH`), és használj ablakfüggvényt úgy, hogy az eredeti sorok megmaradjanak.

Előfeltétel: az 1–2. lecke, különösen a `JOIN`, `GROUP BY` és `SUM` használata.

```sql
WITH totals AS (
    SELECT o.customer_id, SUM(oi.quantity) AS item_count
    FROM orders AS o
    JOIN order_items AS oi ON oi.order_id = o.order_id
    GROUP BY o.customer_id
)
SELECT * FROM totals;
```

Az aggregáció egy csoportot egy sorra sűrít. A `RANK() OVER (...)` ezzel szemben minden terméksort megtart, és mellé rangot számol.

Feladat: [`03-advanced.sql`](../exercises/03-advanced.sql). A saját SQL-edet a `python3 scripts/learning_runner.py --file my-answer.sql` paranccsal futtasd. A referencia: [CTE Fundamentals](../../content/03-intermediate-sql/cte-fundamentals.md).
