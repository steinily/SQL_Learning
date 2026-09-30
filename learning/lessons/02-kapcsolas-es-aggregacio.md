# 2. Kapcsolás és aggregáció

## Cél

Tudd összekapcsolni a táblákat `JOIN ... ON` segítségével, és csoportonként számolni `COUNT`, `SUM` vagy `AVG` függvénnyel.

```sql
SELECT c.name, COUNT(o.order_id) AS order_count
FROM customers AS c
LEFT JOIN orders AS o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY order_count DESC, c.name;
```

Az `INNER JOIN` csak a mindkét oldalon illeszkedő sorokat adja. A `LEFT JOIN` a bal oldali sorokat akkor is megtartja, ha nincs párjuk. Ezért használjuk, ha a nulla rendeléssel rendelkező vevőket is látni akarjuk.

Nyisd meg a [`02-join.sql`](../exercises/02-join.sql) feladatot. Figyelj rá, hogy a rendelési érték `quantity * unit_price` legyen, ne csak az egységár összege.
