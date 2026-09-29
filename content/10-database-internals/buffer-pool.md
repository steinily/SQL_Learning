---
schema_version: 1
id: DBKB-INT-0007
title: Buffer Pool
type: concept
primary_domain: database-internals
secondary_domains: [performance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-INT-0002]
related: [DBKB-INT-0008, DBKB-PERF-0024]
aliases: [shared buffer cache]
search_keywords: [buffer pool, cache hit, dirty buffer]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-INT-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Buffer hit, dirty page és eviction fogalmakat elválasztja]
---
# Buffer Pool

Buffer pool a gyakran használt data és index page-ek memóriabeli cache-e. Cache hit csökkenti a storage I/O-t, de hit ratio önmagában nem teljesítménybizonyíték; query latency, reads és contention együtt mérendő.

## Források
- [PostgreSQL 18 — Resource Consumption](https://www.postgresql.org/docs/18/runtime-config-resource.html)
