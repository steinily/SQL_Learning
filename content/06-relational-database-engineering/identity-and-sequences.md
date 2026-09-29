---
schema_version: 1
id: DBKB-RDBE-0004
title: Identity and Sequences
type: concept
primary_domain: relational-database-engineering
secondary_domains: [postgresql, data-modeling]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-MODL-0007, DBKB-SQL-0020]
related: [DBKB-RDBE-0005]
aliases: [generated identity, sequence]
search_keywords: [identity, sequence, auto increment, gap, generated key]
risk: caution
version_sensitive: true
review_cycle: 12m
research_packages: [RP-RDBE-0001]
source_ids: [SRC-000038, SRC-000009]
acceptance_criteria: [Identity generation és business uniqueness különbségét adja, Gap és retry behavior-t nem hibának nevezi]
---
# Identity and Sequences

Identity/sequence technikai key-ek generálására szolgál. A sequence értékei concurrency, rollback,
cache vagy failed insert miatt gapeket tartalmazhatnak; gap-free business numbering külön, drágább
transaction policy.

Identity nem business uniqueness: alternate key constraint továbbra is szükséges. Explicit override,
restart, migration és replication behavior engine-specific. External invoice numbert ne keverd
automatikusan surrogate identityvel.

## Források

- [PostgreSQL 18 — CREATE TABLE](https://www.postgresql.org/docs/18/sql-createtable.html)
- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
