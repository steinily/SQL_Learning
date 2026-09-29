---
schema_version: 1
id: DBKB-ISQL-0008
title: Anti Joins
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
prerequisites: [DBKB-ISQL-0007, DBKB-FND-0017]
related: [DBKB-ISQL-0014, DBKB-ISQL-0028]
aliases: [missing-match join]
search_keywords: [anti join, not exists, unmatched, missing relationship]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ISQL-0002]
source_ids: [SRC-000033]
acceptance_criteria:
  - Meghatározza az anti join missing-match semanticsét.
  - NULL-safe alapmintaként mutatja be a NOT EXISTS formát.
  - Futtatható anti-join példát ad.
---
# Anti Joins

Logical anti join azokat a bal oldali sorokat adja, amelyekhez nincs matching jobb oldali sor.
Portable és null-tudatos alapminta a correlated `NOT EXISTS`.

```sql
SELECT c.customer_id
FROM customer AS c
WHERE NOT EXISTS (
  SELECT 1 FROM sales_order AS o
  WHERE o.customer_id = c.customer_id
);
```

A `LEFT JOIN ... WHERE right_key IS NULL` is használható, ha a tesztelt jobb oldali key garantáltan
non-null, és a join predicate pontos. Nullable business column tesztelése false unmatched jelzést
adhat. `NOT IN` nullable input mellett `UNKNOWN` eredményt okozhat, ezért nem automatikus helyettesítő.

Anti join tipikus data-quality kérdés: orphan candidate, hiányzó feldolgozás vagy még nem teljesített
követelmény. Időbeli feltételnél az ablakot az inner subqueryben kell megadni, különben más „nincs”
kérdést teszünk fel.

A `SQL-ISQL-0008` három customerből az egyetlen order nélküli sort validálja SQLite-on.

## Források

- [PostgreSQL 18 — Subquery Expressions](https://www.postgresql.org/docs/18/functions-subquery.html)
