---
schema_version: 1
id: DBKB-OBS-0013
title: Capacity and Storage Monitoring
type: technology
primary_domain: observability
secondary_domains: [capacity-planning]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OBS-0003]
related: []
aliases: [database storage telemetry]
search_keywords: [disk usage, growth rate, IOPS, capacity alert]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OBS-0001]
source_ids: [SRC-000054]
acceptance_criteria: [Capacity dimensions, trends and response signals are defined]
---
# Capacity and Storage Monitoring

Capacity telemetry-ben absolute free space, growth rate, log/WAL usage, I/O latency, throughput, inode vagy file limit és backup footprint szerepeljen. Alert window és forecast legyen workload-aware; disk expansion előtt azonosítsd a retention, runaway query vagy replication root cause-ot.

## Források
- [PostgreSQL — Managing Disk Usage](https://www.postgresql.org/docs/current/diskusage.html)
