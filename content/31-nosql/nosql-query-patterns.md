---
schema_version: 1
id: DBKB-NOSQL-0013
title: NoSQL Query Patterns
type: playbook
primary_domain: nosql
secondary_domains: [performance, data-modeling]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, redis, apache-cassandra, apache-couchdb]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-NOSQL-0012]
related: [DBKB-NOSQL-0006, DBKB-NOSQL-0008]
aliases: [NoSQL access path]
search_keywords: [query pattern, bounded query, pagination, projection, explain]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000086, SRC-000089, SRC-000090, SRC-000091]
acceptance_criteria: [Query contract, bounded pagination, routing and plan validation are defined]
---
# NoSQL Query Patterns

Minden queryhez rögzítsd a key/routing feltételt, expected cardinality-t, maximum page size-t, consistency igényt és timeoutot. A wildcard, unbounded scan vagy cross-shard fan-out legyen explicit exception, költség- és rate-limittel.

Production release előtt használj vendor explain/profile eszközt, representative cardinality-t és failure/load tesztet. Pagination esetén stable cursor és duplicate/missing item behavior kell; offset alapú lapozás distributed mutable data-n gyakran törékeny.

## Források
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Redis Documentation](https://redis.io/docs/latest/)
- [Apache CouchDB Documentation](https://docs.couchdb.org/)
