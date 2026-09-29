---
schema_version: 1
id: DBKB-REC-0008
title: Migration Recipes
type: playbook
primary_domain: recipes
secondary_domains: [migration, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-REC-0007]
related: [DBKB-MIG-0001]
aliases: [schema migration runbook]
search_keywords: [expand contract, backfill, dual write, cutover, rollback]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000086]
acceptance_criteria: [Inventory, expand/contract, backfill, compatibility, cutover and rollback are actionable]
---
# Migration Recipes

Migration lépései: inventory and dependency graph, additive expand, dual-read/write vagy backfill, compatibility validation, cutover, old shape deprecation és cleanup. Minden lépéshez owner, metric, abort threshold és rollback boundary tartozzon.

Backfill legyen idempotent, resumable és throttled; compare row count, checksum, null/duplicate, FK/invariant és query latency. Destructive drop csak retention/backup és consumer sign-off után.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
