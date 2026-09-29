---
schema_version: 1
id: DBKB-ISQL-0019
title: COALESCE and NULLIF
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
scope: portable-sql
prerequisites: [DBKB-FND-0017, DBKB-ISQL-0018]
related: [DBKB-ISQL-0026]
aliases: [null handling expression]
search_keywords: [coalesce, nullif, default, divide by zero]
risk: caution
version_sensitive: false
review_cycle: 24m
research_packages: [RP-ISQL-0003, RP-ISQL-0004]
source_ids: [SRC-000035]
acceptance_criteria:
  - Meghatározza a COALESCE és NULLIF semanticsét.
  - Elkülöníti a presentation defaultot a stored meaningtől.
  - Futtatható safe-ratio példát ad.
---
# COALESCE and NULLIF

`COALESCE(a, b, ...)` az első nem-`NULL` argumentumot adja. `NULLIF(a, b)` `NULL`-t ad, ha a két
argumentum equal, különben `a`-t. Gyakori safe-ratio forma: `numerator / NULLIF(denominator, 0)`.

```sql
SELECT revenue / NULLIF(units, 0) AS revenue_per_unit
FROM metric;
```

Ez zero denominatornál `NULL`-t ad, de nem dönt arról, hogy a business metricnek zero, missing vagy
error kell-e lennie. A `COALESCE(..., 0)` csak akkor helyes, ha a consumer contract valóban azonosnak
tekinti a hiányt és a nullát.

Argumentumok common type resolutiont igényelnek. Sentinel value használata `COALESCE`-ben equalityhez
veszélyes, ha a sentinel a domainben előfordulhat. Index és predicate behavior enginefüggő; plan
evidence nélkül ne tegyél performance ígéretet.

A `SQL-ISQL-0019` normál és zero denominator esetet ellenőriz SQLite-on.

## Források

- [PostgreSQL 18 — Conditional Expressions](https://www.postgresql.org/docs/18/functions-conditional.html)
