---
schema_version: 1
id: DBKB-CONTRACT-0008
title: Consumer-Driven Contracts
type: technology
primary_domain: data-contracts
secondary_domains: [integration, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openapi, asyncapi]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CONTRACT-0007]
related: [DBKB-INTG-0001]
aliases: [CDC contract]
search_keywords: [consumer driven contract, provider, consumer expectation, pact]
risk: production-critical
version_sensitive: false
review_cycle: 6m
research_packages: [RP-CONTRACT-0001]
source_ids: [SRC-000095, SRC-000096]
acceptance_criteria: [Consumer expectations, provider verification, ownership and conflict resolution are described]
---
# Consumer-Driven Contracts

Consumer-driven contractban a consumer deklarálja a ténylegesen használt fields, operations, events és error behavior elvárását; a provider ezt verifyolja. A shared contract registry kapcsolja a consumer versiont, provider buildet, statuszt és deprecation window-t.

CDC nem mentesít producer-wide invariant, security és load test alól. Consumer conflict esetén owner, priority, migration window és explicit decision kell; ne lazítsd a contractot egyetlen rosszul modellezett consumer miatt.

## Források
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
