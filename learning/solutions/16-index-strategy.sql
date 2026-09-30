CREATE INDEX idx_orders_status_date_exercise ON orders(status, order_date);
EXPLAIN QUERY PLAN SELECT order_id FROM orders WHERE status = 'paid' AND order_date >= '2026-01-01';
-- Az összetett index bal szélső oszlopa a vezető; status nélkül a date predicate nem ugyanúgy használja a prefixet.
