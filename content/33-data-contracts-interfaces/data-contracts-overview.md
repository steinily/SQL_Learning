---
schema_version: 1
id: DBKB-CONTRACT-0001
title: Data Contracts Overview
type: overview
primary_domain: data-contracts
secondary_domains: [data-integration, governance]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openapi, asyncapi, cloudevents]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-DARCH-0001]
related: []
aliases: [data interface contract]
search_keywords: [data contract, API contract, schema, producer, consumer, compatibility]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CONTRACT-0001]
source_ids: [SRC-000095, SRC-000096, SRC-000097]
acceptance_criteria: [Contract purpose, producer/consumer obligations, schema, quality, compatibility and ownership are introduced]
---
# Data Contracts Overview

Data contract producer és consumer közötti explicit interface: schema, semantics, examples, quality/freshness SLO, security classification, versioning, compatibility, ownership és deprecation policy. A YAML/JSON file önmagában nem contract enforcement.

HTTP API-hoz OpenAPI, message-driven interface-hez AsyncAPI, event contexthez CloudEvents használható; ezek kombinálhatók, de a tooling és runtime binding korlátait dokumentáld. Contract change csak consumer impact analysis és validáció után publikálható.

## Források
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [CloudEvents](https://cloudevents.io/)
