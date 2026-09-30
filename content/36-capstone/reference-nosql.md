---
schema_version: 1
id: DBKB-CAP-0065
title: Reference NoSQL
type: reference
primary_domain: capstone
secondary_domains: [nosql, data-modeling]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, redis, apache-cassandra, apache-couchdb]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0064]
related: [DBKB-NOSQL-0001]
aliases: [NoSQL checklist]
search_keywords: [NoSQL reference, document, key value, partition, consistency, backup]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000086, SRC-000089, SRC-000090, SRC-000091]
acceptance_criteria: [Model, query, consistency, replication, security, migration and recovery checklist is provided]
---
# Reference NoSQL

Checklist: access pattern; aggregate/document/value; partition/shard; index; consistency/transaction; replication/conflict; TTL/retention; schema evolution; security; observability; backup/restore; migration/reconciliation.

Vendor behavior és defaults release-specific; feature or benchmark claimhez exact manual and actual evidence kell.

## Források
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Redis Documentation](https://redis.io/docs/latest/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache CouchDB Documentation](https://docs.couchdb.org/)
