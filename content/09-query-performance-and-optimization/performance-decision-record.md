---
schema_version: 1
id: DBKB-PERF-0033
title: Performance Decision Record
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
prerequisites: [DBKB-PERF-0023]
related: [DBKB-IDX-0025]
aliases: [performance ADR]
search_keywords: [performance decision record, query tuning ADR]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Context, evidence, decision, impact, rollback és owner mezőket ad]
---
# Performance Decision Record

Performance decision record tartalmazza a contextet, baseline-t, hypothesis-t, plan evidence-et, választott változtatást, várható és tényleges impactot, rollbacket, owner-t és review date-et.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
