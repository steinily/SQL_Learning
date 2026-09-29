---
schema_version: 1
id: DBKB-STOR-0007
title: JSON and Semi Structured Data
type: technology
primary_domain: data-storage
secondary_domains: [data-integration]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [json]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-STOR-0006]
related: []
aliases: [JSON data format]
search_keywords: [JSON, object, array, nested data, encoding]
risk: caution
version_sensitive: false
review_cycle: 6m
research_packages: [RP-STOR-0001]
source_ids: [SRC-000076]
acceptance_criteria: [JSON syntax, interoperability and schema/semantics caveats are explained]
---
# JSON and Semi Structured Data

JSON object/array/value szerkezetet és UTF-8 interoperabilityt definiál, de schema enforcement, field ordering, numeric precision, null/missing semantics és domain contract application-specific. Semi-structured storage előtt explicit schema discovery, validation, evolution és query cost policy kell.

## Források
- [RFC 8259 — JSON](https://www.rfc-editor.org/rfc/rfc8259)
