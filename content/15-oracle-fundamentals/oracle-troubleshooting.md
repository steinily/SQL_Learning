---
schema_version: 1
id: DBKB-ORA-0012
title: Oracle Troubleshooting
type: troubleshooting
primary_domain: oracle
secondary_domains: [operations, performance]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [oracle-database]
sql_dialects: [oracle-sql]
scope: vendor-specific
prerequisites: [DBKB-ORA-0011]
related: [DBKB-OPS-0001]
aliases: [Oracle incident troubleshooting]
search_keywords: [Oracle incident, alert log, wait event, blocking session, ORA error]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-ORACLE-0001]
source_ids: [SRC-000101]
acceptance_criteria: [Evidence-first triage, safety gates, escalation and closure are described]
---
# Oracle Troubleshooting

Incident triage során először impact, scope, start time és recent change rögzítendő; utána alert/diagnostic evidence, active sessions, waits, blocking és resource pressure vizsgálandó. Ne módosíts production state-ot hypothesis és rollback nélkül.

Decision path: contain impact; preserve evidence; test least-invasive hypothesis; apply approved mitigation; monitor recovery; document root cause, residual risk és follow-up. ORA error interpretation release-specific, ezért official docs hivatkozás szükséges.

## Forrás
- [Oracle Database Documentation](https://docs.oracle.com/en/database/oracle/oracle-database/)
