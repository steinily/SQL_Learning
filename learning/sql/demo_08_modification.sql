-- query: biztonságos módosítás és visszagörgetés
BEGIN;
-- query: áremelés tranzakción belül
UPDATE products SET unit_price = ROUND(unit_price * 1.10, 2) WHERE category = 'book';
-- query: ellenőrzés
SELECT name, unit_price FROM products WHERE category = 'book';
-- query: visszagörgetés
ROLLBACK;
