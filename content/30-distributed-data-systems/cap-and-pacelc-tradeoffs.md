---
schema_version: 1
id: DBKB-DDS-0007
title: CAP and PACELC Tradeoffs
type: concept
primary_domain: distributed-data-systems
secondary_domains: [architecture]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [apache-cassandra, etcd]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DDS-0006]
related: [DBKB-DDS-0005, DBKB-DDS-0015]
aliases: [availability consistency tradeoff]
search_keywords: [CAP, PACELC, partition tolerance, latency consistency]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-DDS-0001]
source_ids: [SRC-000086, SRC-000088]
acceptance_criteria: [CAP/PACELC is presented as a tradeoff model, not a vendor feature label]
---
# CAP and PACELC Tradeoffs

CAP/PACELC model segít a trade-off megfogalmazásában, de nem helyettesíti a konkrét API contractot. Partition alatt a consistency vagy availability preferencia határozza meg, milyen operation sikeres; partition hiányában latency és consistency közötti választás is számít.

Ne címkézd egy teljes terméket egyszerűen „CP” vagy „AP”-ként minden workloadra. Írd le az operationt, failure state-et, acknowledgementet, stale-read lehetőséget és recovery-t. Az etcd és Cassandra eltérő célokra és konfigurációs modellel készülnek.

## Források
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [etcd Documentation](https://etcd.io/docs/)
