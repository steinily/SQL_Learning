---
schema_version: 1
id: DBKB-NOSQL-0018
title: NoSQL Troubleshooting
type: troubleshooting
primary_domain: nosql
secondary_domains: [operations, performance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, redis, apache-cassandra, apache-couchdb]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-NOSQL-0017]
related: [DBKB-OPS-0001]
aliases: [NoSQL incident runbook]
search_keywords: [NoSQL incident, slow query, replica lag, hot key, conflict]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000086, SRC-000089, SRC-000090, SRC-000091]
acceptance_criteria: [Common symptoms map to evidence, safe mitigation and verification]
---
# NoSQL Troubleshooting

**Slow query:** capture query shape, routing key, cardinality, explain/profile és node-level saturation; indexet vagy timeoutot ne módosíts vakon. **Hot key/partition:** azonosítsd a skew-t, throttle-olj és tervezz key migrationt.

**Replica lag/conflict:** hasonlítsd össze timestamps/versions/offsets, állítsd meg a veszélyes write path-ot, majd vendor-supported repair vagy reconciliation után nyisd vissza. Minden remediation előtt készíts snapshotot és incident evidence-et.

## Források
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Redis Documentation](https://redis.io/docs/latest/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache CouchDB Documentation](https://docs.couchdb.org/)
