---
schema_version: 1
id: DBKB-ORA-0005
title: Oracle Indexes and Execution Plans
type: technology
primary_domain: oracle
secondary_domains: [oracle, performance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [oracle-database]
sql_dialects: [oracle-sql]
scope: vendor-specific
prerequisites: [DBKB-ORA-0004]
related: [DBKB-PERF-0001]
aliases: [Oracle plan tuning]
search_keywords: [Oracle index, execution plan, optimizer statistics, partition pruning]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ORACLE-0001]
source_ids: [SRC-000101]
acceptance_criteria: [Oracle index candidate, optimizer plan, statistics and regression validation are explained]
---
# Oracle Indexes and Execution Plans

Index candidate-et query predicate/order, selectivity, cardinality, DML cost és storage alapján válassz. Explain/plan outputot representative statistics-szel értelmezd; hint csak documented hypothesis és rollback mellett.

Statistics refresh, bind peeking/plan stability, partition pruning és stale plan behavior okozhat regressziót. Before/after measure latency/resource/correctness és write impactot; egyetlen plan text nem benchmark.

## Forrás
- [Oracle Database Documentation](https://docs.oracle.com/en/database/oracle/oracle-database/)
