---
schema_version: 1
id: DBKB-INT-0016
title: WAL Archiving
type: technology
primary_domain: database-internals
secondary_domains: [backup-recovery]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0005]
related: [DBKB-INT-0017, DBKB-INT-0018]
aliases: [continuous archiving]
search_keywords: [WAL archiving, archive_command, point in time recovery]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [WAL archive, retention és restore verification kapcsolatát leírja]
---
# WAL Archiving

WAL archiving a log segmenteket külön recovery célra megőrzi, lehetővé téve point-in-time recovery-t megfelelő base backup mellett. Archive success, lag, retention és restore test nélkül a backup claim nem bizonyított.

## Források
- [PostgreSQL 18 — Continuous Archiving](https://www.postgresql.org/docs/18/continuous-archiving.html)
