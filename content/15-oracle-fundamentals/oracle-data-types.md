---
schema_version: 1
id: DBKB-ORA-0003
title: Oracle Data Types
type: concept
primary_domain: oracle
secondary_domains: [data-modeling, sql]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [oracle-database]
sql_dialects: [oracle-sql]
scope: vendor-specific
prerequisites: [DBKB-ORA-0002]
related: [DBKB-MODL-0001]
aliases: [Oracle types]
search_keywords: [Oracle NUMBER, VARCHAR2, DATE, TIMESTAMP, CLOB, JSON]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ORACLE-0001]
source_ids: [SRC-000101]
acceptance_criteria: [Oracle type selection, precision, temporal, large object and conversion risks are covered]
---
# Oracle Data Types

Type választásnál precision/scale, character semantics, timezone, nullability, LOB/storage, JSON support és index/query behavior számít. Implicit conversion vagy NLS-dependent literal eredmény- és performance regressziót okozhat.

Contractban rögzítsd unit/timezone/encoding/precision jelentést és validációt. Type change migration előtt profile-old existing values, overflow/truncation/null impactot és rollbacket.

## Forrás
- [Oracle Database Documentation](https://docs.oracle.com/en/database/oracle/oracle-database/)
