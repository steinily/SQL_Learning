---
schema_version: 1
id: DBKB-SS-0005
title: SQL Server Security
type: concept
primary_domain: sql-server
secondary_domains: [security]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0004]
related: [DBKB-PG-0020]
aliases: [SQL Server access control]
search_keywords: [SQL Server security, login, user, role, GRANT]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Login/user/role/permission és least privilege rétegeit adja]
---
# SQL Server Security

SQL Server security login, database user, role, ownership és permission rétegekből áll. Object-level `GRANT`/`DENY`/`REVOKE`, ownership chain és service identity behaviorét explicit security reviewben ellenőrizd.

## Források
- [Microsoft Learn — Permissions hierarchy](https://learn.microsoft.com/sql/relational-databases/security/permissions-database-engine)
