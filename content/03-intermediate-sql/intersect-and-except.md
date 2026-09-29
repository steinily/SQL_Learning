---
schema_version: 1
id: DBKB-ISQL-0016
title: INTERSECT and EXCEPT
type: concept
primary_domain: intermediate-sql
secondary_domains: [data-quality]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-ISQL-0015]
related: [DBKB-ISQL-0017, DBKB-ISQL-0027]
aliases: [set intersection, set difference]
search_keywords: [intersect, except, minus, reconciliation]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ISQL-0002]
source_ids: [SRC-000034]
acceptance_criteria:
  - Meghatározza az intersection és difference irányát.
  - Bemutatja az ALL és vendor naming eltéréseket.
  - Futtatható reconciliation példát ad.
---
# INTERSECT and EXCEPT

`INTERSECT` a mindkét inputban jelen lévő result row-kat adja. `EXCEPT` az első inputban jelen lévő,
de a másodikban hiányzó sorokat; ezért irányérzékeny. Alapformájuk duplicate-et eliminál, az `ALL`
variáns multiplicityt kezel, ha támogatott.

```sql
SELECT customer_id FROM expected_customer
EXCEPT
SELECT customer_id FROM actual_customer;
```

Ez hasznos reconciliationnél, de a reverse difference-et is futtatni kell a teljes equality
ellenőrzéséhez. Column count, position és compatible type ugyanúgy contract, mint `UNION` esetén.

Egyes vendorok `MINUS` nevet használnak `EXCEPT` helyett, és az `ALL` támogatás eltérhet. Combined
set operationsnél zárójelekkel tedd explicit-té a precedence-et; PostgreSQLben `INTERSECT` erősebben
köt, mint `UNION` és `EXCEPT`.

A `SQL-ISQL-0016` expected és actual id-k intersectionjét és hiányzó id-jét ellenőrzi SQLite-on.

## Források

- [PostgreSQL 18 — Combining Queries](https://www.postgresql.org/docs/18/queries-union.html)
