---
schema_version: 1
id: DBKB-CONTRACT-0004
title: AsyncAPI Contracts
type: technology
primary_domain: data-contracts
secondary_domains: [streaming, integration]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [asyncapi]
sql_dialects: []
scope: vendor-specific
prerequisites: [DBKB-CONTRACT-0003]
related: [DBKB-STREAM-0001]
aliases: [event API contract]
search_keywords: [AsyncAPI, channel, operation, message, binding, broker]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CONTRACT-0001]
source_ids: [SRC-000096]
acceptance_criteria: [AsyncAPI channels, operations, messages, servers, bindings and delivery obligations are explained]
---
# AsyncAPI Contracts

AsyncAPI-ban a channel, operation/action, message, payload schema, server és protocol binding együtt adja az event interface-t. Contract része a key/partitioning, ordering scope, delivery semantics, retry, duplicate és replay behavior is, ha a platform ezeket vállalja.

A broker-specific bindinget külön versioneld a protocol-neutral message semantics-től. Consumer compatibility, dead-letter és schema evolution teszt legyen a publish gate; dokumentáció generálása nem bizonyítja a runtime enforcementet.

## Forrás
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
