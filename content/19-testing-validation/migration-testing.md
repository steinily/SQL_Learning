---
schema_version: 1
id: DBKB-TEST-0015
title: Migration Testing
type: playbook
primary_domain: testing-validation
secondary_domains: [migration]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-TEST-0014]
related: []
aliases: [schema migration testing]
search_keywords: [migration test, expand contract, rollback, compatibility]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TEST-0001]
source_ids: [SRC-000058, SRC-000059]
acceptance_criteria: [Forward/backward compatibility, data validation and rollback are specified]
---
# Migration Testing

Migration test ellenőrizze syntax/metadata, forward és backward compatibility, data transformation, index/constraint behavior, application contractot, rollbackot és runtime durationt. Production rollout előtt representative volume és failure path kell; a dry-run önmagában nem bizonyítja az apply safety-t.

## Források
- [PostgreSQL — Regression Tests](https://www.postgresql.org/docs/current/regress.html)
- [Microsoft SQL Server Documentation](https://learn.microsoft.com/en-us/sql/relational-databases/)
