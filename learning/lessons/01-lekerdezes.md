# 1. Az első lekérdezések

## Cél

Használd a `SELECT`, `FROM`, `WHERE`, `ORDER BY` és `LIMIT` elemeket. A `SELECT` a kívánt oszlopokat, a `FROM` a forrást, a `WHERE` a soronkénti szűrést adja meg.

```sql
SELECT name, unit_price
FROM products
WHERE category = 'accessory'
ORDER BY unit_price DESC;
```

Az SQL nem ígér sorrendet `ORDER BY` nélkül. Tartós lekérdezésben ne használj indokolatlanul `SELECT *`-ot, mert a sémaváltozás az eredmény alakját is megváltoztathatja.

## Gyakorlat

Nyisd meg a [`01-select.sql`](../exercises/01-select.sql) fájlt. Írd meg a három lekérdezést, majd ellenőrizd a [mintamegoldással](../solutions/01-select.sql).

## Tipikus hiba

A `WHERE` sorokat szűr, ezért aggregált eredmény szűrésére később a `HAVING` szolgál.
