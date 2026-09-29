---
schema_version: 1
id: DBKB-OPS-0005
title: Users Roles and Privileges Operations
type: technology
primary_domain: database-operations
secondary_domains: [security]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OPS-0004]
related: []
aliases: [DBA access operations]
search_keywords: [roles, grants, privilege review, service account]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OPS-0001]
source_ids: [SRC-000049]
acceptance_criteria: [Access lifecycle and least privilege review are explained]
---
# Users Roles and Privileges Operations

User- és role-lifecycle-ben legyen owner, purpose, expiry vagy review date, valamint auditálható grant inventory. Privilege change előtt scope-old a service account-ot, alkalmazd least privilege alapján, és ellenőrizd effective permissions-t a target engine saját semantics-a szerint.

## Források
- [PostgreSQL — Database Roles](https://www.postgresql.org/docs/current/user-manag.html)
