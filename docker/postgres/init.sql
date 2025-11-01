DO $$
BEGIN
  IF NOT EXISTS (
    SELECT FROM pg_database WHERE datname = 'movies'
  ) THEN
    PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE movies');
  END IF;
END
$$;

DO $$
BEGIN
  IF NOT EXISTS (
    SELECT FROM pg_roles WHERE rolname = 'root'
  ) THEN
    CREATE ROLE root WITH LOGIN PASSWORD 'rootroot';
    ALTER ROLE root SET client_encoding TO 'utf8';
    ALTER ROLE root SET default_transaction_isolation TO 'read committed';
    ALTER ROLE root SET timezone TO 'UTC';
  END IF;
END
$$;

GRANT ALL PRIVILEGES ON DATABASE movies TO root;

\connect movies
DO $$
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM information_schema.schemata WHERE schema_name = 'public'
  ) THEN
    PERFORM 'CREATE SCHEMA public';
  END IF;
END
$$;

GRANT ALL ON SCHEMA public TO root;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO root;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO root;
