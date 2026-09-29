---
schema_version: 1
id: DBKB-ASQL-0022
title: Dynamic SQL Safety
type: concept
primary_domain: advanced-sql
secondary_domains: [security]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-SQL-0002]
related: [DBKB-SQL-0011]
aliases: [dynamic command execution]
search_keywords: [dynamic sql, injection, parameter, identifier, quote_ident]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ASQL-0003]
source_ids: [SRC-000045]
acceptance_criteria:
  - Elkülöníti a bindolható value-t a dinamikus identifiertől.
  - Allowlist és safe quoting policyt ír elő.
  - Nem futtat mesterséges security execution példát.
---
# Dynamic SQL Safety

Dynamic SQL csak akkor indokolt, ha statement shape vagy identifier runtime változik. **Value-t**
parameterként kell bindolni; table/column **identifier** rendszerint nem bind parameter, ezért szűk
allowlistből és dialect-helyes identifier quotinggal állítható elő.

String escaping nem helyettesíti a parameter bindingot. A teljes identifier allowlist tartalmazza a
schema-t, objectet, columnokat, sort directiont és optional clause-okat. User inputból érkező SQL
fragment tiltott.

PostgreSQL PL/pgSQL `EXECUTE` command textet futtat, `USING` parameter value-kat ad át; identifierhez
`format` megfelelő specifierrel vagy documented quoting function kell. Privilege context, search path,
logging és error redaction szintén security boundary.

Ez a topic source-verified. A local SQLite harness nem modellezi PostgreSQL PL/pgSQL privilege és
injection környezetét, ezért execution `N/A`, nem hamis PASS.

## Források

- [PostgreSQL 18 — PL/pgSQL Statements](https://www.postgresql.org/docs/18/plpgsql-statements.html)
