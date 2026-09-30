---
schema_version: 1
id: DBKB-CAP-0046
title: Reference SQL Glossary
type: reference
primary_domain: capstone
secondary_domains: [sql, learning]
levels: [beginner]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-CAP-0045]
related: [DBKB-SQL-0001]
aliases: [SQL quick reference]
search_keywords: [SQL glossary, SELECT, DML, DDL, transaction, "NULL"]
risk: safe
version_sensitive: false
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000001]
acceptance_criteria: [SQL core terms, command families, safety and dialect caveats are summarized]
---
# Reference SQL Glossary

Core: relation/table, row, column, key, constraint, `SELECT`, `INSERT`, `UPDATE`, `DELETE`, DDL, DML, transaction, isolation, index, NULL, predicate, join, aggregate és execution plan.

Mindig jelöld a dialectet, NULL semantics-et, transaction boundary-t, destructive risket és validationt. A concise reference nem helyettesíti a linked vendor documentationt.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
