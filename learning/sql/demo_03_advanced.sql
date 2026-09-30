-- query: CTE-vel számolt vevői összesítés
WITH customer_totals AS (SELECT o.customer_id, SUM(oi.quantity * p.unit_price) AS total FROM orders AS o JOIN order_items AS oi ON oi.order_id = o.order_id JOIN products AS p ON p.product_id = oi.product_id WHERE o.status <> 'cancelled' GROUP BY o.customer_id) SELECT c.name, COALESCE(ct.total, 0) AS total FROM customers AS c LEFT JOIN customer_totals AS ct ON ct.customer_id = c.customer_id ORDER BY total DESC, c.name;
-- query: ablakfüggvényes rangsor
SELECT name, category, unit_price, RANK() OVER (PARTITION BY category ORDER BY unit_price DESC) AS category_rank FROM products ORDER BY category, category_rank;
