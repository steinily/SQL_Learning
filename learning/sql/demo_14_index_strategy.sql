-- query: összetett index
CREATE INDEX idx_orders_status_date ON orders(status, order_date);
-- query: prefix keresés terve
EXPLAIN QUERY PLAN SELECT order_id FROM orders WHERE status = 'paid' AND order_date >= '2026-01-01';
