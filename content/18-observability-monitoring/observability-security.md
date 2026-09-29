---
schema_version: 1
id: DBKB-OBS-0018
title: Observability Security
type: technology
primary_domain: observability
secondary_domains: [security-privacy]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [opentelemetry, prometheus, postgresql]
sql_dialects: [postgresql, tsql, mysql]
scope: cross-vendor
prerequisites: [DBKB-SEC-0015]
related: []
aliases: [telemetry security]
search_keywords: [telemetry access, sensitive SQL, redaction, observability security]
risk: security-sensitive
version_sensitive: true
review_cycle: 6m
research_packages: [RP-OBS-0001]
source_ids: [SRC-000055, SRC-000050]
acceptance_criteria: [Telemetry data protection, access and redaction are covered]
---
# Observability Security

Telemetry személyes adatot, SQL textet, identifiers-t, host detailt és credential-adjacent contextet tartalmazhat. Attribute allow-list, redaction, encryption, access control, retention és exporter endpoint hardening szükséges; debug logginget ne hagyj unlimited production módban.

## Források
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/)
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
