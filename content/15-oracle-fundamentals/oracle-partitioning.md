---
schema_version: 1
id: DBKB-ORA-0006
title: Oracle Partitioning
type: technology
primary_domain: oracle
secondary_domains: [storage, performance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [oracle-database]
sql_dialects: [oracle-sql]
scope: vendor-specific
prerequisites: [DBKB-ORA-0005]
related: [DBKB-STOR-0001]
aliases: [Oracle table partitioning]
search_keywords: [range partition, list partition, hash partition, partition pruning]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ORACLE-0001]
source_ids: [SRC-000101]
acceptance_criteria: [Partitioning strategy, pruning, lifecycle and maintenance risks are explained]
---
# Oracle Partitioning

Partitioning egy logical tablet több physical partitionre bont; a választás a partition key, pruning lehetőség, lifecycle és maintenance alapján történik. Range, list és hash stratégiát az Oracle release/edition támogatási mátrixával kell egyeztetni.

Tervezési ellenőrzőlista: válassz stabil, gyakran szűrt kulcsot; ellenőrizd a local/global index trade-offot; tervezz partition maintenance és statistics frissítést; mérd a pruningot execution planben. A partitioning nem helyettesíti az adatmodellt vagy a workload-tesztet.

## Forrás
- [Oracle Database Documentation](https://docs.oracle.com/en/database/oracle/oracle-database/)
