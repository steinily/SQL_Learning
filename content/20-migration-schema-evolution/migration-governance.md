---
schema_version: 1
id: DBKB-MIG-0018
title: Migration Governance
type: playbook
primary_domain: migration
secondary_domains: [governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-MIG-0017]
related: []
aliases: [schema change governance]
search_keywords: [migration approval, change record, risk, exception]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-MIG-0001]
source_ids: [SRC-000060, SRC-000061, SRC-000062]
acceptance_criteria: [Approval, ownership, evidence, exception and review lifecycle are stated]
---
# Migration Governance

Migration governance-ban owner, risk classification, dependency map, test evidence, change approval, window, abort/rollback decision maker, communication és post-change review szerepeljen. Emergency path legyen time-bound és utólagos evidence/review kötelezettséggel, ne legyen állandó bypass.

## Források
- [PostgreSQL — SQL Commands](https://www.postgresql.org/docs/current/sql-commands.html)
