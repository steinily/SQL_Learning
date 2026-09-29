---
schema_version: 1
id: DBKB-ASQL-0003
title: Window Partitioning and Ordering
type: concept
primary_domain: advanced-sql
secondary_domains: [analytics]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-ASQL-0002, DBKB-SQL-0008]
related: [DBKB-ASQL-0004, DBKB-ASQL-0009]
aliases: [window specification]
search_keywords: [partition by, window order, peer, tie breaker]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ASQL-0001]
source_ids: [SRC-000039, SRC-000040]
acceptance_criteria:
  - Elkülöníti a window orderinget a final orderingtől.
  - Definiálja a peer groupot és deterministic tie-breakert.
  - Futtatható partition-order példát ad.
---
# Window Partitioning and Ordering

`PARTITION BY` minden partitionben újraindítja a window számítást. Window `ORDER BY` a partitionön
belüli sequence-et és peer groupot definiálja, de nem garantálja a végső result presentation ordert;
ahhoz outer `ORDER BY` kell.

```sql
ROW_NUMBER() OVER (
  PARTITION BY department_id
  ORDER BY salary DESC, employee_id
)
```

Azonos window sort key-jű sorok peers. Ranking functionök peer behavior-ja definiált, de
`ROW_NUMBER` stabil kiosztásához unique tie-breaker szükséges. Temporal vagy text key-nél timezone és
collation is a contract része.

Több function azonos specificationnel named `WINDOW` clause-t használhat, ha a dialect támogatja;
ez csökkenti a driftet. A final output ordert akkor is külön add meg.

A `SQL-ASQL-0003` két departmentben külön sequence-et és explicit final ordert ellenőriz SQLite-on.

## Források

- [PostgreSQL 18 Tutorial — Window Functions](https://www.postgresql.org/docs/18/tutorial-window.html)
