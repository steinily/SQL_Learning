---
schema_version: 1
id: DBKB-CAP-0047
title: Reference Modeling Glossary
type: reference
primary_domain: capstone
secondary_domains: [relational-modeling, data-modeling]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0046]
related: [DBKB-MODL-0001]
aliases: [modeling quick reference]
search_keywords: [entity, relationship, cardinality, normalization, key, constraint]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Modeling terms, integrity controls and denormalization tradeoffs are summarized]
---
# Reference Modeling Glossary

Entity/attribute/relationship, cardinality, candidate/primary/foreign key, natural/surrogate key, normalization, functional dependency, aggregate, temporal validity és denormalization a core terms.

Model reviewnél kérdezd: melyik invariantet constraint védi, hol a source-of-truth, milyen access pattern, lifecycle, ownership és migration path van. Diagram önmagában nem implementál integrity-t.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
