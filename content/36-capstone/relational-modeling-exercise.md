---
schema_version: 1
id: DBKB-CAP-0024
title: Relational Modeling Exercise
type: exercise
primary_domain: capstone
secondary_domains: [relational-modeling, sql]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-CAP-0023]
related: [DBKB-MODL-0001]
aliases: [relational model lab]
search_keywords: [ERD, primary key, foreign key, normalization, constraint]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Learner produces ERD, normalized schema, constraints and query workload]
---
# Relational Modeling Exercise

Modellezz subscription/billing domain-t customer, plan, subscription, invoice és payment entity-kkel. Indokold candidate/primary/foreign key-eket, cardinalityt, normalizationt és temporal/status mezőket.

Írj DDL-t constraints-szel és legalább öt representative query-t. Validate-old duplicate, orphan, invalid state transition és concurrent update edge case-eket; migration és rollback is legyen része.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
