---
schema_version: 1
id: DBKB-RDBE-0013
title: Naming and Ownership
type: concept
primary_domain: relational-database-engineering
secondary_domains: [governance, security]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql, postgresql]
scope: cross-vendor
prerequisites: [DBKB-MODL-0022, DBKB-RDBE-0008]
related: [DBKB-RDBE-0019]
aliases: [database naming convention]
search_keywords: [naming, ownership, role, schema, identifier]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-RDBE-0001]
source_ids: [SRC-000009, SRC-000038]
acceptance_criteria: [Stable naming és owner policyt ad, Reserved words/case/search path risket kezeli]
---
# Naming and Ownership

Naming convention tegye láthatóvá az object purpose-ét, grainjét és lifecycle-ját; kerüld az implicit
pluralizálást, reserved wordöt és case-sensitive quoted identifier dependencyt. Stable names támogatják
a migration és observability eszközöket.

Ownership különítsen execution role-t, migration owner-t és data stewardet. Least privilege és default
privilege policy legyen, ne személyes ownerhez kötött production object.

## Források

- [PostgreSQL 18 — CREATE TABLE](https://www.postgresql.org/docs/18/sql-createtable.html)
- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
