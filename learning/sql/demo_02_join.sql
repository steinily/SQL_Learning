-- query: vevő és rendelés összekapcsolása
SELECT c.name, o.order_id, o.status FROM customers AS c JOIN orders AS o ON o.customer_id = c.customer_id ORDER BY o.order_id;
-- query: rendelési értékek
SELECT o.order_id, c.name, SUM(oi.quantity * p.unit_price) AS total FROM orders AS o JOIN customers AS c ON c.customer_id = o.customer_id JOIN order_items AS oi ON oi.order_id = o.order_id JOIN products AS p ON p.product_id = oi.product_id WHERE o.status <> 'cancelled' GROUP BY o.order_id, c.name ORDER BY total DESC;
