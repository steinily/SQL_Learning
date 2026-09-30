SELECT c.name, COALESCE(o.status, 'nincs rendelés') AS order_status FROM customers c LEFT JOIN orders o ON o.customer_id = c.customer_id ORDER BY c.name, o.order_id;
SELECT c.name FROM customers c LEFT JOIN orders o ON o.customer_id = c.customer_id WHERE o.order_id IS NULL;
SELECT c.name, COUNT(o.order_id) AS order_count FROM customers c LEFT JOIN orders o ON o.customer_id = c.customer_id GROUP BY c.customer_id, c.name ORDER BY c.name;
