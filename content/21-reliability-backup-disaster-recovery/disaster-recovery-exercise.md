---
schema_version: 1
id: DBKB-DR-0018
title: Disaster Recovery Exercise
type: exercise
primary_domain: disaster-recovery
secondary_domains: [validation]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DR-0017]
related: []
aliases: [DR drill exercise]
search_keywords: [DR exercise, restore drill, failover, recovery evidence]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DR-0001]
source_ids: [SRC-000063, SRC-000064]
acceptance_criteria: [Exercise defines evidence without claiming unexecuted results]
---
# Disaster Recovery Exercise

Tervezd meg egy regional outage, backup restore és application cutover gyakorlatát. Határozd meg authorizationt, abort conditiont, dependency ordert, actual RTO/RPO mérését, data integrity reconciliationt, communicationt és remediation backlogot; execution-verified csak valódi gyakorlat után jelölhető.

## Források
- [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final)
- [PostgreSQL — Backup and Restore](https://www.postgresql.org/docs/current/backup.html)
