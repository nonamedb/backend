

CREATE USER nonamedb PASSWORD 'test';
--ALTER USER script_db SUPERUSER;
CREATE DATABASE nonamedb_backend;
GRANT ALL PRIVILEGES ON DATABASE nonamedb_backend TO nonamedb;
ALTER ROLE nonamedb WITH SUPERUSER;
