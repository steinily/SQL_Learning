---
schema_version: 1
id: DBKB-CAP-0003
title: Query Performance Case Study
type: case-study
primary_domain: capstone
secondary_domains: [performance, sql]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-CAP-0002]
related: [DBKB-PERF-0001]
aliases: [query tuning case]
search_keywords: [query performance, plan regression, index, statistics, case study]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Scenario requires baseline, plan evidence, hypothesis, change and regression validation]
---
# Query Performance Case Study

Egy p95 query latency regresszió után készíts baseline-t, query fingerprintet, execution plan/statistics evidence-et és hypothesis matrixot. Hasonlítsd össze index, query rewrite, statistics és workload isolation opciókat.

Elvárt evidence: representative execution output, before/after plan, latency/resource mérés, correctness check, rollback és residual risk. Fiktív benchmarkot ne adj meg; a case instructional scenario marad.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
