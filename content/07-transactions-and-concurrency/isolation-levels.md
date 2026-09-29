---
schema_version: 1
id: DBKB-TX-0006
title: Isolation Levels
type: concept
primary_domain: transactions-and-concurrency
secondary_domains: [concurrency]
levels: [intermediate, advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-TX-0005]
related: [DBKB-TX-0007, DBKB-TX-0013]
aliases: [transaction isolation]
search_keywords: [read committed, repeatable read, serializable, isolation]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Isolation levelt observable phenomena-hoz köti, PostgreSQL scope-ot és serialization retryt ad]
---
# Isolation Levels

Isolation level concurrency phenomena és conflict behavior contractja. Named levels között engine-ek
jelentése és implementationje eltérhet; PostgreSQL 18 documentationből nem általánosítunk minden DBMS-re.

Alacsonyabb isolation több concurrencyt, kevesebb coordinationt, de több anomaly lehetőségét adhatja.
Serializable erősebb invariant protectiont céloz, de serialization failure miatt retry path kellhet.

Isolation választás business invariantből induljon, ne defaultból. Teszteld read/write patternnel,
expected error handlinggel és reprezentatív concurrencyval.

## Források

- [PostgreSQL 18 — Transaction Isolation](https://www.postgresql.org/docs/18/transaction-iso.html)
- [PostgreSQL 18 — Concurrency Control](https://www.postgresql.org/docs/18/mvcc.html)
