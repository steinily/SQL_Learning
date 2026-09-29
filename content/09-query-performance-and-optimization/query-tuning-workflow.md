---
schema_version: 1
id: DBKB-PERF-0023
title: Query Tuning Workflow
type: playbook
primary_domain: query-performance
secondary_domains: [governance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-PERF-0003, DBKB-PERF-0022]
related: [DBKB-PERF-0035]
aliases: [query optimization workflow]
search_keywords: [query tuning workflow, plan comparison, performance change]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Reproduce, measure, change, validate, rollback workflowet ad]
---
# Query Tuning Workflow

1. Rögzítsd a workloadot és baseline-t. 2. Gyűjts `EXPLAIN (ANALYZE, BUFFERS)` evidence-et kontrollált környezetben. 3. Változtass egy tényezőt. 4. Mérj representative runokkal. 5. Dokumentáld impactot és rollbacket.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
