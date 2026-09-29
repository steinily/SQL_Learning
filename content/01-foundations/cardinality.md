---
schema_version: 1
id: DBKB-FND-0021
title: Cardinality
type: concept
primary_domain: foundations
secondary_domains: [data-modeling, performance]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql]
scope: cross-vendor
prerequisites: [DBKB-FND-0009, DBKB-FND-0018]
related: [DBKB-FND-0022, DBKB-FND-0031]
aliases: [row count, relationship cardinality]
search_keywords: [one-to-many, estimate, distinct count, optimizer]
risk: safe
version_sensitive: true
review_cycle: on-major-release
research_packages: [RP-FND-0004]
source_ids: [SRC-000015]
acceptance_criteria:
  - Elkülöníti a set, relation, result és relationship cardinality jelentést.
  - Bemutatja az actual és estimated cardinality különbségét.
  - Kapcsolja a fogalmat a selectivityhez.
---
# Cardinality

A **cardinality** általánosan elemszám. Database contextben több, egymással rokon jelentése van:

- relation/table cardinality: row-k száma;
- query result cardinality: visszaadott row-k száma;
- column cardinality: gyakran distinct value-k száma;
- relationship cardinality: one-to-one, one-to-many vagy many-to-many részvétel.

Mindig nevezd meg, melyikről beszélsz. A „high-cardinality column” distinct-value értelme nem
azonos a table nagy row countjával.

## Actual és estimate

Az **actual cardinality** futáskor megfigyelt row count. Az optimizer **estimated cardinalityt**
számol statistics és feltételezések alapján. PostgreSQL 18 row-estimation példái a relation
cardinality és predicate selectivity szorzatával mutatják be az estimated rows képzését.

Hibás estimate rossz join orderhez, memory allocationhöz vagy scan választáshoz vezethet. Oka
lehet elavult statistics, correlated column, skew, expression vagy parameter uncertainty.

## Modeling cardinality

A conceptual relationship minimum/maximum részvételt ad. A physical schema ezt `NOT NULL`,
`UNIQUE`, foreign key és junction table kombinációjával közelíti. Nem minden minimum
cardinality védhető egyszerű row-local constrainttel; „minden parentnek legalább egy child”
transaction és lifecycle kérdés is.

## Mérési szabály

Performance elemzésben külön rögzítsd estimate és actual értéket ugyanahhoz a plan node-hoz,
azonos parameter/dataset mellett. Egyetlen futás nem univerzális workload bizonyíték.

## Forrás

- [PostgreSQL 18 — Row Estimation Examples](https://www.postgresql.org/docs/18/row-estimation-examples.html)
