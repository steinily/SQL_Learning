-- Deliberately invalid staging-only rows. Never load this into the constrained canonical model.
CREATE TABLE dirty_customer_import (
    source_row INTEGER,
    customer_code TEXT,
    customer_name TEXT,
    country_code TEXT,
    issue TEXT
);

INSERT INTO dirty_customer_import VALUES
    (1, 'CUST-ALPHA', 'Alpha Components duplicate', 'HU', 'duplicate business key'),
    (2, NULL, 'Missing code customer', 'DE', 'missing required key'),
    (3, 'CUST-BAD', '', 'HUNGARY', 'empty name and invalid country-code shape');
