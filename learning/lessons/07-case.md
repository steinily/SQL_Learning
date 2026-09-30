# 7. CASE és üzleti kategóriák

## Cél

Alakíts át értékeket üzleti kategóriává `CASE` segítségével, és adj minden ágnak egyértelmű jelentést.

```sql
SELECT name, unit_price,
       CASE
           WHEN unit_price < 5000 THEN 'cheap'
           WHEN unit_price < 15000 THEN 'standard'
           ELSE 'premium'
       END AS price_band
FROM products
ORDER BY unit_price;
```

A `CASE` ágai felülről lefelé kerülnek kiértékelésre. Legyen `ELSE` ág is, különben a nem illeszkedő sorok NULL-t kaphatnak.

## Gyakorlat

Oldd meg a [`09-case.sql`](../exercises/09-case.sql) feladatot. A referencia: [CASE Expressions](../../content/03-intermediate-sql/case-expressions.md).
