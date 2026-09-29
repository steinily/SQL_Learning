---
schema_version: 1
id: DBKB-NOSQL-0015
title: NoSQL Backup and Restore
type: playbook
primary_domain: nosql
secondary_domains: [disaster-recovery, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, redis, apache-cassandra, apache-couchdb]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-NOSQL-0014]
related: [DBKB-DR-0001]
aliases: [NoSQL recovery]
search_keywords: [NoSQL backup, restore, point in time recovery, snapshot, RPO]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000086, SRC-000089, SRC-000090, SRC-000091]
acceptance_criteria: [Backup consistency, restore verification, RPO/RTO and evidence are defined]
---
# NoSQL Backup and Restore

Backup policy tartalmazza a consistency boundary-t, frequencyt, retentiont, encryptiont és RPO-t. Snapshot vagy export csak akkor használható recovery evidence-ként, ha restore-t izolált környezetben ténylegesen lefuttattad és az application invariantokat ellenőrizted.

Restore runbook: freeze vagy capture a write boundary-t, restore metadata/index/config state-et, replay szükséges logokat, majd count/checksum/domain reconciliationt futtass. RTO, lag és partial restore failure legyen mérhető; a replication nem helyettesíti a backupot.

## Források
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Redis Documentation](https://redis.io/docs/latest/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache CouchDB Documentation](https://docs.couchdb.org/)
