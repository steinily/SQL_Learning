---
schema_version: 1
id: DBKB-FND-0024
title: Data Integrity
type: concept
primary_domain: foundations
secondary_domains: [data-quality, database-engineering]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql]
scope: general
prerequisites: [DBKB-FND-0008, DBKB-FND-0010, DBKB-FND-0011]
related: [DBKB-FND-0025, DBKB-FND-0027]
aliases: [entity integrity, referential integrity, domain integrity]
search_keywords: [constraint, invariant, validation, consistency, quality]
risk: caution
version_sensitive: false
review_cycle: 12m
research_packages: [RP-FND-0002, RP-FND-0004]
source_ids: [SRC-000009]
acceptance_criteria:
  - Elkülöníti az entity, domain, referential és transactional integrityt.
  - Megmutatja a preventive és detective control szerepét.
  - Elválasztja az integrityt a tágabb data quality fogalomtól.
---
# Data Integrity

A **data integrity** annak tulajdonsága, hogy az adat a deklarált structure-t és invariantokat
megőrzi létrehozás, módosítás, concurrency, failure és movement során.

## Integrity rétegek

- **Entity integrity:** minden row azonosítható, nincs tiltott duplicate identity.
- **Domain integrity:** value type, range és business domain szabályainak megfelel.
- **Referential integrity:** relationship target létezik és lifecycle action szabályos.
- **Transactional integrity:** összetartozó változások boundaryn belül maradnak.
- **Cross-system integrity:** replica, pipeline vagy export nem veszít és nem duplikál csendben.

## Preventive és detective control

Constraint és transaction megelőzhet invalid state-et. Reconciliation, profiling és audit
detectálhat olyan hibát, amely external source-ból vagy régi rendszerből érkezett. A két control
nem helyettesíti egymást: csak detection mellett a hibás adat már consumerhez juthat; csak
prevention mellett az undeclared vagy cross-system hiba rejtve maradhat.

## Integrity és quality

Constraint-valid adat lehet pontatlan vagy elavult. Egy valid kétbetűs code nem bizonyítja, hogy
a customer tényleges országát jelöli. Az integrity a deklarált szabályhoz való megfelelés; data
quality tágabb, célhoz kötött dimenziókat is vizsgál.

## Ownership

Minden critical invarianthez legyen owner, enforcement location, monitoring és remediation.
Ugyanazt a szabályt több rétegben is ellenőrizhetjük, de a canonical enforcement és error
contract legyen egyértelmű.

## Forrás

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
