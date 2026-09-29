---
schema_version: 1
id: DBKB-FND-0032
title: Database Warehouse Lake and Lakehouse
type: comparison
primary_domain: foundations
secondary_domains: [data-architecture, analytics]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [microsoft-fabric]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-FND-0003, DBKB-FND-0030, DBKB-FND-0031]
related: [DBKB-FND-0033]
aliases: [data warehouse, data lake, lakehouse]
search_keywords: [operational database, analytics, object storage, governance, open format]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-FND-0004]
source_ids: [SRC-000017, SRC-000019]
acceptance_criteria:
  - Fogalmi cél és workload szerint hasonlítja össze a platformtípusokat.
  - Jelzi, hogy a vendor elnevezések és határok átfedhetnek.
  - Bemutatja a governance és data movement következményeket.
---
# Database Warehouse Lake and Lakehouse

Ezek az elnevezések eltérő primary workloadot és governance modellt hangsúlyoznak; nem
szabványos, kölcsönösen kizáró product kategóriák.

## Operational database

Application state-et szolgál ki rövid transactionökkel és aktuális integrityvel. Gyakran
source rendszer, de nem automatikusan enterprise system of record minden adathoz.

## Data warehouse

Integrált, curated analytical adatot és governed schema/semantic réteget kínál. Complex SQL,
BI és repeatable metric szolgálata a cél. Adat betöltése ETL/ELT latencyt és reconciliationt
hoz.

## Data lake

Object/file storage köré szervezett, többféle structured, semi-structured vagy binary adatot
őrizhet. Flexibility és olcsó scale mellett catalog, quality, small-file kezelés és access
governance nélkül „data swamp” kockázat van.

## Lakehouse

Lake storage/open file format fölé table metadata, transaction, schema, governance és warehouse-
szerű query capabilityt adó architecture family. Microsoft Fabric current dokumentációja a
Lakehouse-t lake flexibility és warehouse capability kombinációjaként pozicionálja; ez vendor
implementation példa.

## Döntési szempontok

- operation és latency/freshness target;
- data format és update pattern;
- transaction/consistency scope;
- BI, ML és exploration consumer;
- catalog, lineage, security és retention;
- portability és proprietary service dependency;
- data movement, duplicate copy és egress cost.

Egy organization mindegyiket használhatja, de minden másolatnál legyen ownership, freshness és
reconciliation contract.

## Források

- [Microsoft — Online Analytical Processing](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-analytical-processing)
- [Microsoft Fabric — Data storage options](https://learn.microsoft.com/en-us/fabric/fundamentals/store-data)
