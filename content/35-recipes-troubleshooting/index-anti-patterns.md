---
schema_version: 1
id: DBKB-REC-0043
title: Index Anti-Patterns
type: error
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
prerequisites: [DBKB-REC-0042]
related: [DBKB-IDX-0001]
aliases: [index mistakes]
search_keywords: [unused index, duplicate index, low selectivity, index bloat]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Index anti-pattern detection and safe removal/change are described]
---
# Index Anti-Patterns

Kerüld a duplicate/overlapping vagy unused indexet, low-selectivity-only indexet, wrong composite ordert, minden fieldre indexet, high-churn tableen uncontrolled indexet és indexet rossz query shape elfedésére.

Removal előtt usage/plan inventory, dependency, backup, rollback és post-drop regression test kell. Measure write latency, storage, bloat/fragmentation és query p95; index count önmagában nem quality metric.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
