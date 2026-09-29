---
schema_version: 1
id: DBKB-ISQL-0027
title: Duplicate Handling
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
prerequisites: [DBKB-SQL-0012, DBKB-FND-0019]
related: [DBKB-ISQL-0015, DBKB-ISQL-0016]
aliases: [deduplication]
search_keywords: [duplicate, distinct, union, grain, survivor rule]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ISQL-0004]
source_ids: [SRC-000034]
acceptance_criteria:
  - Megkülönbözteti a physical duplicate-ot a business duplicate-tól.
  - Deterministic survivor rule-t követel adatjavításnál.
  - Futtatható duplicate profiling példát ad.
---
# Duplicate Handling

Duplicate csak deklarált grain és business identity mellett értelmezhető. Két teljesen azonos result
row physical duplicate; két eltérő record ugyanazzal a natural key-jel business duplicate lehet.

`DISTINCT` és `UNION` result-level duplicate eliminationt végez, de nem választ canonical survivor
recordot. Adatjavításnál deterministic rule kell: például legfrissebb trusted source, explicit source
priority és stable tie-breaker. Ezt auditálhatóan dokumentáld.

Első lépés a profiling:

```sql
SELECT business_key, COUNT(*) AS occurrences
FROM source_record
GROUP BY business_key
HAVING COUNT(*) > 1;
```

Join után megjelenő ismétlés lehet helyes one-to-many cardinality, nem data defect. `DISTINCT` hozzáadása
előtt bizonyítsd a relationshipet. Delete-based deduplication destructive migration: backup,
quarantine, foreign-key impact és rollback plan szükséges.

A `SQL-ISQL-0027` exact duplicate groupokat és occurrence countot ellenőriz SQLite-on.

## Források

- [PostgreSQL 18 — Combining Queries](https://www.postgresql.org/docs/18/queries-union.html)
