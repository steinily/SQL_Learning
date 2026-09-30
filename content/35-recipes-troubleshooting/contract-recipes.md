---
schema_version: 1
id: DBKB-REC-0025
title: Contract Recipes
type: playbook
primary_domain: recipes
secondary_domains: [data-contracts, integration]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openapi, asyncapi, cloudevents]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-REC-0024]
related: [DBKB-CONTRACT-0001]
aliases: [API contract recipe]
search_keywords: [contract, schema, compatibility, consumer, deprecation, event]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000095, SRC-000096, SRC-000097]
acceptance_criteria: [Contract design, validation, compatibility, security, publication and rollback are actionable]
---
# Contract Recipes

Contract recipe rögzítse schema/semantic, examples, auth, quality/SLO, idempotency/order/replay, compatibility, owner, revision és sunset date értékét. Lint, schema validation, consumer test és runtime integration legyen publish gate.

Breaking change előtt impact analysis, dual-read/publish, migration guide, communication és rollback kell. CloudEvents `id/source/type`, OpenAPI operation/response és AsyncAPI channel/message binding ne csak dokumentációban szerepeljen: runtime mappinget is verify-old.

## Források
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [CloudEvents](https://cloudevents.io/)
