---
schema_version: 1
id: DBKB-PERF-0007
title: Index Scans
type: concept
primary_domain: query-performance
secondary_domains: [postgresql]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PERF-0004, DBKB-IDX-0003]
related: [DBKB-PERF-0006, DBKB-PERF-0008]
aliases: [index scan]
search_keywords: [index scan, index condition, heap fetch]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Index Scan és Index Only Scan különbségét plan output alapján adja]
---
# Index Scans

Index scan indexből választja ki a tuple locatorokat, majd szükség esetén heapet olvas. Index-only scan esetén a visibility és coverage feltételei továbbiak; actual plan nélkül ne állíts teljes heap-elkerülést.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
