---
schema_version: 1
id: DBKB-REC-0031
title: Replication Troubleshooting
type: troubleshooting
primary_domain: recipes
secondary_domains: [reliability, disaster-recovery]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, apache-cassandra]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-REC-0030]
related: [DBKB-DR-0001]
aliases: [replica lag runbook]
search_keywords: [replication lag, replica, WAL, binlog, quorum, failover]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000086]
acceptance_criteria: [Lag, connectivity, apply errors, conflict, failover and reconciliation are actionable]
---
# Replication Troubleshooting

Capture-old primary/replica identity, LSN/offset/timestamp, lag, apply error, network path, disk/IO and recent DDL/DML. Distinguish transport lag, apply lag, conflict, schema mismatch és quorum loss.

Ne promote-olj vakon; define-olj RPO, write fencing, failover owner és reconciliation. Repair/replay legyen version- és topology-aware, majd count/checksum/business invariant és read-after-write validation zárja.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
