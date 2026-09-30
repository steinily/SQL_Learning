# 6. Al-lekérdezések

## Cél

Használj scalar subquery-t egy értékhez, `IN`-t több lehetséges értékhez, és `EXISTS`-et annak vizsgálatára, hogy létezik-e kapcsolódó sor.

```sql
SELECT name, unit_price
FROM products
WHERE unit_price > (SELECT AVG(unit_price) FROM products);
```

Az `EXISTS` nem a kapcsolt sorok számát adja vissza, hanem azt kérdezi: van legalább egy illeszkedő sor? Ezért gyakran jó választás duplikációk elkerülésére.

## Gyakorlat

Oldd meg a [`08-subqueries.sql`](../exercises/08-subqueries.sql) feladatot. Hasonlítsd össze az `IN` és `EXISTS` megoldást, és olvasd el a [Subquery Fundamentals](../../content/03-intermediate-sql/subquery-fundamentals.md) anyagot.
