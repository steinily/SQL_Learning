SELECT order_id, CASE WHEN status IN ('new', 'paid') THEN 'open' WHEN status = 'shipped' THEN 'done' WHEN status = 'cancelled' THEN 'cancelled' ELSE 'unknown' END AS order_state FROM orders;
SELECT name, CASE WHEN unit_price < 5000 THEN 'cheap' WHEN unit_price < 15000 THEN 'standard' ELSE 'premium' END AS price_band FROM products;
SELECT name, CASE WHEN unit_price > 10000 THEN 'yes' ELSE 'no' END AS has_discount FROM products;
