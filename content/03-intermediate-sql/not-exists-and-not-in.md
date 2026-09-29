---
schema_version: 1
id: DBKB-ISQL-0014
title: NOT EXISTS and NOT IN
type: comparison
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
prerequisites: [DBKB-ISQL-0013, DBKB-FND-0017]
related: [DBKB-ISQL-0008, DBKB-ISQL-0026]
aliases: [not in null trap]
search_keywords: [not exists, not in, "null", anti join, unknown]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ISQL-0002, RP-ISQL-0004]
source_ids: [SRC-000033]
acceptance_criteria:
  - Truth-table szinten összehasonlítja a két formát.
  - Bemutatja a nullable NOT IN veszélyét.
  - Futtatható ellenpéldát ad.
---
# NOT EXISTS and NOT IN

`NOT EXISTS` azt állítja, hogy nincs matching row. `value NOT IN (subquery)` azt, hogy a value egyik
returned értékkel sem equal. Non-null domainben gyakran azonos eredményt adnak, nullable inputnál nem.

Ha a `NOT IN` jobb oldalán nincs match, de van `NULL`, a comparison eredménye `UNKNOWN` lehet, ezért
a `WHERE` egyetlen sort sem tart meg. `NOT EXISTS` correlated equalityvel nem tesz globális
„ismeretlen” állítást egy unrelated null row miatt.

```sql
SELECT c.customer_id
FROM customer AS c
WHERE NOT EXISTS (
  SELECT 1 FROM sales_order AS o
  WHERE o.customer_id = c.customer_id
);
```

`NOT IN` csak akkor választható biztonságosan, ha mindkét oldal nullability contractja bizonyított,
vagy a null-kezelés explicit és üzletileg helyes. A puszta `WHERE key IS NOT NULL` hozzáadása nem
feltétlen kezeli a bal oldali `NULL` business jelentését.

A `SQL-ISQL-0014` ugyanazon fixture-en egymás mellett mutatja a `NOT EXISTS` helyes eredményét és a
nullable `NOT IN` empty eredményét.

## Források

- [PostgreSQL 18 — Subquery Expressions](https://www.postgresql.org/docs/18/functions-subquery.html)
