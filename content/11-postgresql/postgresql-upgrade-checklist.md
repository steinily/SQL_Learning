---
schema_version: 1
id: DBKB-PG-0039
title: PostgreSQL Upgrade Checklist
type: playbook
primary_domain: postgresql
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0027, DBKB-PG-0031]
related: [DBKB-PG-0040]
aliases: [PostgreSQL upgrade runbook]
search_keywords: [PostgreSQL upgrade checklist, pg_upgrade checklist]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Precheck, rehearsal, compatibility, cutover, verification és rollback lépéseit adja]
---
# PostgreSQL Upgrade Checklist

Precheck: version/extension/client compatibility, backup/restore, disk and downtime. Rehearsal: representative migration and query validation. Cutover: freeze, backup, upgrade, smoke tests. Aftercare: plan/statistics, replication, monitoring, rollback window.

## Források
- [PostgreSQL 18 — Upgrading a PostgreSQL Cluster](https://www.postgresql.org/docs/18/upgrading.html)
