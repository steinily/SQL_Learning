---
schema_version: 1
id: DBKB-RDBE-0017
title: View Contract Design
type: concept
primary_domain: relational-database-engineering
secondary_domains: [integration, governance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-RDBE-0006, DBKB-MODL-0023]
related: [DBKB-RDBE-0012]
aliases: [view interface]
search_keywords: [view contract, column stability, grain, dependency]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-RDBE-0001]
source_ids: [SRC-000037]
acceptance_criteria: [View grain/type/name contractot és compatibility rule-t rögzít, SELECT * kerülését előírja]
---
# View Contract Design

View contractja a column name/type, row grain, nullability, ordering expectation és freshness semantic.
Consumer interface-ként explicit select listet használj, ne `SELECT *`-ot. Underlying table change csak
impact analysis és compatibility test után történjen.

View security, updatability és materialization nem implicit. Dokumentáld ownerét, dependencyit,
deprecation pathját és consumer SLA-ját.

## Források

- [PostgreSQL 18 Tutorial — Views](https://www.postgresql.org/docs/18/tutorial-views.html)
