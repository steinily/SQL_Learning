---
schema_version: 1
id: DBKB-DR-0015
title: Data Loss Assessment
type: troubleshooting
primary_domain: disaster-recovery
secondary_domains: [data-quality]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-DR-0013]
related: []
aliases: [recovery data loss analysis]
search_keywords: [data loss, missing transactions, reconciliation, RPO breach]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DR-0001]
source_ids: [SRC-000063, SRC-000064]
acceptance_criteria: [Loss boundary, reconciliation and business impact are described]
---
# Data Loss Assessment

Data loss assessment az utolsó verified durable point, archive/replica gap, recovery target, committed transaction evidence és downstream reconciliation alapján határozza meg a loss boundary-t. Ne használj row countot kizárólagos proofként: domain totals, event IDs, audit trail és business owner confirmation is kellhet.

## Források
- [PostgreSQL — Continuous Archiving and PITR](https://www.postgresql.org/docs/current/continuous-archiving.html)
- [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final)
