---
schema_version: 1
id: DBKB-ASQL-0018
title: Advanced JSON Querying
type: concept
primary_domain: advanced-sql
secondary_domains: [semi-structured-data]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-FND-0012]
related: [DBKB-ASQL-0019]
aliases: [json extraction, json path]
search_keywords: [json, jsonb, path, extraction, containment]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ASQL-0002]
source_ids: [SRC-000041]
acceptance_criteria:
  - Elkülöníti a JSON value és text extractiont.
  - Kezeli a missing path type és indexing kérdését.
  - SQLite-labelled extraction példát ad.
---
# Advanced JSON Querying

JSON querynél külön contract a document validity, path existence, JSON type és SQL target type.
PostgreSQL `json` és `jsonb` operatorai, SQL/JSON path feature-jei és SQLite JSON functionjei nem
azonos API-k; minden snippet dialect-labelled.

Text extraction után a numeric comparison előtt explicit cast és invalid-input policy kell. Missing
path és JSON `null` nem feltétlen azonos SQL `NULL` jelentés. Array expansion megváltoztatja a row
grain-t és megsokszorozhatja a source sort.

Containment és path predicate indexelhetősége operator-, type- és engine-specific. Plan evidence
nélkül ne állíts index usage-et. Gyakran használt, stabil attributum normalizált/generated columnba
emelése mérlegelendő constrainttel.

A `SQL-ASQL-0018` SQLite `json_extract` functionnel typed quantityt olvas és exact resultot ellenőriz;
nem igazolja PostgreSQL operator syntaxát.

## Források

- [PostgreSQL 18 — JSON Functions and Operators](https://www.postgresql.org/docs/18/functions-json.html)
