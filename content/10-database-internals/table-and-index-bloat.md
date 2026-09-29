---
schema_version: 1
id: DBKB-INT-0015
title: Table and Index Bloat
type: troubleshooting
primary_domain: database-internals
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0011, DBKB-INT-0014]
related: [DBKB-IDX-0013]
aliases: [relation bloat]
search_keywords: [table bloat, index bloat, dead tuples, vacuum]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Bloat mérési és remediation döntést workload evidence alapján ad]
---
# Table and Index Bloat

Bloat a relation vagy index fizikailag nagyobb méretét jelenti a hasznos élő tartalomhoz képest. Diagnózisnál dead tuples, vacuum progress, table/index size és workload együtt vizsgálandó; rebuild csak kontrollált impact tervvel.

## Források
- [PostgreSQL 18 — Routine Vacuuming](https://www.postgresql.org/docs/18/routine-vacuuming.html)
