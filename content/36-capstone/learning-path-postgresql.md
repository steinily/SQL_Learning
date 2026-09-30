---
schema_version: 1
id: DBKB-CAP-0071
title: Learning Path PostgreSQL
type: learning-path
primary_domain: capstone
secondary_domains: [postgresql, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-CAP-0070]
related: [DBKB-CAP-0028, DBKB-CAP-0048]
aliases: [PostgreSQL path]
search_keywords: [PostgreSQL learning path, EXPLAIN, VACUUM, WAL, backup]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Ordered PostgreSQL path with query, transaction, maintenance, security and recovery milestones]
---
# Learning Path PostgreSQL

Sorrend: SQL foundations → relational modeling → PostgreSQL exercise → plans/indexes → transactions/locks → VACUUM/WAL/replication → backup/restore → PostgreSQL case/reference.

Exit criteria: version-aware runbook, actual plan/lock/backup evidence, least-privilege role, recovery validation és rollback.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
