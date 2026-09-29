---
schema_version: 1
id: DBKB-DR-0011
title: Failover and Failback
type: playbook
primary_domain: disaster-recovery
secondary_domains: [high-availability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DR-0010]
related: []
aliases: [database failover runbook]
search_keywords: [failover, failback, split brain, fencing, promotion]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DR-0001]
source_ids: [SRC-000064, SRC-000065]
acceptance_criteria: [Decision, fencing, promotion, client routing and failback are specified]
---
# Failover and Failback

Failover előtt confirmáld failure scope-ot, fencinget, data freshness-t, promotion eligibility-t és client routingot. Failback külön change: source recovery, divergence reconciliation, replication re-seed, traffic drain és verification kell; automatic failover nem bizonyítja safe failbackot.

## Források
- [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final)
- [Microsoft — Backup and Restore](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/)
