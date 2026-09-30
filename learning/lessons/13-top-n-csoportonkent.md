# 13. Top-N csoportonként

## Cél

Adj vissza minden kategóriából legfeljebb N sort, és tudd megmagyarázni a `ROW_NUMBER`, `RANK` és `DENSE_RANK` közötti tie-viselkedést.

```sql
WITH ranked AS (
    SELECT p.*, ROW_NUMBER() OVER (
        PARTITION BY category ORDER BY unit_price DESC, product_id
    ) AS position
    FROM products p
)
SELECT name, category, unit_price
FROM ranked
WHERE position <= 2;
```

A window function eredményét ugyanabban a SELECT-szinten általában nem szűrheted közvetlenül `WHERE`-rel; ezért kell CTE vagy derived table.

## Gyakorlat

Oldd meg a [`13-top-n.sql`](../exercises/13-top-n.sql) feladatot. A referencia: [Top-N per Group](../../content/04-advanced-sql/top-n-per-group.md).
