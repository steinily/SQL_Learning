BEGIN;
UPDATE products SET unit_price = unit_price * 1.10 WHERE category = 'book';
SELECT name, unit_price FROM products WHERE category = 'book';
ROLLBACK;

BEGIN;
INSERT INTO products(product_id, name, category, unit_price) VALUES (6, 'SQL kártyacsomag', 'book', 4000);
COMMIT;
SELECT * FROM products WHERE product_id = 6;
