---
schema_version: 1
id: DBKB-DDS-0006
title: Quorum and Tunable Consistency
type: technology
primary_domain: distributed-data-systems
secondary_domains: [architecture, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-cassandra]
sql_dialects: []
scope: vendor-specific
prerequisites: [DBKB-DDS-0005]
related: [DBKB-DDS-0004]
aliases: [read quorum, write quorum]
search_keywords: [quorum, consistency level, replica acknowledgement, tunable consistency]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-DDS-0001]
source_ids: [SRC-000086]
acceptance_criteria: [Quorum arithmetic, operation-level consistency choice and failure behavior are addressed]
---
# Quorum and Tunable Consistency

Quorum strategyban a read és write acknowledgement számát a replication factorhez viszonyítva választod. A cél, hogy a read/write intersection vagy a termék saját consistency guarantee-je megfeleljen az alkalmazási igénynek; a formula önmagában nem helyettesíti a vendor semantics ellenőrzését.

Operation-szinten rögzítsd a consistency levelt, timeoutot, retry policy-t és a degraded-mode viselkedést. A magasabb quorum növelheti a latency-t és csökkentheti a partition alatti availability-t; minden döntéshez failure test és SLO kell.

## Forrás
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
