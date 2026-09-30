# 4. NULL és COALESCE

## Cél

Értsd meg, hogy a `NULL` nem nulla és nem üres szöveg, hanem ismeretlen vagy hiányzó érték. Használd a `IS NULL`, `IS NOT NULL` és `COALESCE` kifejezéseket.

A `NULL = NULL` nem `TRUE`, ezért NULL keresésére nem `=`, hanem `IS NULL` kell. A `COALESCE(a, b)` az első nem NULL értéket adja vissza.

```sql
SELECT c.name, COALESCE(o.status, 'nincs rendelés') AS order_status
FROM customers AS c
LEFT JOIN orders AS o ON o.customer_id = c.customer_id
ORDER BY c.name, o.order_id;
```

## Gyakorlat

Oldd meg a [`06-null.sql`](../exercises/06-null.sql) feladatot, majd futtasd a saját fájlodat a `python3 scripts/learning_runner.py --file my-answer.sql` paranccsal. A referencia: [NULL Fundamentals](../../content/01-foundations/null-fundamentals.md).

Tipikus hiba: a `COUNT(*)` a LEFT JOIN által létrehozott NULL-os sort is megszámolja; a kapcsolt kulcsot, például `COUNT(o.order_id)`, használd, ha tényleges rendeléseket akarsz számolni.
