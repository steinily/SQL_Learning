---
schema_version: 1
id: DBKB-NOSQL-0016
title: NoSQL Security
type: technology
primary_domain: nosql
secondary_domains: [security, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, redis, apache-cassandra, apache-couchdb]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-NOSQL-0015]
related: [DBKB-SEC-0001]
aliases: [NoSQL access control]
search_keywords: [NoSQL security, authentication, authorization, TLS, encryption]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000086, SRC-000089, SRC-000090, SRC-000091]
acceptance_criteria: [Authentication, authorization, network security, encryption and audit controls are covered]
---
# NoSQL Security

NoSQL deploymentet ne hagyd public network boundary-n; használj TLS/mTLS-t, authenticationt, least-privilege authorizationt és secret rotationt. A default vagy anonymous access legyen tiltva, a admin és application identity legyen külön.

Auditáld a read/write/admin műveleteket, bulk exportot, replication/membership változást és configuration override-ot. Backup, snapshot és log is tartalmazhat sensitive data-t; encryption-at-rest, retention és redaction legyen ellenőrizhető.

## Források
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Redis Documentation](https://redis.io/docs/latest/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Apache CouchDB Documentation](https://docs.couchdb.org/)
