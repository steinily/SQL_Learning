---
schema_version: 1
id: DBKB-IDX-0001
title: Indexing Overview
type: overview
primary_domain: indexing
secondary_domains: [performance]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-TX-0017]
related: [DBKB-IDX-0002, DBKB-IDX-0003]
aliases: [database indexes]
search_keywords: [indexing, database index, access path]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Index célját és trade-offjait összefoglalja]
---
# Indexing Overview

Az index másodlagos access path, amely bizonyos predicate, ordering vagy join műveleteket gyorsíthat. Cserébe storage-ot, write costot és maintenance-et ad a rendszerhez.

## Források
- [PostgreSQL 18 — Indexes](https://www.postgresql.org/docs/18/indexes.html)
