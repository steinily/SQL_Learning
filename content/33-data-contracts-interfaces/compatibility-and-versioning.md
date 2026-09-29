---
schema_version: 1
id: DBKB-CONTRACT-0006
title: Compatibility and Versioning
type: playbook
primary_domain: data-contracts
secondary_domains: [integration, governance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openapi, asyncapi, cloudevents]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CONTRACT-0005]
related: [DBKB-MIG-0001]
aliases: [contract evolution]
search_keywords: [backward compatibility, forward compatibility, versioning, deprecation]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CONTRACT-0001]
source_ids: [SRC-000095, SRC-000096, SRC-000097]
acceptance_criteria: [Compatibility classes, expand-contract, version policy and deprecation are actionable]
---
# Compatibility and Versioning

Backward compatibility azt jelenti, hogy a régi consumer működik az új producerrel; forward compatibility ennek fordított iránya. A policy legyen field-, message-, endpoint- és semantic szinten explicit, mert egy syntax-valid schema change is lehet business-breaking.

Expand-contract: add optional field/operation, dual-read vagy dual-publish, consumer migration, majd old shape deprecation és removal. A version marker, sunset date, owner, impact analysis és rollback path legyen kötelező.

## Források
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [CloudEvents](https://cloudevents.io/)
