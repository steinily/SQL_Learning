---
schema_version: 1
id: DBKB-ORA-0010
title: Oracle High Availability
type: technology
primary_domain: oracle
secondary_domains: [reliability, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [oracle-database]
sql_dialects: [oracle-sql]
scope: vendor-specific
prerequisites: [DBKB-ORA-0009]
related: [DBKB-OPS-0001]
aliases: [Oracle HA]
search_keywords: [Oracle Data Guard, RAC, failover, switchover, availability]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ORACLE-0001]
source_ids: [SRC-000101]
acceptance_criteria: [HA topology, failover evidence, RPO/RTO and operational ownership are covered]
---
# Oracle High Availability

HA design a szolgáltatási RPO/RTO, failure domain és recovery ownership alapján válasszon Oracle capability-t. RAC, Data Guard és más opciók eltérő failure modelt, licensinget és üzemeltetési terhet jelentenek; a támogatást az adott release dokumentációja igazolja.

Gyakorlat: define failure scenarios; execute approved switchover/failover drill; verify application reconnect, data protection és monitoring; record elapsed time and gaps; restore normal role. Drill nélkül a HA csak design claim.

## Forrás
- [Oracle Database Documentation](https://docs.oracle.com/en/database/oracle/oracle-database/)
