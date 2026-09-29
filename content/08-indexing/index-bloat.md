---
schema_version: 1
id: DBKB-IDX-0013
title: Index Bloat
type: troubleshooting
primary_domain: indexing
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-IDX-0012]
related: [DBKB-IDX-0022]
aliases: [index fragmentation, wasted index space]
search_keywords: [index bloat, dead tuples, reindex]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Bloat diagnosist mérési és remediation caveat-tel adja]
---
# Index Bloat

Index bloatnál a fizikai indexméret és a hasznos index-tartalom aránya romolhat, ami I/O-t és cache pressure-t növel. Diagnózis legyen mérés-alapú; vak `REINDEX` productionben nem elfogadható.

## Források
- [PostgreSQL 18 — Routine Vacuuming](https://www.postgresql.org/docs/18/routine-vacuuming.html)
