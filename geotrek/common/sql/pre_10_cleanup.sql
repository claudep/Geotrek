DROP TABLE IF EXISTS south_migrationhistory;  -- legacy, replaced by django_migrations table

DROP FUNCTION IF EXISTS ft_date_insert() CASCADE;
DROP FUNCTION IF EXISTS ft_date_update() CASCADE;

CREATE EXTENSION IF NOT EXISTS "pgcrypto";