---
schema_version: 1
id: DBKB-ISQL-0026
title: NULL-Safe Query Patterns
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
prerequisites: [DBKB-FND-0017, DBKB-ISQL-0019]
related: [DBKB-ISQL-0014, DBKB-ISQL-0027]
aliases: [null-aware SQL]
search_keywords: ["null", is null, coalesce, not exists, three-valued logic]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ISQL-0004]
source_ids: [SRC-000033, SRC-000035]
acceptance_criteria:
  - Query constructonként kezeli a NULL semanticset.
  - Elutasítja a constraint nélküli sentinel substitutiont.
  - Futtatható null-aware equality mintát ad.
---
# NULL-Safe Query Patterns

„NULL-safe” nem egyetlen syntax, hanem a missing/unknown business jelentés explicit kezelése minden
constructban. Nullnesshez `IS NULL`; anti joinhoz nullable right side esetén `NOT EXISTS`; default
presentationhöz csak indokolt `COALESCE` használható.

Portable null-aware equality minta:

```sql
(a = b) OR (a IS NULL AND b IS NULL)
```

Vendorok kínálhatnak `IS [NOT] DISTINCT FROM` vagy null-safe equality operatort, de támogatásuk és
syntaxuk eltér. `COALESCE(a, sentinel) = COALESCE(b, sentinel)` csak akkor helyes, ha constraint
bizonyítja, hogy sentinel egyik domainben sem fordulhat elő.

Concatenation, arithmetic, aggregate, unique constraint és ordering `NULL` behavior-ját külön kell
ellenőrizni. Egyetlen általános „NULL rule” nem helyettesíti a construct truth table-jét.

A `SQL-ISQL-0026` nullable párokon ellenőrzi az explicit equality mintát SQLite-on.

## Források

- [PostgreSQL 18 — Subquery Expressions](https://www.postgresql.org/docs/18/functions-subquery.html)
- [PostgreSQL 18 — Conditional Expressions](https://www.postgresql.org/docs/18/functions-conditional.html)
