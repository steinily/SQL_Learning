---
schema_version: 1
id: DBKB-TX-0012
title: Deadlocks
type: troubleshooting
primary_domain: transactions-and-concurrency
secondary_domains: [operations]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-TX-0011]
related: [DBKB-TX-0019, DBKB-TX-0024]
aliases: [deadlock detection, transaction cycle]
search_keywords: [deadlock, lock cycle, deadlock retry]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-TX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Deadlock cycle, prevention és retry különbséget magyaráz]
---
# Deadlocks

Deadlock akkor jön létre, amikor tranzakciók kölcsönösen olyan lockokra várnak, amelyeket egymás tart. Az engine a ciklus egyik tranzakcióját megszakíthatja; az alkalmazásnak a retry-t csak biztonságos, idempotens műveletnél szabad alkalmaznia.

Megelőzéshez konzisztens resource-ordering, rövid transaction és determinisztikus hozzáférési sorrend kell. A konkrét error code és timeout engine/version dependent.

## Források

- [PostgreSQL 18 — Deadlocks](https://www.postgresql.org/docs/18/explicit-locking.html#LOCKING-DEADLOCKS)
