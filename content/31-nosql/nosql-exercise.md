---
schema_version: 1
id: DBKB-NOSQL-0024
title: NoSQL Exercise
type: exercise
primary_domain: nosql
secondary_domains: [data-modeling, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, redis, apache-cassandra, apache-couchdb]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-NOSQL-0023]
related: [DBKB-NOSQL-0013, DBKB-NOSQL-0015]
aliases: [NoSQL lab]
search_keywords: [NoSQL exercise, modeling lab, migration test, failure test]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000089, SRC-000090, SRC-000091]
acceptance_criteria: [Learner creates model, consistency, migration and recovery evidence]
---
# NoSQL Exercise

Válassz egy customer/profile workloadot és hasonlíts össze document, key-value és wide-column modellt.

1. Írd le az access patternöket, key/index választást, consistency és transaction boundary-t.
2. Tervezd meg a schema evolutiont, backup/restore-t és egy hot-key failure tesztet.
3. Készíts migration plan-t dual-run, reconciliation, cutover és rollback lépésekkel.

Elvárt eredmény: model decision matrix, sample schema, query evidence, failure matrix és runbook. Execution-verified státuszt csak tényleges futtatási output után használj.

## Források
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Redis Documentation](https://redis.io/docs/latest/)
- [Apache CouchDB Documentation](https://docs.couchdb.org/)
