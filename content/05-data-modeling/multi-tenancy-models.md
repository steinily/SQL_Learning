---
schema_version: 1
id: DBKB-MODL-0014
title: Multi-Tenancy Models
type: concept
primary_domain: data-modeling
secondary_domains: [security, operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql, postgresql]
scope: cross-vendor
prerequisites: [DBKB-MODL-0004, DBKB-MODL-0007]
related: [DBKB-MODL-0010, DBKB-MODL-0022]
aliases: [tenant isolation]
search_keywords: [multi-tenancy, tenant_id, shared schema, isolation]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MODL-0002]
source_ids: [SRC-000009, SRC-000014]
acceptance_criteria: [Shared table/schema/database modelt összevet, Tenant isolation és key scope mindenhol explicit]
---
# Multi-Tenancy Models

Három gyakori modell: shared table `tenant_id`-val, tenantenként schema, vagy tenantenként database.
Shared table olcsóbb és egyszerűbben skálázható, de minden query, key, unique constraint és job tenant
scope-ot igényel. Schema/database isolation erősebb boundaryt ad, nagyobb provisioning és operations
költséggel.

Tenant ID ne csak application convention legyen: composite FK/UNIQUE, row-level policy vagy repository
helper kényszerítse. Cross-tenant reporting és admin access explicit privileged path. Cache key,
background job, export, backup/restore és log redaction is tenant boundary.

A `SQL-MODL-0014` fixture tenant-keyed orders queryjét validálja; ez nem helyettesít production
authorization testet.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
- [PostgreSQL 18 — Concurrency Control](https://www.postgresql.org/docs/18/mvcc.html)
