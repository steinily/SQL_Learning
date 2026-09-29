---
schema_version: 1
id: DBKB-ISQL-0001
title: Intermediate SQL Overview
type: overview
primary_domain: intermediate-sql
secondary_domains: [sql-fundamentals, data-modeling]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-SQL-0016, DBKB-SQL-0014]
related: [DBKB-ISQL-0009, DBKB-ISQL-0020, DBKB-ISQL-0028]
aliases: [intermediate query patterns]
search_keywords: [subquery, cte, set operation, semi join, recursive query]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ISQL-0001, RP-ISQL-0002, RP-ISQL-0003, RP-ISQL-0004]
source_ids: [SRC-000032, SRC-000033, SRC-000034, SRC-000036]
acceptance_criteria:
  - Összeköti a grain, existence, set és reusable-query mintákat.
  - Meghatározza a correctness-first választási elveket.
  - Elkülöníti a logical semanticset a physical optimizationtől.
---
# Intermediate SQL Overview

Az intermediate SQL nem hosszabb syntaxok gyűjteménye, hanem pontosabb **grain**, existence és set
gondolkodás. Ugyanazt a business kérdést join, subquery, set operation vagy CTE is kifejezheti, de
cardinality, `NULL` és duplicate semanticsük eltérhet.

## Választási térkép

- Kapcsolt columnokra van szükség: megfelelő logical join.
- Csak azt kérdezed, van-e match: `EXISTS` alapú semi join.
- Match hiányát keresed: `NOT EXISTS` alapú anti join, explicit nullability review-val.
- Két result halmazt kombinálsz: `UNION`, `INTERSECT` vagy `EXCEPT`.
- Egy statementet olvasható részekre bontasz: derived table vagy CTE.
- Reusable schema interface kell: view; lifecycle-lal rendelkező köztes adat kell: temporary object.
- „Minden követelményt teljesít” kérdés: relational division.

Minden mintánál előbb írd le az input és output grain-t, majd a duplicate és `NULL` contractot. Csak
ezután vizsgáld az execution plant. A logical forma nem garantál konkrét join algorithmet,
materializationt vagy evaluation countot.

Az M03 portable példái ephemeral SQLite környezetben futnak. PostgreSQL 18-ra vonatkozó CTE,
subquery és set-operation állítások official dokumentációval source-verifiedek; más engine-re külön
execution evidence kell.

## Források

- [PostgreSQL 18 — WITH Queries](https://www.postgresql.org/docs/18/queries-with.html)
- [PostgreSQL 18 — Subquery Expressions](https://www.postgresql.org/docs/18/functions-subquery.html)
- [PostgreSQL 18 — Combining Queries](https://www.postgresql.org/docs/18/queries-union.html)
