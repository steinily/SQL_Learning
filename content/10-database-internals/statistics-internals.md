---
schema_version: 1
id: DBKB-INT-0022
title: Statistics Internals
type: technology
primary_domain: database-internals
secondary_domains: [performance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0021, DBKB-PERF-0013]
related: [DBKB-IDX-0011]
aliases: [planner statistics internals]
search_keywords: [statistics internals, pg_statistic, histogram, most common values]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Statistics representation és planner estimate kapcsolatát írja le]
---
# Statistics Internals

Planner statistics histogram, most-common-values és distinctness becslésekkel modellezi a predicate distributiont. A belső catalog representation version-sensitive; a tuning claimet plan és data evidence támassza alá.

## Források
- [PostgreSQL 18 — Planner Statistics](https://www.postgresql.org/docs/18/planner-stats.html)
