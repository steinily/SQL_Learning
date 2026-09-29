---
schema_version: 1
id: DBKB-PG-0002
title: PostgreSQL Architecture
type: concept
primary_domain: postgresql
secondary_domains: [architecture]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0001]
related: [DBKB-INT-0001, DBKB-PG-0004]
aliases: [PostgreSQL server architecture]
search_keywords: [PostgreSQL architecture, postmaster, backend process, cluster]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Cluster, server process, backend és database relationshipet adja]
---
# PostgreSQL Architecture

PostgreSQL server process-eket és database cluster struktúrát használ; client connection backend processhez kapcsolódik, amely shared resources-szal dolgozik. A pontos process és memory model PostgreSQL version és deployment context függő.

## Források
- [PostgreSQL 18 — Server Setup and Operation](https://www.postgresql.org/docs/18/server-start.html)
