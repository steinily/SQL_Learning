---
schema_version: 1
id: DBKB-OPS-0020
title: Database Operations Exercise
type: exercise
primary_domain: database-operations
secondary_domains: [validation]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OPS-0015, DBKB-OPS-0018]
related: []
aliases: [DBA operations exercise]
search_keywords: [operations exercise, runbook rehearsal, restore drill]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OPS-0001]
source_ids: [SRC-000049]
acceptance_criteria: [Exercise defines evidence without claiming unexecuted results]
---
# Database Operations Exercise

Készíts versioned runbookot egy staging database promotion és restore drill számára. Rögzíts precheckeket, approvalt, backup artifactot, restore verificationt, health check outputot és rollback döntést; execution-verified státusz csak tényleges futtatás után adható.

## Források
- [PostgreSQL — Backup and Restore](https://www.postgresql.org/docs/current/backup.html)
