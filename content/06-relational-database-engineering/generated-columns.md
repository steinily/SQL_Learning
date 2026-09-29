---
schema_version: 1
id: DBKB-RDBE-0005
title: Generated Columns
type: concept
primary_domain: relational-database-engineering
secondary_domains: [data-modeling, data-integrity]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-SQL-0010, DBKB-MODL-0019]
related: [DBKB-RDBE-0002]
aliases: [computed column]
search_keywords: [generated column, computed, stored, derived value]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RDBE-0001]
source_ids: [SRC-000038]
acceptance_criteria: [Generated és client-maintained value-t elkülönít, Dependency és migration scope-ot rögzít]
---
# Generated Columns

Generated column értéke más column expressionéből származik, ezért a database tartja konzisztensen.
Ez jó derived value és indexelhető access shape lehet, de expression volatility, dependency, type,
write restriction és rebuild cost engine-specific.

Ne tárolj generated columnban olyan időt vagy external state-et, amely nem determinisztikus. A
business source-of-truth továbbra is az input column; generated value contractját és migration impactját
dokumentáld.

PostgreSQL syntax és támogatás version-sensitive, local SQLite evidence nélkül source-verified.

## Források

- [PostgreSQL 18 — CREATE TABLE](https://www.postgresql.org/docs/18/sql-createtable.html)
