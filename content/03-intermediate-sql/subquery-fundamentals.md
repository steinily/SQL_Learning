---
schema_version: 1
id: DBKB-ISQL-0009
title: Subquery Fundamentals
type: concept
primary_domain: intermediate-sql
secondary_domains: [sql-fundamentals]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-SQL-0003, DBKB-SQL-0004]
related: [DBKB-ISQL-0010, DBKB-ISQL-0011, DBKB-ISQL-0012]
aliases: [nested query]
search_keywords: [subquery, scalar, correlated, derived table, query block]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ISQL-0002]
source_ids: [SRC-000033, SRC-000036]
acceptance_criteria:
  - Context szerint rendszerezi a subquery formákat.
  - Megköveteli a cardinality és correlation vizsgálatát.
  - Futtatható uncorrelated subquery példát ad.
---
# Subquery Fundamentals

Subquery egy másik SQL statementbe ágyazott query block. Contextje határozza meg a contractját:
scalar helyzetben legfeljebb egy érték, `IN` mellett egy column több sora, `EXISTS` mellett pedig csak
a row existence számít. `FROM`-ban table-shaped derived table lesz.

Uncorrelated subquery nem hivatkozik külső query columnra. Correlated subquery igen; ezért logical
értelemben a külső sor kontextusában értékelhető, de a physical evaluation countot az optimizer
határozza meg.

```sql
SELECT product_id
FROM product
WHERE unit_price > (SELECT AVG(unit_price) FROM product);
```

Review során bizonyítsd a scalar cardinalityt, a returned column countot, a type compatibilityt és a
`NULL` behavior-t. `ORDER BY` row limit nélkül subqueryben gyakran nem ad meaningful contractot, és a
külső result sorrendjét nem garantálja.

A `SQL-ISQL-0009` az átlagár feletti terméket exact eredménnyel ellenőrzi SQLite-on.

## Források

- [PostgreSQL 18 — Subquery Expressions](https://www.postgresql.org/docs/18/functions-subquery.html)
- [PostgreSQL 18 — Table Expressions](https://www.postgresql.org/docs/18/queries-table-expressions.html)
