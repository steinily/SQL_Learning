---
schema_version: 1
id: DBKB-ORA-0002
title: Oracle SQL and PL SQL
type: technology
primary_domain: oracle
secondary_domains: [sql, programming]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [oracle-database]
sql_dialects: [oracle-sql, plsql]
scope: vendor-specific
prerequisites: [DBKB-ORA-0001]
related: [DBKB-SQL-0001]
aliases: [Oracle SQL PL/SQL]
search_keywords: [Oracle SQL, PL/SQL, package, procedure, function, exception]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ORACLE-0001]
source_ids: [SRC-000101]
acceptance_criteria: [Oracle SQL/PLSQL execution, exception, bind and transaction boundaries are explained]
---
# Oracle SQL and PL SQL

Oracle SQL query-k és PL/SQL procedure/function/package együtt adhatnak adat- és üzleti logikát. Bind variable, explicit exception handling, transaction boundary, privilege context és instrumentation legyen tudatos.

PL/SQL block sikeres compile-ja nem bizonyít runtime correctnesset; teszteld null/error/concurrency és rollback eseteket. Dynamic SQL csak parameter bindinggal és allow-listed object identifierrel használható.

## Forrás
- [Oracle Database Documentation](https://docs.oracle.com/en/database/oracle/oracle-database/)
