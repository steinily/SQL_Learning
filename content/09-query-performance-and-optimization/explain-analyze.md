---
schema_version: 1
id: DBKB-PERF-0003
title: EXPLAIN ANALYZE
type: technology
primary_domain: query-performance
secondary_domains: [postgresql]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PERF-0002]
related: [DBKB-PERF-0024]
aliases: [runtime plan]
search_keywords: [EXPLAIN ANALYZE, actual rows, buffers]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PERF-0001]
source_ids: [SRC-000014]
acceptance_criteria: [EXPLAIN ANALYZE execution és side-effect kockázatát dokumentálja]
---
# EXPLAIN ANALYZE

Az `EXPLAIN ANALYZE` ténylegesen lefuttatja a statementet, és actual timing/rows adatokat ad. DML esetén side effectet okozhat; használj tranzakciós rollbacket vagy read-only reprodukciót, és ne állíts elő execution evidence nélkül.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
