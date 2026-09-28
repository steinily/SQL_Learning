# Governance Policies

## Source hierarchy

- S1: official/primary documentation, specifications, standards, release notes.
- S2: authoritative secondary sources such as academic work, recognized books and vendor engineering material.
- S3: reputable technical secondary sources.
- S4: community sources. Useful for discovery and operational experience, but not sole evidence for critical claims when stronger evidence exists.

## Evidence levels

- E1 Normal: authoritative references at document level.
- E2 Explicit: claim-level evidence for version-sensitive, security-sensitive, limits/defaults and non-obvious behavior.
- E3 Reproduction preferred: behavior/performance claims that can be demonstrated experimentally.

## Verification

Detailed dimensions are tracked separately: content, sources, facts, syntax, execution, expected results, dialects, metadata and links.

Allowed summary states:
- unverified
- source-verified
- syntax-verified
- execution-verified
- fully-verified

A summary state cannot imply checks that did not run.

## QA severity

BLOCKER, CRITICAL, MAJOR, MINOR, INFO.

VERIFIED requires zero BLOCKER, CRITICAL and MAJOR findings.

## Uncertainty quarantine

Use VERIFY_REQUIRED, SOURCE_CONFLICT, EXECUTION_NOT_TESTED or VERSION_UNCONFIRMED instead of guessing.

## Scope control

New topics enter DISCOVERED and are classified by architecture review as V1_REQUIRED, V1_OPTIONAL, BACKLOG or REJECTED. Automation cannot directly enlarge the V1 baseline.

## Rework

Maximum normal automated rework cycles: 3. Then escalate to HUMAN_REVIEW_REQUIRED.

## Publishing

New documents are non-publishable by default. Publication requires valid metadata, complete maturity, required validation and zero blocking QA findings. Deletion is never inferred from a missing file during normal sync; archive is preferred.

## Performance claims

Record engine/version, dataset/workload and evidence. Wall-clock numbers are environment-specific. Universal faster/slower claims require exceptional evidence.

## Synthetic content

Atlas data is synthetic. Synthetic case studies and simulated/illustrative benchmarks must be labelled.
