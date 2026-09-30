-- query: két vagy több nem törölt rendelést leadó vevők
SELECT c.name, COUNT(o.order_id) AS order_count FROM customers AS c JOIN orders AS o ON o.customer_id = c.customer_id WHERE o.status <> 'cancelled' GROUP BY c.customer_id, c.name HAVING COUNT(o.order_id) >= 2;
