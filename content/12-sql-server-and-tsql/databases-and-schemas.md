---
schema_version: 1
id: DBKB-SS-0004
title: Databases and Schemas
type: concept
primary_domain: sql-server
secondary_domains: [schema-design]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0002]
related: [DBKB-SS-0005]
aliases: [SQL Server schema]
search_keywords: [SQL Server database, schema, dbo, three-part name]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Instance/database/schema/object namespace és ownership különbségét adja]
---
# Databases and Schemas

SQL Server instance database-eket hostol; database-en belül schema namespace-ek és objects vannak. Three-part naming, default schema és ownership deployment/security behaviorre hat, ezért explicit qualification és owner policy szükséges.

## Források
- [Microsoft Learn — Database-level roles](https://learn.microsoft.com/sql/relational-databases/security/authentication-access/database-level-roles)
