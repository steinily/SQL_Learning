---
schema_version: 1
id: DBKB-CAP-0021
title: Contract Case Study
type: case-study
primary_domain: capstone
secondary_domains: [data-contracts, integration]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openapi, asyncapi, cloudevents]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0020]
related: [DBKB-CONTRACT-0001]
aliases: [contract case]
search_keywords: [OpenAPI, AsyncAPI, CloudEvents, compatibility, consumer]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000095, SRC-000096, SRC-000097]
acceptance_criteria: [Scenario requires HTTP/event contract, compatibility, security and deprecation decisions]
---
# Contract Case Study

Order API új required fieldet és event payload change-et vezetne be; három régi consumer működik. Készíts OpenAPI/AsyncAPI/CloudEvents contractot, compatibility matrixot, consumer-driven testet, security policy-t és deprecation plan-t.

Elvárt evidence: diff, valid/invalid examples, test output, consumer impact, dual-run, sunset és rollback. Runtime enforcementet csak ténylegesen futtatott validator/gateway outputtal állíts.

## Források
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [CloudEvents](https://cloudevents.io/)
