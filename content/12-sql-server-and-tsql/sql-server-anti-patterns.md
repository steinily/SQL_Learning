---
schema_version: 1
id: DBKB-SS-0034
title: SQL Server Anti-Patterns
type: troubleshooting
primary_domain: sql-server
secondary_domains: [governance]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlserver]
sql_dialects: [tsql]
scope: vendor-specific
prerequisites: [DBKB-SS-0033]
related: [DBKB-SS-0040]
aliases: [SQL Server operational anti-pattern]
search_keywords: [SQL Server anti-pattern, NOLOCK abuse, cursor, implicit conversion]
risk: production-critical
version_sensitive: false
review_cycle: 12m
research_packages: [RP-SS-0001]
source_ids: [SRC-000030]
acceptance_criteria: [NOLOCK abuse, cursor overuse, implicit conversion, untested backup anti-patternokat adja]
---
# SQL Server Anti-Patterns

Kerülendő a blanket `NOLOCK`, cursor set-based rewrite nélkül, implicit conversion indexelt predicate-en, sa/owner application access, unbounded Agent retry és restore test nélküli backup claim. Minden exceptionnek owner és expiry kell.

## Források
- [Microsoft Learn — SQL Server performance](https://learn.microsoft.com/sql/relational-databases/performance/monitor-and-tune-for-performance)
