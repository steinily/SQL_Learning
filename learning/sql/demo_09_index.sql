-- query: index létrehozása és terv megtekintése
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
-- query: végrehajtási terv
EXPLAIN QUERY PLAN SELECT * FROM orders WHERE customer_id = 1;
