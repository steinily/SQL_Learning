---
schema_version: 1
id: DBKB-FND-0031
title: Database Workloads
type: concept
primary_domain: foundations
secondary_domains: [performance, architecture]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: []
sql_dialects: []
scope: general
prerequisites: [DBKB-FND-0003, DBKB-FND-0021, DBKB-FND-0030]
related: [DBKB-FND-0022, DBKB-FND-0032]
aliases: [workload profile, access pattern]
search_keywords: [latency, throughput, concurrency, read write ratio, query shape]
risk: caution
version_sensitive: false
review_cycle: 12m
research_packages: [RP-FND-0004]
source_ids: [SRC-000016, SRC-000017]
acceptance_criteria:
  - Meghatározza a workloadot mérhető operation-eloszlásként.
  - Felsorolja a capacity és correctness szempontokat.
  - Elutasítja az egyetlen átlagértékből levont univerzális következtetést.
---
# Database Workloads

A **database workload** az operationök, adatok, concurrency és időbeli eloszlás együttese.
Nem egyetlen QPS szám: ugyanaz a request rate egészen más terhelést adhat point lookup, bulk
write, large join vagy lock contention mellett.

## Leírandó dimenziók

- operation mix: read/insert/update/delete/DDL;
- query shape és result cardinality;
- transaction size, duration és isolation;
- concurrent session és burst pattern;
- data volume, growth, hot/cold distribution;
- latency percentile és throughput target;
- CPU, memory, I/O, network és log pressure;
- availability, durability és recovery requirement.

## Baseline és változás

Performance állítás csak declared environment, dataset és workload mellett értelmes. Average
latency elfedheti a tailt; ezért p50/p95/p99 és error/timeout együtt kellhet. Baseline után egy
változót módosíts, és execution plan/resource metric alapján hasonlíts.

## Mixed workload

Valós rendszerek gyakran vegyesek: OLTP mellett dashboard, batch reconciliation és maintenance
fut. A conflict időablak, resource governance és replica routing alapján kezelhető. A workload
elnevezés nem teszi automatikusan alkalmassá vagy alkalmatlanná az engine-t.

## Synthetic teszt korlátja

Synthetic benchmark reprodukálható, de csak a modellezett distributiont bizonyítja. Production
esetet vagy univerzális gyorsaságot nem szabad belőle kitalálni. E KB minden benchmarkot
`MEASURED`, `SIMULATED` vagy `ILLUSTRATIVE` provenance-nel kezel.

## Források

- [Microsoft — OLTP](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-transaction-processing)
- [Microsoft — OLAP](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-analytical-processing)
