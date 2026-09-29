---
schema_version: 1
id: DBKB-FND-0008
title: Database Keys
type: concept
primary_domain: foundations
secondary_domains: [data-modeling, sql]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-FND-0006, DBKB-FND-0007]
related: [DBKB-FND-0009, DBKB-FND-0010, DBKB-FND-0011]
aliases: [primary key, candidate key, alternate key, foreign key, composite key]
search_keywords: [identity, uniqueness, natural key, surrogate key]
risk: safe
version_sensitive: true
review_cycle: on-major-release
research_packages: [RP-FND-0002]
source_ids: [SRC-000009, SRC-000023]
acceptance_criteria:
  - Elkülöníti a superkey, candidate, primary, alternate és foreign key fogalmát.
  - Megmagyarázza a natural és surrogate key trade-offot.
  - Nem azonosítja a key constraintet az indexszel.
---
# Database Keys

A **key** attribute-ok olyan készlete, amely row identityt vagy relationök közötti hivatkozást
fejez ki. A key logical contract; egy index lehet enforcement vagy access mechanizmus, de nem
ugyanaz a fogalom.

## Key típusok

- **Superkey:** bármely attribute-készlet, amely egyedileg azonosít; tartalmazhat fölösleges
  attribute-ot.
- **Candidate key:** minimális superkey: egyetlen attribute sem hagyható el az uniqueness
  elvesztése nélkül.
- **Primary key:** a candidate key-ek közül kijelölt fő identity.
- **Alternate key:** a többi candidate key, gyakran `UNIQUE NOT NULL` constrainttel.
- **Composite key:** több columnból álló key.
- **Foreign key:** referencing column-készlet, amely egy referenced candidate/unique keyhez
  kötődik.

PostgreSQL 18-ban a `PRIMARY KEY` unique és non-null értékeket követel, és enforcementhez
automatikusan unique indexet hoz létre. Ebből nem következik, hogy minden DBMS ugyanazt az
index típust vagy storage layoutot használja.

## Natural és surrogate key

A **natural key** a business domainből származik, például egy stabil szabványos kód. Előnye,
hogy jelentést hordoz és gyakran eleve rendelkezésre áll; kockázata, hogy változhat, hosszú
vagy érzékeny lehet.

A **surrogate key** rendszer által adott, üzleti jelentés nélküli identity. Keskeny és stabil
lehet, de önmagában nem védi a business duplicate-ot. Ha a `customer_id` surrogate, a valódi
business uniquenessre továbbra is külön constraint kell.

## Composite identity

```sql
CREATE TABLE sales_order_line (
    sales_order_id INTEGER NOT NULL,
    line_number INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    PRIMARY KEY (sales_order_id, line_number)
);
```

A column order része a concrete constraint és index megvalósításnak, de logical identityként
az attribute-pár együtt számít. Foreign key esetén a referencing columnok száma és kompatibilis
type-ja illeszkedjen.

## Key-választási kérdések

- Stabil marad-e az érték merge, import és organization change során?
- Lehet-e újrahasznosítani vagy átadni más entitynek?
- Tartalmaz-e PII-t, amely logokba és child table-ekbe terjedne?
- Offline vagy distributed producer tud-e collision nélkül ID-t képezni?
- A business uniqueness teljesen deklarálva van-e?

## Források

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
- [PostgreSQL 18 — Glossary](https://www.postgresql.org/docs/18/glossary.html)
