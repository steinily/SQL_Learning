---
schema_version: 1
id: DBKB-ISQL-0018
title: CASE Expressions
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
scope: portable-sql
prerequisites: [DBKB-SQL-0010]
related: [DBKB-ISQL-0003, DBKB-ISQL-0019]
aliases: [searched case, simple case]
search_keywords: [case, when, then, else, conditional expression]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-ISQL-0003]
source_ids: [SRC-000035]
acceptance_criteria:
  - Bemutatja a searched és simple CASE formát.
  - Tárgyalja az ELSE NULL és type resolution hatását.
  - Futtatható classification példát ad.
---
# CASE Expressions

A `CASE` scalar conditional expression. A searched form egymás után vizsgál predicate-eket; az első
`TRUE` branch eredménye lesz a value. A simple form egy expressiont hasonlít több value-hoz.

```sql
CASE
  WHEN amount >= 1000 THEN 'large'
  WHEN amount >= 100 THEN 'medium'
  ELSE 'small'
END
```

A branch sorrend jelentéssel bír: a szélesebb predicate túl korán elérhetetlenné tehet későbbi ágat.
`ELSE` nélkül az unmatched eredmény `NULL`. Minden result branchnek common compatible type-ra kell
feloldódnia; implicit conversion adatvesztést vagy error-t okozhat.

`CASE` használható select listben, orderingben és aggregate inputként, de nem procedural control-flow
statement. Ne támaszkodj side effectre vagy undocumented expression-evaluation rendre.

A `SQL-ISQL-0018` boundary értékekkel ellenőrzi a három classification branchet SQLite-on.

## Források

- [PostgreSQL 18 — Conditional Expressions](https://www.postgresql.org/docs/18/functions-conditional.html)
