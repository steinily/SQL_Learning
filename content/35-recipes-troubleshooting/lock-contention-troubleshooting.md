---
schema_version: 1
id: DBKB-REC-0028
title: Lock Contention Troubleshooting
type: troubleshooting
primary_domain: recipes
secondary_domains: [transactions, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-REC-0027]
related: [DBKB-TX-0001]
aliases: [lock wait diagnosis]
search_keywords: [lock wait, blocking session, transaction duration, timeout]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Blocking graph, transaction owner, safe mitigation and verification are covered]
---
# Lock Contention Troubleshooting

Capture blocker/waiter graph, transaction/session ID, lock mode/resource, age, query and application owner. Ne kill-elj automatikusan; előbb azonosítsd a commit/rollback safety-t, user impactot és retry behavior-t.

Containment: stop new work, reduce batch size, cancel safe waiter vagy approved blocker termination. Fix hosszú transaction, inconsistent lock order vagy missing index lehet; post-checkben verify-old lock wait, throughput és invariant állapotot.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
