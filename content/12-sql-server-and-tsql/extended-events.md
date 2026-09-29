---
schema_version: 1
id: DBKB-SS-0031
title: Extended Events
type: technology
primary_domain: sql-server
secondary_domains: [observability]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0026]
related: [DBKB-SS-0032]
aliases: [XEvent]
search_keywords: [Extended Events, XEvent session, event target]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [Event/session/target, filtering, overhead és retention trade-offot adja]
---
# Extended Events

Extended Events session eventeket, actions-t és targeteket rögzít célzott filteringgel. Session designnál overhead, dropped events, sensitive payload, retention és correlation ID legyen kontrollált.

## Források
- [Microsoft Learn — Extended Events](https://learn.microsoft.com/sql/relational-databases/extended-events/extended-events)
