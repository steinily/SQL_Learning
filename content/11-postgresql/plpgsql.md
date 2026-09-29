---
schema_version: 1
id: DBKB-PG-0015
title: PL/pgSQL
type: technology
primary_domain: postgresql
secondary_domains: [programming]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0014]
related: [DBKB-PG-0016, DBKB-PG-0017]
aliases: [PLpgSQL]
search_keywords: [PL/pgSQL, procedural language, exception handling]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [PL/pgSQL block, variable, control flow és exception scopeját adja]
---
# PL/pgSQL

PL/pgSQL database-side procedural language control flowot, variables, dynamic SQL-t és exception handlinget biztosít. Function hosszú transactiont és lockot tarthat, ezért performance és security review kötelező.

## Források
- [PostgreSQL 18 — PL/pgSQL](https://www.postgresql.org/docs/18/plpgsql.html)
