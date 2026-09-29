---
schema_version: 1
id: DBKB-SS-0027
title: Always On Availability Groups
type: technology
primary_domain: sql-server
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0025]
related: [DBKB-SS-0028]
aliases: [AG, availability group]
search_keywords: [Always On, availability group, synchronous commit, failover]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Replica, synchronization, listener, failover és RTO/RPO caveat-et adja]
---
# Always On Availability Groups

Always On Availability Groups adatbázis-replikákat és listener endpointot használ HA/DR célra. Sync/async commit, redo/send queue, automatic/manual failover, quorum és client retry külön evidence-et igényel.

## Források
- [Microsoft Learn — Always On availability groups](https://learn.microsoft.com/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server)
