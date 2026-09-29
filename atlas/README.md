# Atlas Manufacturing Demo Ecosystem

Atlas Manufacturing is a wholly synthetic manufacturing domain used consistently across the knowledge base.

## Rules

- No real PII or production data.
- Fixed seeds for generated datasets.
- Schema, data and fixtures are versioned.
- New entities require a documented teaching use.
- Impossible constrained states belong in raw/staging/dirty fixtures, not the canonical constrained dataset.

## Planned datasets

- atlas-tiny — manual examples
- atlas-small — exercises
- atlas-medium — performance and integration
- atlas-large — generated advanced-performance dataset
- atlas-dirty — deliberate data-quality problems

## Planned areas

Organization, customers, suppliers, products, materials, BOM, sales, purchasing, inventory, production, machines, quality, shipping, employees and audit.

## Planned analytical projection

Dimensions: customer, product, supplier, date, machine, plant.  
Facts: sales, production, inventory, quality, shipments.

## Planned event families

order.created, order.updated, production.started, production.completed, inventory.received, inventory.consumed, quality.failed, shipment.created and shipment.delivered.

## Implemented V1 slice

The versioned `v1/` tree implements the tiny organization/customer/product/order slice.
`fixtures/atlas-tiny.sql` is deterministic and constrained; deliberate quality defects are
isolated under `dirty/`. Run `.venv/bin/python scripts/atlas_validate.py` to execute the
fixture, foreign-key checks and stable assertions in an in-memory SQLite environment.
