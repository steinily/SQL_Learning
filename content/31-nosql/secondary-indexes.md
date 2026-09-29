---
schema_version: 1
id: DBKB-NOSQL-0008
title: Secondary Indexes
type: technology
primary_domain: nosql
secondary_domains: [performance, data-modeling]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb, apache-cassandra]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-NOSQL-0007]
related: [DBKB-IDX-0001]
aliases: [NoSQL index]
search_keywords: [secondary index, index selectivity, multikey index, query plan]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000086, SRC-000089]
acceptance_criteria: [Index selectivity, write cost, cardinality and query-plan validation are covered]
---
# Secondary Indexes

Secondary index javítja a nem-primary lookupot, de write amplificationet, storage costot és maintenance terhet ad. Mérd a selectivity-t, cardinality-t, hot partition risket és index build/rebuild hatását a foreground workloadra.

MongoDB-ben explain outputtal, Cassandra-ban pedig a product-supported access pattern szerint ellenőrizd, hogy a query valóban bounded és routingolható. Indexet ne adj hozzá csak azért, hogy egy rossz partition key-t elfedj.

## Források
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
