---
schema_version: 1
id: DBKB-CONTRACT-0003
title: OpenAPI Contracts
type: technology
primary_domain: data-contracts
secondary_domains: [api-design, integration]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openapi]
sql_dialects: []
scope: vendor-specific
prerequisites: [DBKB-CONTRACT-0002]
related: [DBKB-INTG-0001]
aliases: [OpenAPI interface]
search_keywords: [OpenAPI, path, operation, response, parameter, security scheme]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CONTRACT-0001]
source_ids: [SRC-000095]
acceptance_criteria: [OpenAPI paths, operations, schemas, responses, errors and security are treated as contract]
---
# OpenAPI Contracts

OpenAPI contractban a path/operation, parameter, requestBody, response, error shape, schema, server és security scheme együtt értelmezendő. Documentáld a idempotency key-t, paginationt, rate limitet, timeoutot és auth scope-ot is, ha runtime behavior része.

Breaking change például required field, response type vagy error semantics módosítása lehet; compatibility tool csak a specifikációban leírható részeket látja. Generated client/server outputot a tényleges runtime és integration test ellenőrizze.

## Forrás
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
