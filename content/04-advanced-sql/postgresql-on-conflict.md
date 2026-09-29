---
schema_version: 1
id: DBKB-ASQL-0024
title: PostgreSQL ON CONFLICT
type: technology
primary_domain: advanced-sql
secondary_domains: [postgresql, concurrency]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-ASQL-0023]
related: [DBKB-ASQL-0025]
aliases: [PostgreSQL upsert]
search_keywords: [on conflict, excluded, arbiter index, returning]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ASQL-0003]
source_ids: [SRC-000043]
acceptance_criteria:
  - Bemutatja a conflict target, excluded és RETURNING fogalmakat.
  - PostgreSQL 18 scope-ot rögzít.
  - Nem nevezi SQLite executionnek a PostgreSQL syntaxot.
---
# PostgreSQL ON CONFLICT

PostgreSQL `ON CONFLICT` unique/exclusion arbiter alapján választ `DO NOTHING` vagy `DO UPDATE`
actiont. `EXCLUDED` a proposed row, a target alias az existing row hivatkozása. `DO UPDATE`-hez
explicit conflict target szükséges.

```sql
INSERT INTO distributor (did, name)
VALUES (5, 'New Name')
ON CONFLICT (did) DO UPDATE
SET name = EXCLUDED.name
RETURNING did, name;
```

A dokumentált atomic insert-or-update outcome nem szünteti meg a business-level lost-update,
version-check, trigger és side-effect kérdéseket. `WHERE` condition az update-et korlátozhatja; a
locked-but-not-updated row nem feltétlen kerül `RETURNING` outputba.

Ez PostgreSQL 18 source-verified topic. PostgreSQL runtime nincs konfigurálva, ezért nincs execution
evidence.

## Források

- [PostgreSQL 18 — INSERT](https://www.postgresql.org/docs/18/sql-insert.html)
