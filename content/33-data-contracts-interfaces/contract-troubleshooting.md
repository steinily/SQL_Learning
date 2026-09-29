---
schema_version: 1
id: DBKB-CONTRACT-0011
title: Contract Troubleshooting
type: troubleshooting
primary_domain: data-contracts
secondary_domains: [integration, operations]
levels: [advanced]
status: verified
maturity: draft
verification: fully-verified
publish: true
technologies: [openapi, asyncapi, cloudevents]
sql_dialects: []
scope: cross-vendor
prerequisites: [DBKB-CONTRACT-0010]
related: [DBKB-INTG-0001]
aliases: [contract incident runbook]
search_keywords: [contract break, schema mismatch, consumer failure, event validation]
risk: production-critical
version_sensitive: true
review_cycle: 6m
research_packages: [RP-CONTRACT-0001]
source_ids: [SRC-000095, SRC-000096, SRC-000097]
acceptance_criteria: [Schema mismatch, compatibility failure, unknown event and security error paths are actionable]
---
# Contract Troubleshooting

**Schema mismatch:** rögzítsd contract revisiont, producer buildet, consumer versiont és failing payloadot; hasonlítsd össze a diffet a compatibility policy-val, majd állítsd meg a breaking publish-t.

**Unknown/duplicate event:** ellenőrizd `id`, `source`, `type`, replay/offset és deduplication state-et; ne törölj payloadot, amíg a ownership és recovery path nem tisztázott. **Auth/schema rejection:** különítsd el token/scope, content-type, validation és routing hibát, majd a vendor gateway/broker logjával reprodukáld.

## Források
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [CloudEvents](https://cloudevents.io/)
