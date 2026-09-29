---
schema_version: 1
id: DBKB-NOSQL-0025
title: NoSQL Reference
type: reference
primary_domain: nosql
secondary_domains: [architecture, operations]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, redis, apache-cassandra, apache-couchdb]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-NOSQL-0024]
related: [DBKB-DDS-0001]
aliases: [NoSQL checklist]
search_keywords: [NoSQL reference, selection checklist, consistency, partitioning, recovery]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000086, SRC-000089, SRC-000090, SRC-000091]
acceptance_criteria: [A concise selection and production-readiness checklist is provided]
---
# NoSQL Reference

Selection checklist: data model és access pattern; partition/shard key; consistency/read-after-write; transaction scope; replication/failure domains; index and query plan; schema evolution; backup/restore RPO/RTO; security; observability; vendor/version constraints.

Go-live előtt legyen representative load/failure test, restore evidence, alert/runbook owner, migration rollback és reconciliation report. A termék feature matrixot mindig a linked official manual release-ével együtt használd.

## Források
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Redis Documentation](https://redis.io/docs/latest/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache CouchDB Documentation](https://docs.couchdb.org/)
