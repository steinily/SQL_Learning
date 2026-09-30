EXPLAIN QUERY PLAN SELECT order_id, order_date FROM orders WHERE customer_id = 1;
CREATE INDEX idx_orders_customer_id_optimization ON orders(customer_id);
EXPLAIN QUERY PLAN SELECT order_id, order_date FROM orders WHERE customer_id = 1;
-- A terv javulása önmagában nem elég; production méretű adaton futási időt és IO-t is mérni kell.
