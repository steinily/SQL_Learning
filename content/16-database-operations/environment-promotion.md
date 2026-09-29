---
schema_version: 1
id: DBKB-OPS-0018
title: Environment Promotion
type: playbook
primary_domain: database-operations
secondary_domains: [deployment]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OPS-0014]
related: []
aliases: [database promotion]
search_keywords: [dev test staging production, promotion gate, drift]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OPS-0001]
source_ids: [SRC-000049]
acceptance_criteria: [Promotion gates, drift and evidence are defined]
---
# Environment Promotion

Promotion során ugyanazt a versioned artifactot mozgasd environment-ek között, de külön kezeld a secrets, capacity és data policy eltéréseit. Gate legyen schema validation, migration test, smoke test, rollback readiness és approval; manual drift-et rögzíteni kell.

## Források
- [PostgreSQL — Server Administration](https://www.postgresql.org/docs/current/admin.html)
