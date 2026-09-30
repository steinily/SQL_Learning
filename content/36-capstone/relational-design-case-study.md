---
schema_version: 1
id: DBKB-CAP-0002
title: Relational Design Case Study
type: case-study
primary_domain: capstone
secondary_domains: [relational-modeling, architecture]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-CAP-0001]
related: [DBKB-MODL-0001]
aliases: [relational case]
search_keywords: [relational design, normalization, keys, constraints, case study]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Scenario requires entities, keys, constraints, normalization and tradeoff evidence]
---
# Relational Design Case Study

Egy multi-tenant order domain számára tervezz customer, product, order és payment modellt. Mutasd be candidate key-eket, FK/unique/check constraint-eket, normalization trade-offot és tenant isolationt.

Elvárt evidence: ERD, DDL, representative queries, integrity test, migration/rollback és explicit assumptions. A választott dialect és tényleges execution külön legyen jelölve.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
