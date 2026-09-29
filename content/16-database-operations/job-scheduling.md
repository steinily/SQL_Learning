---
schema_version: 1
id: DBKB-OPS-0012
title: Job Scheduling
type: technology
primary_domain: database-operations
secondary_domains: [automation]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OPS-0009]
related: []
aliases: [database scheduled jobs]
search_keywords: [scheduler, cron, SQL Agent, scheduled maintenance]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OPS-0001]
source_ids: [SRC-000049]
acceptance_criteria: [Scheduling ownership, retries and overlap controls are described]
---
# Job Scheduling

Database jobhoz owner, schedule, timezone, concurrency policy, timeout, retry és alert destination tartozzon. Idempotency és overlap prevention nélkül egy retry vagy clock change duplikált terhelést és adatváltozást okozhat.

## Források
- [PostgreSQL — Background Worker Processes](https://www.postgresql.org/docs/current/bgworker.html)
