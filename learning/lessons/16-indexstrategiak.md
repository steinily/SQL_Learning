# 16. Indexstratégiák

## Cél

Válassz indexet a hozzáférési minta alapján: összetett indexnél a bal szélső oszlopok, részleges indexnél a stabil predicate, covering indexnél pedig a lefedett oszlopok számítanak.

```sql
CREATE INDEX idx_orders_status_date
ON orders(status, order_date);
```

Az index nem ingyenes: tárhelyet, írási költséget és karbantartást kér. Ne a tábla minden oszlopára hozz létre indexet; előbb kérdezési mintát és tervet gyűjts.

## Gyakorlat

Oldd meg a [`16-index-strategy.sql`](../exercises/16-index-strategy.sql) feladatot, majd futtasd a `python3 scripts/learning_runner.py --lesson 14` demót. A referencia: [Composite Indexes](../../content/08-indexing/composite-indexes.md).
