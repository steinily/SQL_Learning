# 12. Window function frame-ek

## Cél

Használj ablakfüggvényt úgy, hogy az eredeti sorok megmaradjanak, és tudd megkülönböztetni a `PARTITION BY`, az `ORDER BY` és a frame szerepét.

```sql
SELECT o.order_id, o.order_date,
       SUM(oi.quantity * p.unit_price) OVER (
           ORDER BY o.order_date, o.order_id
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_total
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p ON p.product_id = oi.product_id;
```

Az aggregáció csoportot sűrít, az ablakfüggvény a sorokat megtartja. A frame mondja meg, hogy az aktuális sorhoz képest mely sorok tartoznak a számításba; a rendezésnél használj determinisztikus tie-breakert is.

## Gyakorlat

Oldd meg a [`12-window.sql`](../exercises/12-window.sql) feladatot, majd futtasd a `python3 scripts/learning_runner.py --lesson 10` demót. A referencia: [Window Frames](../../content/04-advanced-sql/window-frames.md).
