# 5. HAVING: csoportok szűrése

## Cél

Különböztesd meg a sorok szűrésére használt `WHERE` és a már létrejött csoportok szűrésére használt `HAVING` szerepét.

```sql
SELECT customer_id, COUNT(*) AS order_count
FROM orders
WHERE status <> 'cancelled'
GROUP BY customer_id
HAVING COUNT(*) >= 2;
```

A `WHERE` még a csoportosítás előtt szűr, a `HAVING` az aggregáció után. Ha egy feltétel soronként kifejezhető, általában `WHERE`-be kerüljön.

## Gyakorlat

Oldd meg a [`07-having.sql`](../exercises/07-having.sql) feladatot. A referencia: [HAVING](../../content/02-sql-fundamentals/having.md).
