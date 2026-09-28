# Definition of Ready / Done

## Document Definition of Ready

A document may enter writing only when it has:
- manifest item and stable ID
- canonical-location decision
- document type and primary domain
- priority and intended levels
- prerequisites
- acceptance criteria
- research requirements
- validation requirements

## Document Definition of Done

Required:
- manifest acceptance criteria satisfied
- metadata valid
- canonical duplication checked
- content complete
- prerequisites and internal links resolved
- required sources present
- factual QA passed
- dialect review where applicable
- examples validated where applicable
- risk classification correct
- zero BLOCKER, CRITICAL and MAJOR findings

Conditional gates apply to SQL execution, performance, security, destructive operations and version-sensitive claims.

## Domain Definition of Done

- required manifest coverage 100%
- required P0 items complete
- required verification passed
- no required orphan documents
- no unresolved contradictions
- learning order valid
- domain index generated
- required examples/scenarios present

## Release Definition of Done

Release gates are deterministic and manifest-driven. At minimum:
- baseline required scope complete
- BLOCKER = 0
- CRITICAL = 0
- MAJOR = 0
- metadata errors = 0
- broken required internal links = 0
- unresolved contradictions = 0
- required tests PASS
- Docmost dry-run PASS when publishing is enabled
- release snapshot generated

Project Health score alone can never satisfy a release gate.
