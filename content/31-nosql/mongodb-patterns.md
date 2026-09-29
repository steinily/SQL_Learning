---
schema_version: 1
id: DBKB-NOSQL-0020
title: MongoDB Patterns
type: technology
primary_domain: nosql
secondary_domains: [application-design, performance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb]
sql_dialects: []
scope: vendor-specific
prerequisites: [DBKB-NOSQL-0019]
related: [DBKB-NOSQL-0003, DBKB-NOSQL-0008]
aliases: [MongoDB design patterns]
search_keywords: [MongoDB embedding, referencing, aggregation, index, transaction]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000089]
acceptance_criteria: [Embedding/referencing, indexes, aggregation and transaction boundaries are addressed]
---
# MongoDB Patterns

Embedding akkor célszerű, ha az aggregate együtt olvasott és mérete bounded; referencing kell independently updated vagy nagy cardinality-jú relationnél. Indexeket a query shape és explain output alapján válassz, nem a mezők száma alapján.

Aggregation pipeline-nál korán szűrj, bounded resultot és memory/timeout limitet használj. Multi-document transaction csak indokolt invarianthez, explicit retry/idempotency és release-specific support mellett kerüljön be.

## Forrás
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
