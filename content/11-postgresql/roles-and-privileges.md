---
schema_version: 1
id: DBKB-PG-0005
title: Roles and Privileges
type: concept
primary_domain: postgresql
secondary_domains: [security]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0002]
related: [DBKB-PG-0020, DBKB-PG-0021]
aliases: [PostgreSQL role, GRANT]
search_keywords: [PostgreSQL role, privileges, GRANT, REVOKE]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Role membership, ownership, GRANT/REVOKE és least privilege kapcsolatát leírja]
---
# Roles and Privileges

PostgreSQL role lehet login identity, group role vagy object owner. Effective privilege role membership, ownership, `GRANT`/`REVOKE` és default privileges kombinációjából áll; authorization claimhez `has_*_privilege` és catalog evidence kell.

## Források
- [PostgreSQL 18 — Database Roles](https://www.postgresql.org/docs/18/user-manag.html)
