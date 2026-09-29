---
schema_version: 1
id: DBKB-PG-0009
title: Date and Time Types
type: technology
primary_domain: postgresql
secondary_domains: [data-modeling]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0008]
related: [DBKB-PG-0012]
aliases: [timestamp, timestamptz]
search_keywords: [PostgreSQL date, timestamp, timestamptz, timezone]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [timestamp/time zone semantics, interval és timezone caveat-et ad]
---
# Date and Time Types

`timestamp with time zone` és `timestamp without time zone` eltérő üzleti szemantikát hordoz. A timezone, session setting, DST és serialization szabályokat explicit kezeld; wall-clock és instant ne legyen összekeverve.

## Források
- [PostgreSQL 18 — Date/Time Types](https://www.postgresql.org/docs/18/datatype-datetime.html)
