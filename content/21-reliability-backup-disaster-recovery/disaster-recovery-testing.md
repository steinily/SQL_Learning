---
schema_version: 1
id: DBKB-DR-0012
title: Disaster Recovery Testing
type: playbook
primary_domain: disaster-recovery
secondary_domains: [testing-validation]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DR-0011]
related: []
aliases: [DR drill]
search_keywords: [DR test, restore drill, failover exercise, RTO RPO evidence]
risk: destructive
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DR-0001]
source_ids: [SRC-000063, SRC-000064, SRC-000065]
acceptance_criteria: [Authorized test scope, measured recovery and remediation are defined]
---
# Disaster Recovery Testing

DR test lehet tabletop, component restore, clean-room restore, failover vagy full exercise; scope, authorization, abort condition, data safety, communication és evidence előre legyen. Actual RTO/RPO, integrity, dependency readiness és runbook gaps alapján remediation backlog készüljön.

## Források
- [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final)
- [PostgreSQL — Backup and Restore](https://www.postgresql.org/docs/current/backup.html)
