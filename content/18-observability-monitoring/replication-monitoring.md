---
schema_version: 1
id: DBKB-OBS-0012
title: Replication Monitoring
type: technology
primary_domain: observability
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OBS-0003]
related: []
aliases: [replication lag monitoring]
search_keywords: [replication lag, replay, apply delay, replica health]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OBS-0001]
source_ids: [SRC-000054]
acceptance_criteria: [Lag dimensions, freshness impact and failover caveats are covered]
---
# Replication Monitoring

Replication monitoring külön mérje a transport, receive, apply/replay és data freshness lagot, valamint slot/log retention és replica availability jeleket. A lag threshold workload és RPO függő; failover readiness-t nem bizonyítja egyetlen zero-lag mérőszám.

## Források
- [PostgreSQL — Monitoring Database Activity](https://www.postgresql.org/docs/current/monitoring.html)
