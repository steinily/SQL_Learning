INSERT INTO organization VALUES (1, 'ATLAS-HU', 'Atlas Manufacturing Hungary');

INSERT INTO customer VALUES
    (101, 1, 'CUST-ALPHA', 'Alpha Components', 'HU'),
    (102, 1, 'CUST-BETA', 'Beta Industrial', 'DE'),
    (103, 1, 'CUST-GAMMA', 'Gamma Works', 'AT');

INSERT INTO product VALUES
    (1001, 'BRG-6204', 'Bearing 6204', 12.50),
    (1002, 'BLT-M8-30', 'Bolt M8x30', 0.35),
    (1003, 'PMP-A10', 'Assembly Pump A10', 245.00);

INSERT INTO sales_order VALUES
    (5001, 101, '2026-01-15T09:00:00Z', 'SHIPPED'),
    (5002, 102, '2026-01-16T10:30:00Z', 'CONFIRMED'),
    (5003, 101, '2026-01-17T11:15:00Z', 'NEW');

INSERT INTO sales_order_line VALUES
    (5001, 1, 1001, 10, 12.50),
    (5001, 2, 1002, 100, 0.35),
    (5002, 1, 1003, 2, 245.00),
    (5003, 1, 1002, 50, 0.35);
