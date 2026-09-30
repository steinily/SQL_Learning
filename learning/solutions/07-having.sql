SELECT city, COUNT(*) AS customer_count FROM customers GROUP BY city HAVING COUNT(*) >= 2;
SELECT c.name, COUNT(o.order_id) AS order_count FROM customers c JOIN orders o ON o.customer_id = c.customer_id WHERE o.status <> 'cancelled' GROUP BY c.customer_id, c.name HAVING COUNT(o.order_id) >= 2;
SELECT category, AVG(unit_price) AS average_price FROM products GROUP BY category HAVING AVG(unit_price) >= 5000;
