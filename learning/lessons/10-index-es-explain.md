# 10. Index és EXPLAIN QUERY PLAN

## Cél

Értsd meg, hogy az index a keresést segítő struktúra, de nem automatikus gyorsítás. Tanuld meg az SQLite `EXPLAIN QUERY PLAN` alapját.

```sql
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
EXPLAIN QUERY PLAN
SELECT * FROM orders WHERE customer_id = 1;
```

Az indexnek írási és tárhely-költsége van, ezért csak mérés és használati minta alapján hozz létre. A kis laboradatbázisban a planner döntése nem feltétlenül tükrözi production méretű adatok viselkedését.

## Gyakorlat

Oldd meg a [`10-index.sql`](../exercises/10-index.sql) feladatot, és olvasd el az [Indexing Overview](../../content/08-indexing/indexing-overview.md) anyagot. A cél nem az, hogy mindenáron indexet hozz létre, hanem hogy meg tudd indokolni a döntést.
