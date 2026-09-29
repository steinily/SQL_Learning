---
schema_version: 1
id: DBKB-RDBE-0014
title: Relational Design Patterns
type: concept
primary_domain: relational-database-engineering
secondary_domains: [data-modeling]
levels: [intermediate, advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql, postgresql]
scope: cross-vendor
prerequisites: [DBKB-MODL-0017, DBKB-MODL-0020]
related: [DBKB-RDBE-0007, DBKB-RDBE-0010]
aliases: [relational schema patterns]
search_keywords: [header line, association, history, current state, reference]
risk: caution
version_sensitive: false
review_cycle: 24m
research_packages: [RP-RDBE-0001]
source_ids: [SRC-000009, SRC-000016]
acceptance_criteria: [Header-line, association, current-history és reference pattern trade-offot összevet]
---
# Relational Design Patterns

Header-line pattern order és order line grainet választ szét; association table M:N relationt kezel;
current/history pattern a jelen és audit state-et különíti el; reference table controlled vocabularyt
ad. Mindegyiknél PK, FK, duplicate és lifecycle contract explicit.

Pattern ne legyen dogma: workload, temporal requirement, tenant boundary és consumer interface alapján
válassz. Denormalized read projection külön ownerrel és refresh policyval éljen.

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
- [Microsoft — OLTP](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-transaction-processing)
