---
schema_version: 1
id: DBKB-SQ-0001
title: SQLite Overview
type: overview
primary_domain: sqlite
secondary_domains: [embedded-database]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [sqlite]
sql_dialects: [sqlite]
scope: vendor-specific
prerequisites: [DBKB-MY-0030]
related: [DBKB-SQ-0002, DBKB-SQ-0013]
aliases: [SQLite embedded database]
search_keywords: [SQLite, embedded database, file database]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SQ-0001]
source_ids: [SRC-000048]
acceptance_criteria: [Embedded/file-based architecture, use case és client/server boundaryt összefoglalja]
---
# SQLite Overview

SQLite embedded, serverless database engine, amely egy database file-ban tárolhatja az állapotot. Ez egyszerű deploymentet ad, de multi-process concurrency, HA, auth és operational topology nem azonos client/server engine-ekkel.

## Források
- [SQLite Documentation](https://www.sqlite.org/docs.html)
