---
schema_version: 1
id: DBKB-REC-0001
title: SQL Recipes Overview
type: overview
primary_domain: recipes
secondary_domains: [operations, sql]
levels: [intermediate]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql, sqlite]
sql_dialects: [postgresql, tsql, mysql, sqlite]
scope: cross-vendor
prerequisites: [DBKB-SQL-0001]
related: []
aliases: [database cookbook]
search_keywords: [SQL recipe, safe change, validation, rollback, runbook]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-RECIPES-0001]
source_ids: [SRC-000001, SRC-000086, SRC-000098]
acceptance_criteria: [Recipe structure, safety gates, evidence, dialect scope and rollback are introduced]
---
# SQL Recipes Overview

Minden recipe tartalmazza: cél, scope/dialect, prerequisites, read-only precheck, change vagy query, expected result, validation, rollback/abort, evidence és production risk. Destructive lépéshez explicit approval és backup/recovery boundary kell.

Recipe csak akkor execution-verified, ha ténylegesen lefuttattad a megadott környezetben; syntax-valid szöveg nem execution evidence. Dialect-specific commandot ne jelölj portable SQL-ként.

## Források
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [AWS Analytics Documentation](https://docs.aws.amazon.com/analytics/)
