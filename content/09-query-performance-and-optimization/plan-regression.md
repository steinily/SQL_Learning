---
schema_version: 1
id: DBKB-PERF-0022
title: Plan Regression
type: troubleshooting
primary_domain: query-performance
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-PERF-0013, DBKB-PERF-0024]
related: [DBKB-PERF-0027]
aliases: [query plan regression]
search_keywords: [plan regression, performance regression, plan change]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Baseline comparison és regression evidence folyamatot ad]
---
# Plan Regression

Plan regression akkor áll fenn, ha ugyanazon workload representative körülmények között romló runtime vagy resource profile-t mutat. Compare-old/new plan, statistics, data distribution, engine version és configuration szükséges; cost change önmagában nem bizonyíték.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
