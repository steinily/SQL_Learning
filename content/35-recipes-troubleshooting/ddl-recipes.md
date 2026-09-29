---
schema_version: 1
id: DBKB-REC-0002
title: DDL Recipes
type: cheatsheet
primary_domain: recipes
secondary_domains: [sql, migration]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-REC-0001]
related: [DBKB-MIG-0001]
aliases: [schema change recipes]
search_keywords: [CREATE TABLE, ALTER TABLE, index, constraint, DDL]
risk: destructive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000086]
acceptance_criteria: [DDL prechecks, locking impact, rollback and dialect caveats are covered]
---
# DDL Recipes

DDL előtt inspectáld a current schema-t, dependencyket, lock/timeout policy-t és rollback lehetőséget. Additive column/constraint/index legyen expand lépés; destructive drop/rename csak usage inventory, backup és approved cutover után.

Validate catalog diff, application compatibility, constraint violations, index build progress és query plan. A syntax és transactional DDL behavior dialect-specific; production run előtt staging vagy read-only precheck szükséges.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
