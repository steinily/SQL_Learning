-- query: optimalizálható keresés
CREATE INDEX idx_orders_customer_id_advanced ON orders(customer_id);
-- query: terv vizsgálata
EXPLAIN QUERY PLAN SELECT order_id, order_date FROM orders WHERE customer_id = 1;
