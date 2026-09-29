---
schema_version: 1
id: DBKB-ISQL-0012
title: Correlated Subqueries
type: concept
primary_domain: intermediate-sql
secondary_domains: [query-performance]
levels: [intermediate, advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-ISQL-0009]
related: [DBKB-ISQL-0010, DBKB-ISQL-0013]
aliases: [correlated nested query]
search_keywords: [correlation, outer reference, per-row context, decorrelation]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ISQL-0002]
source_ids: [SRC-000033]
acceptance_criteria:
  - Megmagyarázza az outer reference scope-ját.
  - Nem tesz bizonyítatlan evaluation-count állítást.
  - Futtatható correlated aggregate példát ad.
---
# Correlated Subqueries

Correlated subquery a külső query block egy vagy több columnjára hivatkozik. Logical jelentése a
külső sor kontextusához kötött; ebből nem következik, hogy az engine szó szerint soronként egyszer
futtatja. Decorrelation és más rewrite optimizerfüggő.

```sql
SELECT p.product_id
FROM product AS p
WHERE p.unit_price > (
  SELECT AVG(p2.unit_price)
  FROM product AS p2
  WHERE p2.category_id = p.category_id
);
```

Alias qualification nélkül könnyű véletlenül belső columnra bindolni vagy mindig-igaz predicate-et
írni. A scope boundaryt és aliasokat review során explicit kövesd.

Rewrite join plusz pre-aggregation formára akkor korrekt, ha megmarad az empty group, `NULL`,
duplicate és cardinality behavior. Performance választáshoz mindkét formát reprezentatív adaton,
azonos parameterrel és execution plannel mérd.

A `SQL-ISQL-0012` category average feletti productokat ellenőriz SQLite-on.

## Források

- [PostgreSQL 18 — Subquery Expressions](https://www.postgresql.org/docs/18/functions-subquery.html)
