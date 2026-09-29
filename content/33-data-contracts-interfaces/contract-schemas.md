---
schema_version: 1
id: DBKB-CONTRACT-0002
title: Contract Schemas
type: concept
primary_domain: data-contracts
secondary_domains: [data-modeling, data-quality]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openapi, asyncapi, cloudevents]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CONTRACT-0001]
related: [DBKB-DQ-0001]
aliases: [schema contract]
search_keywords: [schema, required field, enum, format, semantic contract]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CONTRACT-0001]
source_ids: [SRC-000095, SRC-000096, SRC-000097]
acceptance_criteria: [Structural and semantic schema elements, examples and validation responsibilities are explained]
---
# Contract Schemas

Schema rögzíti a field name/type/requiredness/format/enum/constraints értékét, de a business semantics, units, timezone, null meaning, quality threshold és privacy classification is contract része.

Adj valid, invalid és edge-case examples-t. A producer validál publish előtt, a consumer pedig tolerant parsinggel és unknown-field policy-val kezelje a változást; a schema registry vagy linter csak akkor számít gate-nek, ha ténylegesen fut a pipeline-ban.

## Források
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [CloudEvents](https://cloudevents.io/)
