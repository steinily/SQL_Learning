---
schema_version: 1
id: DBKB-SEC-0010
title: Data Masking and Tokenization
type: technology
primary_domain: security-privacy
secondary_domains: [privacy]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [postgresql, sql-server, mysql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-SEC-0012]
related: []
aliases: [sensitive data masking]
search_keywords: [masking, tokenization, pseudonymization, test data]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-SEC-0001]
source_ids: [SRC-000052]
acceptance_criteria: [Masking, tokenization and reversibility trade-offs are distinguished]
---
# Data Masking and Tokenization

Masking, tokenization és pseudonymization különböző protection model-ek; dokumentáld a reversibility-t, key/token vault ownership-et, joinability-t és residual disclosure risk-et. Non-production refresh során a masked outputot is ellenőrizd, mert indirect identifiers újraazonosítást tehetnek lehetővé.

## Források
- [EUR-Lex — GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
