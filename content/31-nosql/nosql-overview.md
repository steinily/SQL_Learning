---
schema_version: 1
id: DBKB-NOSQL-0001
title: NoSQL Overview
type: overview
primary_domain: nosql
secondary_domains: [data-modeling, architecture]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, redis, apache-couchdb]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DDS-0001]
related: []
aliases: [non-relational database]
search_keywords: [NoSQL, document, key value, graph, wide column]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000089, SRC-000090, SRC-000091]
acceptance_criteria: [NoSQL data models and selection tradeoffs are introduced]
---
# NoSQL Overview

NoSQL olyan adatstore-ok gyűjtőneve, amelyek a relational table/SQL modelltől eltérő primary data modelre épülnek: key-value, document, wide-column vagy graph. A választást az access pattern, consistency, scale, query complexity, operational maturity és migration cost alapján végezd, ne pusztán popularity alapján.

Denormalization gyakran explicit read path optimalizálás, ezért a source-of-truth, duplicate update és schema evolution legyen dokumentálva. A vendor guarantee-eket mindig az adott release manualja szerint ellenőrizd.

## Források
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Redis Documentation](https://redis.io/docs/latest/)
- [Apache CouchDB Documentation](https://docs.couchdb.org/)
