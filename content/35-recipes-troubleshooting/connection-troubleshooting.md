---
schema_version: 1
id: DBKB-REC-0030
title: Connection Troubleshooting
type: troubleshooting
primary_domain: recipes
secondary_domains: [operations, reliability]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-REC-0029]
related: [DBKB-OPS-0001]
aliases: [database connectivity runbook]
search_keywords: [connection pool, timeout, TLS, DNS, max connections]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001]
acceptance_criteria: [DNS/network/TLS/auth/pool/quota diagnosis and safe remediation are covered]
---
# Connection Troubleshooting

Rétegezd a diagnózist: DNS/routing, TCP/TLS, authentication/authorization, server listener, pool exhaustion, max connections, timeout és database health. Capture-old client/library versiont, endpointet, error code-ot és timestampot.

Containment: bounded pool, backoff/jitter, circuit breaker vagy traffic shed; ne növeld vakon a connection limitet. Verify-old recovery után leak, idle session, auth audit, latency és application retry storm hiányát.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
