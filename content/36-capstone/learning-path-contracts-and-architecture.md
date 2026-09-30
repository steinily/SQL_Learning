---
schema_version: 1
id: DBKB-CAP-0084
title: Learning Path Contracts and Architecture
type: learning-path
primary_domain: capstone
secondary_domains: [data-contracts, data-architecture]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openapi, asyncapi, cloudevents, togaf, dcat]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CAP-0083]
related: [DBKB-CAP-0044, DBKB-CAP-0045]
aliases: [contracts architecture path]
search_keywords: [contract learning path, architecture, ADR, OpenAPI, AsyncAPI, governance]
risk: production-critical
version_sensitive: true
review_cycle: 12m
research_packages: [RP-CAPSTONE-0001]
source_ids: [SRC-000092, SRC-000093, SRC-000095, SRC-000096, SRC-000097]
acceptance_criteria: [Ordered contract/architecture path with interface, governance, security and transition milestones]
---
# Learning Path Contracts and Architecture

Sorrend: contract overview/schema → OpenAPI/AsyncAPI/CloudEvents → compatibility/testing → data product → architecture domains/ADR → governance/security → contract/architecture case/exercise/reference.

Exit criteria: versioned interface, consumer matrix, runtime validation, ADR, ownership, security, SLO, exception/expiry és transition evidence.

## Források
- [The Open Group TOGAF Standard](https://pubs.opengroup.org/togaf-standard/)
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [CloudEvents](https://cloudevents.io/)
