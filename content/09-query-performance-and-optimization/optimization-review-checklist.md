---
schema_version: 1
id: DBKB-PERF-0035
title: Optimization Review Checklist
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
prerequisites: [DBKB-PERF-0033, DBKB-PERF-0034]
related: [DBKB-PERF-0023]
aliases: [query optimization checklist]
search_keywords: [optimization review, performance checklist]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Workload, plan, correctness, resource impact, rollback és ownership review]
---
# Optimization Review Checklist

Review előtt legyen representative workload, baseline, actual plan, correctness check, resource impact, concurrency assessment, rollback és owner. Approval nélkül production plan forcing vagy configuration change nem tekinthető késznek.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
