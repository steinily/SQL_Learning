---
schema_version: 1
id: DBKB-ASQL-0010
title: Running Aggregates
type: concept
primary_domain: advanced-sql
secondary_domains: [analytics]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql, sqlite]
sql_dialects: [postgresql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-ASQL-0009]
related: [DBKB-ASQL-0011]
aliases: [cumulative aggregate, running total]
search_keywords: [running sum, cumulative total, window aggregate]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-ASQL-0001]
source_ids: [SRC-000039, SRC-000040]
acceptance_criteria:
  - Explicit frame-mel ad running aggregate-et.
  - Kezeli a tie és partition reset kérdését.
  - Futtatható cumulative sum példát ad.
---
# Running Aggregates

Running aggregate a partition elejétől az aktuális sorig számol. Explicit `ROWS` frame és total order
teszi deterministic row-by-row contracttá.

```sql
SUM(amount) OVER (
  PARTITION BY account_id
  ORDER BY event_time, event_id
  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) AS running_amount
```

Tie-breaker nélkül az azonos timestamp sorok sequence-e bizonytalan; default frame pedig peers miatt
ugyanazt a cumulative value-t adhatja több sorra. A helyes viselkedés a business questiontől függ.

Opening balance-t külön seed row vagy expression adhat; duplicate transaction és reversal kezelését
az input contractban oldd meg. Window total nem feltétlen ledger balance proof reconciliation nélkül.

A `SQL-ASQL-0010` accountonként resetelő exact cumulative összegeket validál SQLite-on.

## Források

- [PostgreSQL 18 — Window Functions](https://www.postgresql.org/docs/18/functions-window.html)
