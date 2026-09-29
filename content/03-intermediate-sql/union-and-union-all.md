---
schema_version: 1
id: DBKB-ISQL-0015
title: UNION and UNION ALL
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
scope: portable-sql
prerequisites: [DBKB-SQL-0012]
related: [DBKB-ISQL-0016, DBKB-ISQL-0017]
aliases: [set union]
search_keywords: [union, union all, append, duplicate elimination]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-ISQL-0002]
source_ids: [SRC-000034]
acceptance_criteria:
  - Elkülöníti a duplicate-preserving és eliminating formát.
  - Tisztázza az ordering és compatibility contractot.
  - Futtatható összehasonlító példát ad.
---
# UNION and UNION ALL

`UNION ALL` az input queryk sorait duplicate megőrzésével kombinálja. `UNION` ugyanebből duplicate
result row-kat távolít el. Ha a source-ok diszjunktak vagy a duplicate meaningful, `UNION ALL` fejezi
ki a helyes intentet; ne válassz `UNION`-t „biztonságból”.

```sql
SELECT code FROM source_a
UNION ALL
SELECT code FROM source_b;
```

Az inputoknak azonos column counttal és corresponding compatible type-okkal kell rendelkezniük. Az
output columnnevek jellemzően az első queryből származnak, de a type resolution engine-specifikus
részleteit ellenőrizni kell.

Az input queryk fizikai visszaadási sorrendje nem lesz output contract. Egyetlen, a teljes compound
queryre vonatkozó `ORDER BY` kell. Inputonkénti limit/order zárójelezése és támogatása dialectfüggő.

A `SQL-ISQL-0015` `UNION ALL` és `UNION` count különbségét egy eredménysorban validálja SQLite-on.

## Források

- [PostgreSQL 18 — Combining Queries](https://www.postgresql.org/docs/18/queries-union.html)
