---
schema_version: 1
id: DBKB-ASQL-0001
title: Advanced SQL Overview
type: overview
primary_domain: advanced-sql
secondary_domains: [intermediate-sql, analytics]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-ISQL-0001, DBKB-ISQL-0022]
related: [DBKB-ASQL-0002, DBKB-ASQL-0014, DBKB-ASQL-0023]
aliases: [advanced query patterns]
search_keywords: [window function, grouping sets, lateral, json, merge]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ASQL-0001, RP-ASQL-0002, RP-ASQL-0003]
source_ids: [SRC-000039, SRC-000036, SRC-000041, SRC-000043, SRC-000044]
acceptance_criteria:
  - Rendszerezi az M04 analytical relational semi-structured és modification mintáit.
  - Minden engine-sensitive feature-höz dialect scope-ot követel.
  - Correctness concurrency és execution evidence szempontokat ad.
---
# Advanced SQL Overview

Az advanced SQL olyan műveleteket kapcsol össze, amelyeknél a rövid syntax mögött összetett grain,
ordering, frame, type és concurrency contract áll. A modul négy területet fed le: window analytics;
advanced grouping és correlation; JSON/temporal/dynamic SQL; valamint upsert, `MERGE` és bulk DML.

## Correctness sorrend

1. Rögzítsd az input és output grain-t, valamint a duplicate policyt.
2. Tedd explicit-té a partition, ordering és frame határokat.
3. Nevezd meg a dialectet és verziót minden non-portable feature-nél.
4. DML-nél bizonyítsd a source uniquenesset, conflict identityt és transaction boundaryt.
5. Csak ezután értékeld a physical plant és performance-ot.

Window `ORDER BY` nem presentation order; JSON string nem automatikusan typed value; temporal
arithmetic timezone nélkül nem teljes contract; `MERGE` pedig nem általános concurrency garancia.

Az executable példák SQLite-on csak a támogatott, deklarált subsetet igazolják. PostgreSQL 18
`ON CONFLICT`, `MERGE`, JSON és temporal állításai official dokumentációból source-verifiedek, amíg
PostgreSQL runtime nem áll rendelkezésre.

## Források

- [PostgreSQL 18 — Window Functions](https://www.postgresql.org/docs/18/functions-window.html)
- [PostgreSQL 18 — INSERT](https://www.postgresql.org/docs/18/sql-insert.html)
- [PostgreSQL 18 — MERGE](https://www.postgresql.org/docs/18/sql-merge.html)
