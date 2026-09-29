---
schema_version: 1
id: DBKB-FND-0035
title: Query and Database Object Fundamentals
type: concept
primary_domain: foundations
secondary_domains: [sql, database-engineering]
levels: [beginner]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-FND-0003, DBKB-FND-0007, DBKB-FND-0023]
related: [DBKB-FND-0011, DBKB-FND-0019, DBKB-FND-0034]
aliases: [query, table, view, index, sequence]
search_keywords: [SELECT, DDL, DML, catalog, function, trigger]
risk: safe
version_sensitive: true
review_cycle: on-major-release
research_packages: [RP-FND-0004]
source_ids: [SRC-000022, SRC-000023]
acceptance_criteria:
  - Meghatározza a query és result alapfogalmát.
  - Áttekinti a fő database object family-ket.
  - Elkülöníti a logical contractot a performance objecttől.
---
# Query and Database Object Fundamentals

A **query** adatot kér vagy relation-szerű resultot képez. PostgreSQL 18-ban a `SELECT` command
specifikál queryt; a table expression base table, join és subquery kombinációja lehet.

```sql
SELECT product_id, product_name
FROM product
WHERE unit_price > 10
ORDER BY product_id;
```

A select list output columnokat, `FROM` input relationt, `WHERE` predicate-et, `ORDER BY`
presentation ordert ad. Result nem feltétlenül stored object.

## Object family-k

- **Table:** stored row/column relation.
- **View:** stored query definition; resultja lekérdezéskor képződik.
- **Materialized view:** stored query result, explicit refresh semanticsal.
- **Index:** access/enforcement structure; nem authoritative duplicate copy.
- **Sequence/identity:** key value generation mechanizmus.
- **Constraint:** state rule.
- **Function/procedure:** reusable executable database code.
- **Trigger:** eventhez kötött implicit execution; rejtett side effect kockázata van.
- **Schema/catalog:** namespace és metadata organization.

Vendor object set és név eltérhet. PostgreSQL glossary külön global és database-local objecteket
is megkülönböztet.

## DDL, DML és transaction

DDL objectet definiál vagy módosít; DML row state-et kezel; query resultot olvas. A kategória
határa és transaction behavior vendorfüggő. Production change előtt lock, rewrite, dependency
és rollback hatást kell ellenőrizni.

## Canonical source

Index, cache és materialized projection derived state. Az authoritative table/domain ownership
legyen explicit, és derived object legyen rebuildelhető vagy reconciliationnel ellenőrizhető.

## Források

- [PostgreSQL 18 — Queries Overview](https://www.postgresql.org/docs/18/queries-overview.html)
- [PostgreSQL 18 — Glossary](https://www.postgresql.org/docs/18/glossary.html)
