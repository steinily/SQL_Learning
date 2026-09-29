---
schema_version: 1
id: DBKB-PG-0016
title: Functions and Procedures
type: concept
primary_domain: postgresql
secondary_domains: [programming]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-PG-0015]
related: [DBKB-PG-0017]
aliases: [CREATE FUNCTION, CREATE PROCEDURE]
search_keywords: [PostgreSQL function, procedure, volatility, security definer]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-PG-0001]
source_ids: [SRC-000014]
acceptance_criteria: [Function/procedure transaction és volatility/security különbségét leírja]
---
# Functions and Procedures

Function queryból hívható value-returning routine; procedure `CALL`-lal hívható és eltérő transaction control lehetőségei vannak. Volatility, `SECURITY DEFINER`, search path és ownership security-sensitive contract.

## Források
- [PostgreSQL 18 — SQL Functions](https://www.postgresql.org/docs/18/xfunc-sql.html)
