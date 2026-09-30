---
schema_version: 1
id: DBKB-ORA-0011
title: Oracle Migration
type: playbook
primary_domain: oracle
secondary_domains: [migration, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [oracle-database]
sql_dialects: [oracle-sql]
scope: vendor-specific
prerequisites: [DBKB-ORA-0010]
related: [DBKB-MIG-0001]
aliases: [Oracle migration runbook]
search_keywords: [Oracle migration, upgrade, cutover, compatibility, rollback]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ORACLE-0001]
source_ids: [SRC-000101]
acceptance_criteria: [Assessment, rehearsal, cutover, validation and rollback are defined]
---
# Oracle Migration

Migration előtt inventory, compatibility, dependency, data-volume és downtime/RPO/RTO assessment szükséges. A target release és edition támogatását official Oracle dokumentációból kell igazolni.

Runbook: schema/code scan; representative rehearsal; backup and rollback checkpoint; controlled cutover; row/count/checksum and application validation; observability review; signed go/no-go. Production result csak tényleges execution evidence után jelölhető.

## Forrás
- [Oracle Database Documentation](https://docs.oracle.com/en/database/oracle/oracle-database/)
