---
schema_version: 1
id: DBKB-ISQL-0028
title: Relational Division
type: concept
primary_domain: intermediate-sql
secondary_domains: [data-modeling]
levels: [intermediate, advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: portable-sql
prerequisites: [DBKB-ISQL-0008, DBKB-ISQL-0003]
related: [DBKB-ISQL-0013, DBKB-ISQL-0027]
aliases: [for-all query]
search_keywords: [relational division, for all, double not exists, required set]
risk: caution
version_sensitive: false
review_cycle: 24m
research_packages: [RP-ISQL-0004]
source_ids: [SRC-000033]
acceptance_criteria:
  - Minden-követelmény kérdésként definiálja a relational divisiont.
  - Bemutatja a double-NOT-EXISTS és count-based formát.
  - Futtatható positive missing és empty-required-set esetet ad.
---
# Relational Division

Relational division „mely entity teljesít **minden** required conditiont?” kérdés. Portable,
duplicate-insensitive alapminta a double `NOT EXISTS`: nincs olyan requirement, amelyhez nincs match.

```sql
SELECT c.customer_id
FROM customer AS c
WHERE NOT EXISTS (
  SELECT 1 FROM required_product AS r
  WHERE NOT EXISTS (
    SELECT 1 FROM purchase AS p
    WHERE p.customer_id = c.customer_id
      AND p.product_id = r.product_id
  )
);
```

Ha a required set empty, a logikai „minden elemre” állítás vacuously true, tehát minden candidate
megfelel. Ha ez üzletileg nem kívánt, adj külön `EXISTS(required_set)` guardot.

Count-based alternatíva distinct matched requirement countot hasonlít total requirement counthoz.
Ott duplicate, nullable key és unauthorized extra match külön kockázat. A double-anti-join forma
közvetlenül fejezi ki a hiányzó requirement keresését.

A `SQL-ISQL-0028` két required product mellett egy complete és egy incomplete customert ellenőriz
SQLite-on; a fixture duplicate purchase-t is tartalmaz, amely nem változtatja az existence eredményt.

## Források

- [PostgreSQL 18 — Subquery Expressions](https://www.postgresql.org/docs/18/functions-subquery.html)
