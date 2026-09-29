---
schema_version: 1
id: DBKB-NOSQL-0014
title: Document Schema Evolution
type: playbook
primary_domain: nosql
secondary_domains: [data-modeling, migration]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, apache-couchdb]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-NOSQL-0013]
related: [DBKB-MIG-0001]
aliases: [NoSQL schema migration]
search_keywords: [schema evolution, backward compatibility, document migration, dual read]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000089, SRC-000091]
acceptance_criteria: [Expand/contract, version marker, backfill and rollback are covered]
---
# Document Schema Evolution

Document schema evolutionnél kezdd expand lépéssel: add new optional fieldet és dual-read támogatást, majd backfill után válts contractot; csak ezután távolítsd el a régi shape-et. A document version vagy schema marker segíti a mixed-version időszakot.

Backfill legyen idempotent, throttled és resumable. Ellenőrizd a validation rule-t, indexet, old/new reader parity-t és rollbacket; a silent field rename vagy újrahasznált identifier adatvesztést okozhat.

## Források
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Apache CouchDB Documentation](https://docs.couchdb.org/)
