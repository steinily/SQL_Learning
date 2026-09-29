---
schema_version: 1
id: DBKB-RDBE-0008
title: Schemas and Namespaces
type: concept
primary_domain: relational-database-engineering
secondary_domains: [security, governance]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-MODL-0002, DBKB-MODL-0022]
related: [DBKB-RDBE-0013]
aliases: [schema namespace]
search_keywords: [schema, namespace, search path, ownership, qualification]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RDBE-0001]
source_ids: [SRC-000038, SRC-000009]
acceptance_criteria: [Namespace és security boundary különbségét adja, Qualification és search path risket dokumentál]
---
# Schemas and Namespaces

Schema namespace objectnevek és ownership kezelésére szolgál; nem automatikusan tenant vagy security
boundary. PostgreSQL `search_path` implicit object resolutiont okozhat, ezért production DDL és query
explicit qualificationt, trusted pathot és privilege policyt igényel.

Schema ownership, default privileges, migration role és cross-schema dependency legyen rögzítve.
Azonos objectnév shadowingot okozhat; `schema.object` formával tedd egyértelművé a lineage-et.

## Források

- [PostgreSQL 18 — CREATE TABLE](https://www.postgresql.org/docs/18/sql-createtable.html)
- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
