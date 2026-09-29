---
schema_version: 1
id: DBKB-INT-0008
title: Shared Buffers
type: technology
primary_domain: database-internals
secondary_domains: [postgresql]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0007]
related: [DBKB-INT-0023]
aliases: [shared_buffers]
search_keywords: [shared buffers, buffer cache, cache residency]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [shared_buffers konfigurációs szerepét és tuning caveatjét adja]
---
# Shared Buffers

`shared_buffers` a PostgreSQL saját buffer cache-ének méretét szabályozza. Túl alacsony érték I/O-t, túl magas érték OS cache és concurrency trade-offot okozhat; tuninghoz workload baseline és restart/change plan szükséges.

## Források
- [PostgreSQL 18 — Resource Consumption](https://www.postgresql.org/docs/18/runtime-config-resource.html)
