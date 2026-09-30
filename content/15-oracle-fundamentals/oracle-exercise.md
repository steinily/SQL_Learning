---
schema_version: 1
id: DBKB-ORA-0013
title: Oracle Exercise
type: exercise
primary_domain: oracle
secondary_domains: [sql, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [oracle-database]
sql_dialects: [oracle-sql]
scope: vendor-specific
prerequisites: [DBKB-ORA-0012]
related: []
aliases: [Oracle lab]
search_keywords: [Oracle lab, transaction, index, backup, plan]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ORACLE-0001]
source_ids: [SRC-000101]
acceptance_criteria: [Learner produces reproducible Oracle design and validation evidence]
---
# Oracle Exercise

Feladat: tervezz egy release- és edition-specifikus Oracle workloadot, definiálj transaction/index/backup és security döntéseket, majd készíts validation checklistet. A labot izolált, nem production környezetben futtasd.

Deliverables: assumptions; DDL/query sample; expected plan and transaction behavior; backup/restore test plan; security review; observed results with timestamps; deviations and rollback. Execution-verified státusz csak a tényleges futtatási artefactokkal adható.

## Forrás
- [Oracle Database Documentation](https://docs.oracle.com/en/database/oracle/oracle-database/)
