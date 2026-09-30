---
schema_version: 1
id: DBKB-ORA-0004
title: Oracle Transactions and Isolation
type: technology
primary_domain: oracle
secondary_domains: [transactions, reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [oracle-database]
sql_dialects: [oracle-sql, plsql]
scope: vendor-specific
prerequisites: [DBKB-ORA-0003]
related: [DBKB-TX-0001]
aliases: [Oracle transaction isolation]
search_keywords: [Oracle transaction, isolation, read consistency, lock, rollback, SCN]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ORACLE-0001]
source_ids: [SRC-000101]
acceptance_criteria: [Oracle transaction, read consistency, isolation, locking and commit/rollback behavior are covered]
---
# Oracle Transactions and Isolation

Oracle transaction boundary, read consistency, isolation, lock wait, commit/rollback és session behavior legyen explicit. A long-running transaction undo/retention és concurrency impactot okozhat; external callt ne tarts nyitott transactionben.

Serialization/deadlock vagy timeout esetén bounded retry csak idempotent operationre. Validate-old business invariantot, lock/wait graphot és commit outcome-ot; session state és autonomous transaction semantics release-specific lehet.

## Forrás
- [Oracle Database Documentation](https://docs.oracle.com/en/database/oracle/oracle-database/)
