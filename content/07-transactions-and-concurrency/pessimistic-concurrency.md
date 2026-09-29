---
schema_version: 1
id: DBKB-TX-0016
title: Pessimistic Concurrency
type: concept
primary_domain: transactions-and-concurrency
secondary_domains: [application-design]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-TX-0009, DBKB-TX-0010]
related: [DBKB-TX-0015, DBKB-TX-0012]
aliases: [select for update, pessimistic locking]
search_keywords: [pessimistic concurrency, FOR UPDATE, lock before update]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Pessimistic lock használatát és költségeit transaction scope-pal írja le]
---
# Pessimistic Concurrency

Pessimistic concurrencynél a tranzakció előre lockolja a módosítandó erőforrást, például PostgreSQL `SELECT ... FOR UPDATE` segítségével. Ez csökkentheti az elvesző update kockázatát, de növeli a blocking és deadlock esélyét.

A lockolt sorok körét, timeoutot és transaction boundaryt mérhetően kell meghatározni; túl széles lock scope throughput-problémát okozhat.

## Források

- [PostgreSQL 18 — Explicit Locking](https://www.postgresql.org/docs/18/explicit-locking.html)
