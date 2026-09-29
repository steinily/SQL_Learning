---
schema_version: 1
id: DBKB-PG-0038
title: PostgreSQL Incident Runbook
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
prerequisites: [DBKB-PG-0025, DBKB-PG-0031]
related: [DBKB-INT-0024]
aliases: [PostgreSQL incident response]
search_keywords: [PostgreSQL incident, replication lag, corruption, failover]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Safety, scope, evidence, mitigation, recovery és postmortem lépéseket ad]
---
# PostgreSQL Incident Runbook

Incident flow: client impact és safety; active sessions/waits; storage/WAL/replication signal; recent change; reversible mitigation; backup/replica evidence; recovery/failover decision; communication; postmortem. File/catalog repair csak specialist escalation.

## Források
- [PostgreSQL 18 — Monitoring](https://www.postgresql.org/docs/18/monitoring.html)
