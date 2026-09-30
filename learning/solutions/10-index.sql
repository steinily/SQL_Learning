EXPLAIN QUERY PLAN SELECT * FROM orders WHERE customer_id = 1;
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
EXPLAIN QUERY PLAN SELECT * FROM orders WHERE customer_id = 1;
-- Kis adatmennyiségnél a teljes tábla bejárása olcsó lehet; ezért a tervet és a mérést valódi adatmennyiségen kell értékelni.
