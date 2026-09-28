# Docmost Publishing Contract

GitHub is canonical; Docmost is a read/search/navigation projection.

## Eligibility

New documents default to publish=false. Publishing requires complete maturity, valid metadata, required verification and zero blocking QA findings.

## Identity

Stable document ID is the synchronization key. Renames and moves must not become delete/create operations solely because a path changed.

## Operations

CREATE, UPDATE, MOVE, ARCHIVE, DELETE, NO_CHANGE.

ARCHIVE is preferred over DELETE. Bulk deletion requires explicit authorization/policy and must never be inferred silently.

## Dry run

Every significant synchronization produces a preview with operation counts and affected IDs before mutation.

## Integrity

Post-publish checks compare expected and actual page identity/content state. HTTP/API success alone is not sufficient.

## Drift

Manual Docmost changes create DRIFT_DETECTED. Drift must be surfaced rather than silently overwritten.

Docmost-specific limitations must be handled by the publishing adapter, not by weakening the canonical knowledge architecture.
