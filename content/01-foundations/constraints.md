---
schema_version: 1
id: DBKB-FND-0011
title: Constraints
type: concept
primary_domain: foundations
secondary_domains: [data-modeling, sql]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [portable-sql, postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-FND-0007, DBKB-FND-0008, DBKB-FND-0010]
related: [DBKB-FND-0012, DBKB-FND-0016, DBKB-FND-0024]
aliases: [integrity constraint, CHECK, NOT NULL, UNIQUE]
search_keywords: [primary key, foreign key, domain rule, enforcement]
risk: caution
version_sensitive: true
review_cycle: on-major-release
research_packages: [RP-FND-0002]
source_ids: [SRC-000009]
acceptance_criteria:
  - Összehasonlítja a fő constraint típusokat és határaikat.
  - Elmagyarázza a NULL és CHECK kapcsolatát.
  - Tényleges expected-error tesztet kapcsol a dokumentumhoz.
---
# Constraints

A **constraint** deklarált szabály, amely leszűkíti a megengedett database state-eket. Az
adatbázishoz közel védi az invariantot, ezért minden write pathra érvényes, amely nem kerüli meg
az enforcementet.

## Alaptípusok

- `NOT NULL`: a column nem tartalmazhat `NULL` markert.
- `CHECK`: a row értékeire boolean feltételt ad.
- `UNIQUE`: a deklarált column-kombináció ismétlődését szabályozza.
- `PRIMARY KEY`: kijelölt unique, non-null row identity.
- `FOREIGN KEY`: referenced keyhez köti a referencing value-t.

```sql
CREATE TABLE product (
    product_id INTEGER PRIMARY KEY,
    sku VARCHAR(30) NOT NULL UNIQUE,
    list_price DECIMAL(12, 2) NOT NULL,
    discount_price DECIMAL(12, 2),
    CHECK (list_price >= 0),
    CHECK (discount_price IS NULL OR
           (discount_price >= 0 AND discount_price < list_price))
);
```

## CHECK és UNKNOWN

PostgreSQL 18-ban a `CHECK` akkor sérül, ha expressionje `FALSE`; `TRUE` vagy `NULL/UNKNOWN`
esetén elfogadott. Ezért `CHECK (price > 0)` nem helyettesíti a `NOT NULL` constraintet. A
nullabilityt explicit kezeld.

## Mit ne várj constrainttől?

A type és constraint nem ismeri a deklarálatlan business jelentést. A `VARCHAR(2)` nem
bizonyítja, hogy létező country code, a positive amount nem bizonyítja, hogy helyes invoice
összeg. Cross-row, temporal vagy external-system invarianthez más constraint, normalized model,
trigger vagy transaction-safe application protocol kellhet.

## Change és validation

Constraint hozzáadása existing data mellett data scan és blocking kockázatot okozhat. Egyes
engine-ek deferred vagy not-valid/not-enforced workflowt kínálnak; ezek syntaxa és guarantee-je
vendor/version-sensitive. Migration előtt külön mérd fel a régi violationöket, és ne nevezd
enforcednek a csupán dokumentáló szabályt.

A `SQL-FND-0006` valid és invalid ár insertet futtat; az invalid statement expected
`IntegrityError`, a valid row pedig változatlanul lekérdezhető. Ez actual execution evidence,
nem illusztratív PASS.

## Forrás

- [PostgreSQL 18 — Constraints](https://www.postgresql.org/docs/18/ddl-constraints.html)
