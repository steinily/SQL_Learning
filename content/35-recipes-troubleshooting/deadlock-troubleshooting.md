---
schema_version: 1
id: DBKB-REC-0029
title: Deadlock Troubleshooting
type: troubleshooting
primary_domain: recipes
secondary_domains: [transactions, reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-REC-0028]
related: [DBKB-TX-0001]
aliases: [deadlock runbook]
search_keywords: [deadlock, lock graph, victim transaction, retry, lock order]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Deadlock graph collection, safe retry, root cause and prevention are described]
---
# Deadlock Troubleshooting

Őrizd meg a deadlock graphot, victim/owner statementet, resource sequence-t, transaction isolationt és timestampot. A retry csak idempotent vagy safely replayable műveletnél használható, bounded attempts és jitter mellett.

Root cause tipikusan inconsistent lock order, túl széles transaction, hiányzó index vagy external call a transactionben. Fix után stress/reproduction teszt, deadlock rate és business invariant validation szükséges.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
