# 15. Query optimalizálás

## Cél

Ne vakon „gyorsíts” SQL-t: hasonlítsd össze a tervet, a cardinality-becslést, a szűrés formáját és a mért futási időt.

Az optimalizálási ciklus: reprodukálható mérés → `EXPLAIN`/`EXPLAIN QUERY PLAN` → szűk keresztmetszet azonosítása → egy változtatás → újramérés. A helyes eredmény és a teljesítmény két külön ellenőrzés.

Például egy index általában segíthet az `orders.customer_id = ?` keresésen, de a `customer_id + 0 = ?` vagy egy nem megfelelően vezetett összetett index ronthatja a használhatóságot. A konkrét planner-döntést mindig a célrendszeren vizsgáld.

## Gyakorlat

Oldd meg a [`15-optimization.sql`](../exercises/15-optimization.sql) feladatot. A referencia: [Query Tuning Workflow](../../content/09-query-performance-and-optimization/query-tuning-workflow.md).
