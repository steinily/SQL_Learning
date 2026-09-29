---
schema_version: 1
id: DBKB-FND-0023
title: Database Schema
type: concept
primary_domain: foundations
secondary_domains: [data-modeling, database-engineering]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-FND-0003, DBKB-FND-0007]
related: [DBKB-FND-0011, DBKB-FND-0024, DBKB-FND-0035]
aliases: [logical schema, SQL schema, namespace]
search_keywords: [catalog, namespace, DDL, object, search path]
risk: caution
version_sensitive: true
review_cycle: on-major-release
research_packages: [RP-FND-0004]
source_ids: [SRC-000023]
acceptance_criteria:
  - Elkülöníti a broad logical schema és vendor namespace jelentést.
  - Bemutatja a schema object, ownership és change szerepét.
  - Figyelmeztet a search-path és unqualified-name kockázatra.
---
# Database Schema

A **schema** tág értelemben az adat logical leírása: table-ek, columnok, type-ok, constraint-ek,
kapcsolatok és jelentések. SQL productban a szó konkrét namespace-t is jelenthet.

PostgreSQL 18 glossary szerint a schema olyan namespace, amelynek SQL objectjei ugyanabban a
database-ben vannak; tágabban egy database vagy részhalmazának data descriptionje. Más vendor
object hierarchyja eltérhet.

## Schema mint contract

A schema meghatározza, milyen input fogadható el és milyen outputot várhat consumer. DDL-en
túl comment, business definition, ownership, sensitivity és compatibility policy is része a
használható contractnak.

## Namespace

Qualified név például `sales.sales_order`. Namespace elkülönítheti module-ok vagy ownerök
objectjeit, de nem feltétlenül isolation boundary. Privilege és search path külön configuration.
Unqualified name feloldása search path alapján security és correctness kockázatot okozhat;
trusted objectnél explicit qualification indokolt.

## Schema evolution

Add/drop/rename/type change consumer impactot okozhat. Migration előtt dependency inventory,
backward compatibility, rollout order, data validation és rollback/roll-forward terv kell.
Schema version nem csak egy DDL file neve: az alkalmazott state-et és historyt is követni kell.

## Forrás

- [PostgreSQL 18 — Glossary](https://www.postgresql.org/docs/18/glossary.html)
