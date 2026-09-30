---
schema_version: 1
id: DBKB-CAP-0075
title: Learning Path Performance
type: learning-path
primary_domain: capstone
secondary_domains: [performance, observability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0074]
related: [DBKB-CAP-0025, DBKB-CAP-0054]
aliases: [performance path]
search_keywords: [performance learning path, plan, index, wait, baseline, regression]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Ordered performance path with baseline, plan, index, workload and regression evidence]
---
# Learning Path Performance

Sorrend: query semantics → baseline/metrics → plan/statistics → index/design → concurrency/waits → workload isolation/cost → regression test → performance case/reference.

Exit criteria: reproducible measurement, correctness preserved, resource/cost impact known, rollback and limitation documented.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
