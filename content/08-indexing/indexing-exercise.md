---
schema_version: 1
id: DBKB-IDX-0024
title: Indexing Exercise
type: exercise
primary_domain: indexing
secondary_domains: [practice]
levels: [intermediate]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [postgresql]
sql_dialects: [postgresql]
scope: vendor-specific
prerequisites: [DBKB-IDX-0003, DBKB-IDX-0010]
related: [DBKB-IDX-0023]
aliases: [index tuning lab]
search_keywords: [index exercise, EXPLAIN exercise]
risk: safe
version_sensitive: true
review_cycle: 12m
research_packages: [RP-IDX-0001]
source_ids: [SRC-000014]
acceptance_criteria: [EXPLAIN összehasonlítást és index trade-off elemzést gyakoroltat]
---
# Indexing Exercise

Válassz egy filter + ORDER BY queryt, mérd meg az index nélküli és indexelt tervet, majd dokumentáld a cost, actual rows, buffers és write impact különbségét. A lokális eredményt ne általánosítsd más datasetre.

## Források
- [PostgreSQL 18 — Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html)
