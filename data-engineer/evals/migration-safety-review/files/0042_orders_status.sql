-- migration 0042_orders_status.sql
BEGIN;

ALTER TABLE users DROP COLUMN phone;

ALTER TABLE orders ADD COLUMN status VARCHAR(20) NOT NULL;

CREATE INDEX idx_orders_status ON orders (status);

COMMIT;
