---
schema_version: 1
id: DBKB-PG-0020
title: PostgreSQL Security
type: concept
primary_domain: postgresql
secondary_domains: [security]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0005, DBKB-PG-0006]
related: [DBKB-PG-0021, DBKB-PG-0022]
aliases: [PostgreSQL access control]
search_keywords: [PostgreSQL security, privilege, authentication, authorization]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Authentication, authorization, network trust és least privilege rétegeit adja]
---
# PostgreSQL Security

PostgreSQL security rétegei: connection authentication, role/privilege authorization, object ownership, row-level policy, TLS és operational audit. A `SUPERUSER` vagy broad role shortcutokat least-privilege designnal váltsd ki.

## Források
- [PostgreSQL 18 — Client Authentication](https://www.postgresql.org/docs/18/client-authentication.html)
