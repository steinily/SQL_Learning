SELECT c.name, COUNT(o.order_id) AS order_count FROM customers AS c LEFT JOIN orders AS o ON o.customer_id = c.customer_id GROUP BY c.customer_id, c.name ORDER BY c.name;
SELECT o.order_id, SUM(oi.quantity * p.unit_price) AS total FROM orders AS o JOIN order_items AS oi ON oi.order_id = o.order_id JOIN products AS p ON p.product_id = oi.product_id WHERE o.status <> 'cancelled' GROUP BY o.order_id ORDER BY o.order_id;
SELECT c.name FROM customers AS c LEFT JOIN orders AS o ON o.customer_id = c.customer_id WHERE o.order_id IS NULL;
