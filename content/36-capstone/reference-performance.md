---
schema_version: 1
id: DBKB-CAP-0054
title: Reference Performance
type: reference
primary_domain: capstone
secondary_domains: [performance, observability]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0053]
related: [DBKB-PERF-0001]
aliases: [performance checklist]
search_keywords: [performance reference, latency, throughput, plan, wait, baseline]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Performance diagnosis and change validation checklist is provided]
---
# Reference Performance

Baseline workload/volume/version; query fingerprint; p50/p95/p99; throughput/error; plan/stats; CPU/IO/memory; lock/wait; cache; replication; change correlation; correctness; rollback; cost.

Performance claim csak same input, environment and measurement method mellett összehasonlítható. Tuning outputot és limitations-t őrizd meg, ne csak egy elapsed time értéket.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
