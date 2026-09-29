---
schema_version: 1
id: DBKB-ISQL-0017
title: Set Operation Compatibility
type: concept
primary_domain: intermediate-sql
secondary_domains: [data-integration]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-ISQL-0015, DBKB-SQL-0011]
related: [DBKB-ISQL-0016]
aliases: [union compatibility]
search_keywords: [column count, type compatibility, column order, coercion]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ISQL-0002]
source_ids: [SRC-000034]
acceptance_criteria:
  - Megköveteli az azonos column countot és positional type compatibilityt.
  - Tárgyalja a name és semantic alignmentet.
  - Futtatható explicit-CAST példát ad.
---
# Set Operation Compatibility

Set operation inputjai **union-compatible** shape-et igényelnek: azonos számú column és positionönként
compatible type. A kompatibilis syntax még nem jelent semantic kompatibilitást; ugyanabba a positionbe
ugyanazt a business attributumot és unitot kell tenni.

```sql
SELECT customer_id, CAST(amount AS DECIMAL(12,2)) AS amount
FROM current_order
UNION ALL
SELECT customer_id, CAST(amount AS DECIMAL(12,2))
FROM archived_order;
```

Explicit cast dokumentálhatja a common target type-ot, de range, precision és invalid-input risket is
bevezet. Output columnnév és metadata gyakran az első inputból ered; consumer contractnál ezt stabilan
nevezd meg.

Text collation, temporal timezone, character encoding és numeric scale semantic mismatch maradhat
akkor is, ha az engine elfogadja a statementet. Integration előtt profiling és boundary-value test
kell.

A `SQL-ISQL-0017` integerként tárolt és textből explicit castolt id-ket kombinál SQLite-on, exact
ordered outputtal. Más engine type-resolution szabályát ez nem igazolja.

## Források

- [PostgreSQL 18 — Combining Queries](https://www.postgresql.org/docs/18/queries-union.html)
