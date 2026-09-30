-- query: árkategóriák
SELECT name, unit_price, CASE WHEN unit_price < 5000 THEN 'cheap' WHEN unit_price < 15000 THEN 'standard' ELSE 'premium' END AS price_band FROM products ORDER BY unit_price;
