---
schema_version: 1
id: DBKB-DDS-0016
title: Distributed Caching
type: technology
primary_domain: distributed-data-systems
secondary_domains: [performance, application-design]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-cassandra]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DDS-0015]
related: [DBKB-PERF-0001]
aliases: [cache coherence, distributed cache]
search_keywords: [distributed cache, cache invalidation, TTL, stampede, stale data]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-DDS-0001]
source_ids: [SRC-000086]
acceptance_criteria: [Cache consistency, invalidation, TTL, stampede and failure behavior are covered]
---
# Distributed Caching

Cache csak explicit freshness és correctness contract mellett használható. Definiáld a key namespace-t, TTL-t, invalidation forrást, stale-read policy-t és azt, hogy cache outage esetén mi a source-of-truth fallback.

Cache stampede ellen jitterelt TTL, request coalescing vagy bounded refresh használható. Sensitive data cache-elésekor encryption, access isolation és eviction evidence kell; a cache hit rate nem helyettesíti az origin quality metricet.

## Forrás
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
