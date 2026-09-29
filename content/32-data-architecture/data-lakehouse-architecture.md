---
schema_version: 1
id: DBKB-DARCH-0008
title: Data Lakehouse Architecture
type: technology
primary_domain: data-architecture
secondary_domains: [data-warehousing, storage]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [dcat]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DARCH-0007]
related: [DBKB-WH-0001, DBKB-STOR-0001]
aliases: [lakehouse]
search_keywords: [lakehouse, object storage, table format, batch streaming, governance]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DARCH-0001]
source_ids: [SRC-000092, SRC-000093]
acceptance_criteria: [Lakehouse layers, table/catalog contract, quality, serving and governance are covered]
---
# Data Lakehouse Architecture

Lakehouse architecture durable object storage-t és table/catalog semantics-t kapcsol össze analytics és ML workloadokhoz. A designnak tisztáznia kell a raw/validated/curated boundary-t, schema/evolutiont, transaction/consistency supportot és serving pathot.

A data lake önmagában nem catalog, quality vagy governance. Dataset/distribution identity, lineage, access control, retention, compaction/optimization és cost policy legyen a platform contract része; streaming és batch freshness külön SLO-t kaphat.

## Források
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
- [W3C DCAT](https://www.w3.org/TR/vocab-dcat-3/)
