---
schema_version: 1
id: DBKB-ISQL-0025
title: Temporary Objects
type: concept
primary_domain: intermediate-sql
secondary_domains: [operations]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-SQL-0022]
related: [DBKB-ISQL-0020, DBKB-ISQL-0024]
aliases: [temporary table, temp table]
search_keywords: [temp table, session scope, on commit, intermediate data]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ISQL-0003]
source_ids: [SRC-000038]
acceptance_criteria:
  - Elkülöníti a temporary objectet a CTE-től és view-tól.
  - Vendor szerint scope-olja a lifecycle állításokat.
  - Ephemeral környezetben futtatott temp-table példát ad.
---
# Temporary Objects

Temporary table sessionhez vagy transactionhöz kötött intermediate adatot tárolhat. A CTE-től
eltérően több statement használhatja és indexelhető/statistics-szal kezelhető lehet; pontos feature
setje enginefüggő.

PostgreSQL 18-ban a temporary table special schema-ba kerül, session végén automatikusan eltűnik, és
`ON COMMIT` option módosíthatja transaction-end behavior-jét. Ezt nem általánosítjuk SQL Server
`#temp`, MySQL vagy SQLite semanticsre.

```sql
CREATE TEMPORARY TABLE selected_customer (
  customer_id INTEGER PRIMARY KEY
);
```

Lifecycle, connection pooling, name shadowing, transaction rollback, statistics és cleanup mind
review tárgy. Poololt connectionnél a session tovább élhet az application requestnél, ezért explicit
drop vagy hygiene policy kellhet.

A `SQL-ISQL-0025` SQLite connection scope-jában hoz létre temporary table-t, tölti és olvassa. Ez
csak a deklarált environment execution evidence-e.

## Források

- [PostgreSQL 18 — CREATE TABLE](https://www.postgresql.org/docs/18/sql-createtable.html)
