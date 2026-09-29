---
schema_version: 1
id: DBKB-PG-0021
title: Row Level Security
type: technology
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
prerequisites: [DBKB-PG-0020]
related: [DBKB-PG-0005]
aliases: [RLS]
search_keywords: [row level security, policy, USING, WITH CHECK]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [RLS enable/force, USING/WITH CHECK és owner bypass caveat-et adja]
---
# Row Level Security

RLS policy row visibilityt (`USING`) és write admissiont (`WITH CHECK`) szabályozhat. Enable/force state, table owner behavior, role context és policy composition security testtel bizonyítandó.

## Források
- [PostgreSQL 18 — Row Security Policies](https://www.postgresql.org/docs/18/ddl-rowsecurity.html)
