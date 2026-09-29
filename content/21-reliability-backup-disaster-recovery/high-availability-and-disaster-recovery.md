---
schema_version: 1
id: DBKB-DR-0006
title: High Availability and Disaster Recovery
type: comparison
primary_domain: reliability
secondary_domains: [architecture]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DR-0002]
related: []
aliases: [HA versus DR]
search_keywords: [high availability, disaster recovery, failover, replica, regional recovery]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DR-0001]
source_ids: [SRC-000063, SRC-000064, SRC-000065]
acceptance_criteria: [HA and DR goals, failure domains and trade-offs are distinguished]
---
# High Availability and Disaster Recovery

HA a service interruption valószínűségét és failover time-ot csökkenti egy failure domain-en belül; DR szélesebb site/region vagy catastrophic recovery cél. Replica, synchronous commit vagy clustering nem automatikusan backup, corruption protection vagy cross-region DR proof.

## Források
- [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final)
- [Microsoft — Backup and Restore](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/)
