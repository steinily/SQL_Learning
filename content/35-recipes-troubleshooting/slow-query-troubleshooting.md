---
schema_version: 1
id: DBKB-REC-0027
title: Slow Query Troubleshooting
type: troubleshooting
primary_domain: recipes
secondary_domains: [performance, sql]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-REC-0025]
related: [DBKB-PERF-0001]
aliases: [query performance runbook]
search_keywords: [slow query, execution plan, scan, cardinality, regression]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Plan, statistics, locks, resource and remediation evidence are mapped]
---
# Slow Query Troubleshooting

Capture query fingerprint, parameters shape, duration percentile, rows, plan, stats freshness, wait/resource profile és recent change. Compare representative baseline against current plan; ne fixáld index vagy hint hozzáadásával evidence nélkül.

Containment lehet timeout, rate limit, workload isolation vagy rollback; fix után mérd latency, CPU/IO, lock impact és result correctness. Plan improvementet actual execution outputtal dokumentáld.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
