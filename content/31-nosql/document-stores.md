---
schema_version: 1
id: DBKB-NOSQL-0003
title: Document Stores
type: technology
primary_domain: nosql
secondary_domains: [data-modeling, application-design]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, apache-couchdb]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-NOSQL-0002]
related: [DBKB-NOSQL-0014]
aliases: [JSON document database]
search_keywords: [document store, JSON document, embedded document, collection]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000089, SRC-000091]
acceptance_criteria: [Embedding, referencing, document identity and indexing are covered]
---
# Document Stores

Document store-ban az aggregate entity egy JSON-szerű document lehet, embedded subdocumentekkel vagy reference-ekkel. Embed akkor hasznos, ha a read/write lifecycle együtt mozog; reference kellhet shared, nagy vagy independently updated entity esetén.

A document shape, identifier, validation, index és size limit legyen versioned contract. MongoDB és CouchDB különböző query, replication és conflict semantics-et ad; a „JSON store” címke nem bizonyít kompatibilitást.

## Források
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Apache CouchDB Documentation](https://docs.couchdb.org/)
