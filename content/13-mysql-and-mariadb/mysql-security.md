---
schema_version: 1
id: DBKB-MY-0005
title: MySQL Security
type: concept
primary_domain: mysql-mariadb
secondary_domains: [security]
levels: [advanced]
status: verified
maturity: complete
verification: fully-verified
publish: true
technologies: [mysql, mariadb]
sql_dialects: [mysql, mariadb]
scope: cross-vendor
prerequisites: [DBKB-MY-0004]
related: [DBKB-MY-0006]
aliases: [MySQL accounts and privileges]
search_keywords: [MySQL security, account, privilege, GRANT, TLS]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-MY-0001]
source_ids: [SRC-000046, SRC-000047]
acceptance_criteria: [Account, authentication plugin, privilege, role és TLS rétegeit adja]
---
# MySQL Security

MySQL security account identityből, authentication pluginből, role/privilege grantokból, network policyből és TLS-ből épül fel. `GRANT` scope, wildcard host, anonymous account és admin privilege least-privilege reviewt igényel.

## Források
- [MySQL 8.4 — Security](https://dev.mysql.com/doc/refman/8.4/en/security.html)
