---
schema_version: 1
id: DBKB-NOSQL-0007
title: Denormalization Patterns
type: technology
primary_domain: nosql
secondary_domains: [data-modeling, data-quality]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, apache-cassandra]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-NOSQL-0006]
related: [DBKB-NOSQL-0013, DBKB-NOSQL-0014]
aliases: [read model duplication]
search_keywords: [denormalization, materialized view, duplicate data, fan out]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000086, SRC-000089]
acceptance_criteria: [Embedding, duplication, fan-out updates and reconciliation risks are documented]
---
# Denormalization Patterns

Denormalization célja a gyakori read path egyszerűsítése, nem az adatintegritás feladása. Embed, duplicate projection vagy materialized read model előtt definiáld a source-of-truth-t, update ordert, backfillt és stale window-t.

Fan-out write esetén idempotent event vagy job, retry és reconciliation szükséges. Ha a child entity nagy vagy önálló lifecycle-lel bír, embedding helyett reference vagy külön projection lehet biztonságosabb.

## Források
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
