---
schema_version: 1
id: DBKB-ORA-0014
title: Oracle Reference
type: reference
primary_domain: oracle
secondary_domains: [sql, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [oracle-database]
sql_dialects: [oracle-sql, plsql]
scope: vendor-specific
prerequisites: [DBKB-ORA-0013]
related: []
aliases: [Oracle documentation index]
search_keywords: [Oracle reference, SQL reference, PL/SQL reference, administration]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ORACLE-0001]
source_ids: [SRC-000101]
acceptance_criteria: [Official Oracle navigation and version caveat are explicit]
---
# Oracle Reference

Az Oracle Database Documentation a SQL Language Reference, PL/SQL Language Reference, Database Concepts, Administrator's Guide, Backup and Recovery, Security és Performance részekhez ad authoritative kiindulópontot.

Mindig a target database release dokumentációját válaszd; syntax, optimizer, licensing és feature availability eltérhet. A projektben rögzített source csak navigációs és verification anchor, nem helyettesíti a konkrét release manual ellenőrzését.

## Forrás
- [Oracle Database Documentation](https://docs.oracle.com/en/database/oracle/oracle-database/)
