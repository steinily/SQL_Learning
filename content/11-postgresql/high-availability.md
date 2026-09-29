---
schema_version: 1
id: DBKB-PG-0030
title: High Availability
type: concept
primary_domain: postgresql
secondary_domains: [reliability]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-PG-0029]
related: [DBKB-PG-0031, DBKB-PG-0032]
aliases: [PostgreSQL HA, failover]
search_keywords: [high availability, failover, switchover, RTO, RPO]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [HA topology, RTO/RPO, failover és split-brain risket definiálja]
---
# High Availability

HA nem pusztán standby jelenlét: failure detection, promotion, fencing, client routing, data loss tolerance és restore path együttese. RTO/RPO claimet tényleges failover és recovery drill bizonyít.

## Források
- [PostgreSQL 18 — High Availability](https://www.postgresql.org/docs/18/high-availability.html)
