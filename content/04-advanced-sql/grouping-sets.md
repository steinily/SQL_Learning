---
schema_version: 1
id: DBKB-ASQL-0014
title: GROUPING SETS
type: concept
primary_domain: advanced-sql
secondary_domains: [analytics]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-ISQL-0004]
related: [DBKB-ASQL-0015]
aliases: [multi-level grouping]
search_keywords: [grouping sets, subtotal, grand total, grouping]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ASQL-0002]
source_ids: [SRC-000036]
acceptance_criteria:
  - Több group grain egy statementbeli uniójaként magyarázza.
  - Tisztázza a subtotal NULL és GROUPING jelző kérdését.
  - PostgreSQL 18 scope-ot rögzít.
---
# GROUPING SETS

`GROUPING SETS` egy statementben több group-key kombináció aggregate eredményét adja, logical módon
mintha több `GROUP BY` eredményt `UNION ALL` kapcsolna össze.

```sql
SELECT region, product, SUM(amount)
FROM sale
GROUP BY GROUPING SETS ((region, product), (region), ());
```

Az empty grouping set grand total. Subtotal sorban a nem aktív grouping column `NULL` lehet, ami
összetéveszthető stored `NULL` dimension value-val. `GROUPING(...)` vagy engine-specifikus jelző
szükséges a két jelentés elválasztásához.

Minden output sor grainje eltérhet, ezért downstream contractban level indicator kell. Duplicate
measure join előtt ugyanúgy veszély. A repositoryban nincs elérhető PostgreSQL runtime, ezért ez a
topic source-verified; nem kap hamis SQLite execution evidence-et.

## Források

- [PostgreSQL 18 — Table Expressions](https://www.postgresql.org/docs/18/queries-table-expressions.html)
