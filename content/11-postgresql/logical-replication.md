---
schema_version: 1
id: DBKB-PG-0028
title: Logical Replication
type: technology
primary_domain: postgresql
secondary_domains: [replication]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0027]
related: [DBKB-INT-0018]
aliases: [publication/subscription]
search_keywords: [PostgreSQL logical replication, publication, subscription, replication slot]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Publication, subscription, slot, conflict és DDL limitation scopeját adja]
---
# Logical Replication

Logical replication publication/subscription modellel row changeset továbbít. Replication slot retention, initial copy, conflict, schema/DDL drift és apply lag operational evidence-et igényel; exactly-once üzleti hatás nem automatikus.

## Források
- [PostgreSQL 18 — Logical Replication](https://www.postgresql.org/docs/18/logical-replication.html)
