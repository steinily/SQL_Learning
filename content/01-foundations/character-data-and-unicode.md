---
schema_version: 1
id: DBKB-FND-0014
title: Character Data and Unicode
type: concept
primary_domain: foundations
secondary_domains: [sql, data-quality, internationalization]
levels: [beginner, intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [unicode, postgresql]
sql_dialects: [postgresql]
scope: cross-vendor
prerequisites: [DBKB-FND-0012]
related: [DBKB-FND-0033, DBKB-FND-0034]
aliases: [text, string, UTF-8, character set]
search_keywords: [Unicode, code point, grapheme, encoding, collation, normalization]
risk: caution
version_sensitive: true
review_cycle: on-major-release
research_packages: [RP-FND-0003]
source_ids: [SRC-000011, SRC-000012]
acceptance_criteria:
  - Elkülöníti a character, code point, encoding unit, grapheme és byte fogalmát.
  - Bemutatja az encoding, normalization és collation külön szerepét.
  - Nem állít univerzális length vagy comparison semanticsot.
---
# Character Data and Unicode

Text kezelésnél legalább öt réteg különül el: abstract **character**, Unicode **code point**,
encoding form/code unit, storage **byte**, és a felhasználó által egy jelnek érzékelt
**grapheme cluster**. Ezek száma nem feltétlenül azonos.

## Unicode és encoding

A Unicode Standard code pointokat rendel characterekhez és encoding formokat, például UTF-8,
UTF-16 és UTF-32 definiál. UTF-8 változó byte-számot használ; ezért character limit és byte
limit összekeverése truncationt vagy storage hibát okozhat.

Egy látható karakter több code pointból állhat combining mark miatt. Ugyanaz a megjelenés
canonically equivalent sequence-ekkel is reprezentálható. A normalization form egységesítheti
a representationt, de csak tudatos contract alapján; az eredeti byte sequence megőrzése más
követelmény lehet.

## Database character type

PostgreSQL 18-ban a `character varying(n)` limit karakterben, nem byte-ban értendő; a database
character set határozza meg, mi tárolható. A fixed-length `character(n)` blank-padding semanticsa
comparison meglepetést okozhat. Más engine type neve és Unicode támogatása eltérhet.

## Collation

Az encoding azt mondja meg, hogyan kódoljuk a textet. A **collation** sorting és comparison
szabályt ad, gyakran locale és version szerint. Case-insensitive comparison, accent handling és
Unicode normalization nem ugyanaz a feature. Index result és uniqueness is függhet collationtől.

## Biztonságos tervezés

- End-to-end deklaráld az encodinget file, protocol, client és database szinten.
- Boundary tesztben legyen több-byte character, combining sequence és emoji.
- Ne vágj stringet tetszőleges byte positionnél.
- Identifier, username és security-sensitive comparison előtt threat model kell; visually
  confusable characterek külön kockázatot jelentenek.
- Collation/version change után index rebuild vagy revalidation lehet szükséges a vendor
  előírása szerint.

## Források

- [Unicode 16.0 Core Specification](https://www.unicode.org/versions/Unicode16.0.0/core-spec/)
- [PostgreSQL 18 — Character Types](https://www.postgresql.org/docs/18/datatype-character.html)
