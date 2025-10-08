/*
=============================================================
Create Database and Schemas for the Data Warehouse (PostgreSQL)
=============================================================
Script Purpose:
    This script creates a new database named 'data_warehouse' and
    sets up three schemas within it: 'bronze', 'silver', and 'gold'.

    This version follows the project naming conventions using snake_case.

WARNING:
    Running this script will drop the entire 'data_warehouse' database if it exists.
    All data in the database will be permanently deleted.
*/



-- This command must be run from a PostgreSQL client connected to the default 'postgres' database.
-- You cannot drop the database you are currently connected to.

-- First, terminate all connections to the 'data_warehouse' database
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'data_warehouse'
  AND pid <> pg_backend_pid();

-- Drop the database if it exists
DROP DATABASE IF EXISTS data_warehouse;

-- Create the database
CREATE DATABASE data_warehouse;

-- The following commands should be run after connecting to the 'data_warehouse' database.
-- You can do this by right-clicking on the 'data_warehouse' database in DBeaver and opening a new SQL editor.

SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'data_warehouse'
  AND pid <> pg_backend_pid();

-- Drop the database if it exists
DROP DATABASE IF EXISTS data_warehouse;

-- Create the database
CREATE DATABASE data_warehouse;

-- The following commands should be run after connecting to the 'data_warehouse' database.
-- You can do this by right-clicking on the 'data_warehouse' database in DBeaver and opening a new SQL editor.

CREATE SCHEMA IF NOT EXISTS bronze;
CREATE SCHEMA IF NOT EXISTS silver;
CREATE SCHEMA IF NOT EXISTS gold;