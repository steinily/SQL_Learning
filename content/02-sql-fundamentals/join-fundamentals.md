---
schema_version: 1
id: DBKB-SQL-0016
title: Join Fundamentals
type: concept
primary_domain: sql-fundamentals
secondary_domains: [data-modeling]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlserver, sqlite]
sql_dialects: [portable-sql, postgresql, tsql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-SQL-0004, DBKB-FND-0019]
related: [DBKB-SQL-0017, DBKB-SQL-0018, DBKB-SQL-0019]
aliases: [table join]
search_keywords: [join, "on", relationship, cardinality, logical join]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-SQL-0002]
source_ids: [SRC-000022, SRC-000029]
acceptance_criteria:
  - Elkülöníti a logical join type-ot a physical join algorithmtól.
  - Megköveteli a grain és cardinality ellenőrzését.
  - Futtatható relationship join példát ad.
---
# Join Fundamentals

A join két table expression sorait kombinálja. A logical join type mondja meg, hogyan kezeljük a
matched és unmatched sorokat; a physical algorithm — például nested loops, hash vagy merge — optimizer
döntés. A két fogalmat nem szabad összekeverni.

```sql
SELECT o.order_id, c.customer_name
FROM sales_order AS o
JOIN customer AS c
  ON c.customer_id = o.customer_id;
```

Az `ON` predicate a kapcsolatot írja le. Foreign key támogatja az integrityt, de a join correctnesshez
ismerni kell mindkét oldal grain-jét és key uniquenessét. One-to-many join szándékosan megsokszorozza
az „one” oldal értékeit; aggregate előtt ez kritikus.

## Review sorrend

1. Nevezd meg mindkét input grain-jét.
2. Bizonyítsd a join key uniqueness/nullability tulajdonságait.
3. Írd le az elvárt match cardinalityt és az unmatched kezelését.
4. Hasonlíts row countot és edge case-eket, csak utána vizsgálj plant.

Hiányzó predicate Cartesian productot okozhat. `DISTINCT` nem korrekt általános javítás. Composite key
esetén minden komponens szükséges, hacsak az adatmodell más uniquenesset nem garantál.

A `SQL-SQL-0016` SQLite fixture valid foreign key mentén kombinál order és customer sorokat.

## Források

- [PostgreSQL 18 — Queries Overview](https://www.postgresql.org/docs/18/queries-overview.html)
- [Microsoft — FROM clause plus JOIN](https://learn.microsoft.com/en-us/sql/t-sql/queries/from-transact-sql?view=sql-server-ver17)
