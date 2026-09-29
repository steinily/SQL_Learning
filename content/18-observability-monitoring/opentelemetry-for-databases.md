---
schema_version: 1
id: DBKB-OBS-0004
title: OpenTelemetry for Databases
type: technology
primary_domain: observability
secondary_domains: [integration]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [opentelemetry, postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-OBS-0002]
related: []
aliases: [OTel database instrumentation]
search_keywords: [OpenTelemetry, database spans, semantic conventions, collector]
risk: caution
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OBS-0001]
source_ids: [SRC-000055]
acceptance_criteria: [Instrumentation, context, attributes and privacy caveats are scoped]
---
# OpenTelemetry for Databases

OpenTelemetry instrumentation a database client spans, resource attributes és trace context segítségével kapcsolhatja össze az application requestet a database operationnel. SQL text, bind values és identifiers exportja adatvédelmi és cardinality kockázatot jelenthet, ezért redaction és attribute policy szükséges.

## Források
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/)
