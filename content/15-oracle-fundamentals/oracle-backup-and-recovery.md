---
schema_version: 1
id: DBKB-ORA-0007
title: Oracle Backup and Recovery
type: playbook
primary_domain: oracle
secondary_domains: [recovery, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [oracle-database, rman]
sql_dialects: [oracle-sql]
scope: vendor-specific
prerequisites: [DBKB-ORA-0006]
related: [DBKB-REC-0001]
aliases: [Oracle RMAN recovery]
search_keywords: [RMAN, backup, restore, recover, archive log, point in time]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ORACLE-0001]
source_ids: [SRC-000101]
acceptance_criteria: [Backup, restore validation, recovery objective and evidence steps are defined]
---
# Oracle Backup and Recovery

Az Oracle backup/recovery runbook a business RPO/RTO-ból induljon, majd RMAN backup policyt, archived redo kezelést és recovery destination kapacitást rögzítsen. A backup sikeressége önmagában nem bizonyítja a restore képességet.

Runbook: inventory és change freeze; backup metadata és output ellenőrzése; izolált restore/recover próba; consistency és application smoke test; időbélyegzett evidence; dokumentált rollback/escalation. Destructive recovery csak jóváhagyott környezetben futtatható.

## Forrás
- [Oracle Database Documentation](https://docs.oracle.com/en/database/oracle/oracle-database/)
