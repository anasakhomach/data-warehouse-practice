/*
===============================================================================
Database Exploration
===============================================================================
Purpose:
    - To explore the structure of the database, including the list of tables and their schemas.
    - To inspect the columns and metadata for specific tables.

Table Used:
    - INFORMATION_SCHEMA.TABLES
    - INFORMATION_SCHEMA.COLUMNS
===============================================================================
*/

-- Retrieve a list of all tables in the database
SELECT 
    table_catalog, 
    table_schema, 
    table_name, 
    table_type
FROM information_schema.tables
WHERE table_schema NOT IN ('information_schema', 'pg_catalog');

-- Retrieve all columns for a specific table (dim_customers)
SELECT 
    column_name, 
    data_type, 
    is_nullable, 
    character_maximum_length
FROM information_schema.columns
WHERE table_name = 'dim_customers'
  AND table_schema = 'gold';