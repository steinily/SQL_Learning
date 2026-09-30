---
schema_version: 1
id: DBKB-REC-0042
title: Transaction Anti-Patterns
type: error
primary_domain: recipes
secondary_domains: [transactions, reliability]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-REC-0041]
related: [DBKB-TX-0001]
aliases: [transaction mistakes]
search_keywords: [long transaction, deadlock, implicit transaction, retry storm]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001]
acceptance_criteria: [Transaction anti-patterns include evidence-based remediation]
---
# Transaction Anti-Patterns

Anti-pattern a túl hosszú vagy user interactiont tartó transaction, external API call nyitott transactionben, inconsistent lock order, implicit autocommit assumption, non-idempotent blind retry és huge unbounded batch.

Detectáld lock/wait, transaction age, rollback rate, deadlock, log growth és retry metrics alapján. Remediation: kisebb boundary, deterministic order, outbox/compensation, bounded retry és actual invariant test.

## Forrás
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
