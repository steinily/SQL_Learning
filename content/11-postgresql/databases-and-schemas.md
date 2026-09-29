---
schema_version: 1
id: DBKB-PG-0006
title: Databases and Schemas
type: concept
primary_domain: postgresql
secondary_domains: [architecture]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0002]
related: [DBKB-PG-0007]
aliases: [database namespace]
search_keywords: [PostgreSQL database, schema, search_path]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Cluster/database/schema namespace különbségét és search_path risket adja]
---
# Databases and Schemas

PostgreSQL cluster több database-t, database több schema namespace-t tartalmaz. `search_path` implicit object resolutiont okozhat; security-sensitive code használjon explicit schema qualificationt és kontrollált search pathot.

## Források
- [PostgreSQL 18 — Schemas](https://www.postgresql.org/docs/18/ddl-schemas.html)
