---
schema_version: 1
id: DBKB-ASQL-0019
title: JSON Construction and Aggregation
type: concept
primary_domain: advanced-sql
secondary_domains: [semi-structured-data, data-integration]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-ASQL-0018, DBKB-SQL-0013]
related: [DBKB-ISQL-0027]
aliases: [json aggregation]
search_keywords: [json object, json array, json aggregate, ordering]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ASQL-0002]
source_ids: [SRC-000041]
acceptance_criteria:
  - Bemutatja az object és array constructiont.
  - Deterministic array orderinget és duplicate-key policyt követel.
  - SQLite-labelled JSON object példát ad.
---
# JSON Construction and Aggregation

JSON construction relational row-kból objectet, több sorból arrayt vagy object aggregatet képez.
Output contracthoz rögzítsd a property neveket, null inclusiont, numeric/text type-ot és nestinget.

Aggregate array sorrendje csak explicit ordered input/aggregate syntax mellett stabil. Duplicate
object key kezelése function- és enginefüggő; silently last-wins behaviorre ne építs. One-to-many join
többszörözheti a nested itemeket, ezért előbb rögzítsd a child grain-t.

Nagy JSON payload memory és transfer risk; pagination/streaming vagy relational consumer interface
lehet jobb. JSON string concatenation helyett native constructor kell escaping és type correctness
miatt.

A `SQL-ASQL-0019` SQLite `json_object` kimenetét ellenőrzi canonical rövid fixture-rel. PostgreSQL
JSON aggregate behavior csak source-verified.

## Források

- [PostgreSQL 18 — JSON Functions and Operators](https://www.postgresql.org/docs/18/functions-json.html)
