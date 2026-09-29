---
schema_version: 1
id: DBKB-REC-0006
title: Index Recipes
type: playbook
primary_domain: recipes
secondary_domains: [sql, performance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-REC-0005]
related: [DBKB-IDX-0001]
aliases: [index runbook]
search_keywords: [CREATE INDEX, index selectivity, online index, rebuild]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000086]
acceptance_criteria: [Index candidate analysis, lock/build impact, validation and rollback are described]
---
# Index Recipes

Index előtt capture query shape, selectivity, cardinality, write rate, storage és existing index overlap. Choose composite column order from predicates/order, majd validate-old dialect-specific explain/profile outputtal.

Build/rebuildhez online/concurrent capability, lock timeout, resource headroom és rollback kell; index creation success nem bizonyít query improvementet. Monitoráld build progress, bloat/fragmentation és write latency-t.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
