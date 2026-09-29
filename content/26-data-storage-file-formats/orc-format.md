---
schema_version: 1
id: DBKB-STOR-0005
title: ORC Format
type: technology
primary_domain: data-storage
secondary_domains: [performance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-orc]
sql_dialects: [postgresql, tsql, mysql]
scope: vendor-specific
prerequisites: [DBKB-STOR-0002]
related: []
aliases: [Apache ORC]
search_keywords: [ORC, stripe, index, bloom filter, compression]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-STOR-0001]
source_ids: [SRC-000074]
acceptance_criteria: [ORC stripes, indexes, compression and reader compatibility are scoped]
---
# ORC Format

ORC stripe, index, bloom filter, encoding és compression struktúrája analytical scan és predicate filtering optimalizálására szolgálhat. Writer/reader engine support, schema evolution, ACID/table integration és compaction target implementationen validálandó, nem formatnév alapján feltételezhető.

## Források
- [Apache ORC Documentation](https://orc.apache.org/docs/)
