---
schema_version: 1
id: DBKB-FND-0033
title: Structured vs Semi-Structured Data
type: comparison
primary_domain: foundations
secondary_domains: [data-engineering, data-modeling]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [json, xml]
sql_dialects: []
scope: general
prerequisites: [DBKB-FND-0002, DBKB-FND-0005]
related: [DBKB-FND-0012, DBKB-FND-0032]
aliases: [structured data, semi-structured data, unstructured data]
search_keywords: [schema-on-write, schema-on-read, JSON, XML, nested]
risk: safe
version_sensitive: false
review_cycle: 24m
research_packages: [RP-FND-0004]
source_ids: [SRC-000020]
acceptance_criteria:
  - Structure és schema enforcement szerint hasonlít.
  - Elutasítja a semi-structured egyenlő schema-less tévedést.
  - Bemutatja az evolution és validation következményeket.
---
# Structured vs Semi-Structured Data

**Structured data** előre meghatározott, rendszeresen ismétlődő schema szerint szervezett,
például typed table. **Semi-structured data** önleíró tagokat, key-ket vagy nested structure-t
tartalmazhat, miközben a recordok shape-je részben változó; JSON és XML gyakori példa. A NIST
IR 8496 draft ugyanezeket a format family-ket használja data-classification kontextusban.

## Nem minőségi sorrend

A structured adat lehet hibás, a JSON pedig szigorú JSON Schema/contract szerint validált. A
különbség nem „jó vs rossz”, hanem structure és enforcement helye.

## Schema-on-write és schema-on-read

Schema-on-write ingestion előtt ellenőriz; gyors és kiszámítható consumer queryt adhat.
Schema-on-read később értelmez, rugalmasabb landinget enged, de a consumerre tolhat ambiguityt
és repeated validationt. Gyakran mindkettő kell: raw immutable landing és curated typed layer.

## Evolution

Új optional field általában könnyebb, de rename, type change vagy semantics change breaking
lehet. Version, compatibility rule, unknown-field policy és default handling szükséges. Nested
array flatteningnél grain és duplicate semantics külön döntés.

## Modeling döntés

JSON column hasznos aggregate payloadhoz, de ne rejtse el azt az attribute-ot, amelyre foreign
key, frequent predicate vagy strict uniqueness kell. A boundaryt access pattern és invariant
alapján válaszd.

## Forrás

- [NIST IR 8496 draft — Data Classification Concepts](https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8496.ipd.pdf)
