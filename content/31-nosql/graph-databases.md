---
schema_version: 1
id: DBKB-NOSQL-0005
title: Graph Databases
type: technology
primary_domain: nosql
secondary_domains: [data-modeling, analytics]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [mongodb]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-NOSQL-0004]
related: [DBKB-MODL-0001]
aliases: [property graph, graph store]
search_keywords: [graph database, vertex, edge, traversal, relationship]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-NOSQL-0001]
source_ids: [SRC-000089]
acceptance_criteria: [Nodes/edges, traversal workload and graph-vs-document selection are explained]
---
# Graph Databases

Graph data modelben a node/vertex és edge/relationship az elsődleges; a traversal depth, direction, cardinality és path query határozza meg a workloadot. Válaszd graph store-t, ha a relationship traversal a core access pattern, nem pusztán azért, mert entity-k között van kapcsolat.

MongoDB dokumentációja graph-like workloadokhoz is ad modellezési és aggregation capability-ket, de a graph semantics és index behavior konkrét release-hez kötött. Definiáld a cycle, duplicate edge, deletion és authorization szabályokat.

## Forrás
- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
