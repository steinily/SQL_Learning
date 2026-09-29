---
schema_version: 1
id: DBKB-PERF-0034
title: Performance Incident Runbook
type: playbook
primary_domain: query-performance
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PERF-0025, DBKB-PERF-0026]
related: [DBKB-PERF-0035]
aliases: [query performance incident]
search_keywords: [performance incident, slow database, query regression]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Triage, mitigation, evidence capture és follow-up lépéseket ad]
---
# Performance Incident Runbook

Incident flow: scope és impact; active waits/resource saturation; top query fingerprints; recent deploy/statistics/data change; safe mitigation; evidence capture; rollback; post-incident root cause és prevention. Destructive intervention approvalhoz kötött.

## Források
- [PostgreSQL 18 — Monitoring Database Activity](https://www.postgresql.org/docs/18/monitoring.html)
