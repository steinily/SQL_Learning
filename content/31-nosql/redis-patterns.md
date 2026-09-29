---
schema_version: 1
id: DBKB-NOSQL-0019
title: Redis Patterns
type: technology
primary_domain: nosql
secondary_domains: [application-design, performance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [redis]
sql_dialects: []
scope: vendor-specific
prerequisites: [DBKB-NOSQL-0018]
related: [DBKB-NOSQL-0002]
aliases: [Redis design patterns]
search_keywords: [Redis cache, Redis stream, rate limiter, TTL, atomic command]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000090]
acceptance_criteria: [Redis structure selection, TTL, atomicity and durability cautions are covered]
---
# Redis Patterns

String/hash/list/set/sorted-set/stream választásnál az operation semantics, memory cost és cardinality legyen elsődleges. Rate limiterhez atomic increment/expiry vagy Lua-supported pattern kell, de a correctness és clock assumptions legyen explicit.

Cache patternnél TTL és invalidation, queue/stream patternnél consumer acknowledgement, replay és pending recovery szükséges. Redis durability, replication és eviction settinget a business criticality szerint válaszd; cache és source-of-truth szerepet ne keverd.

## Forrás
- [Redis Documentation](https://redis.io/docs/latest/)
