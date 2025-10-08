/*
=============================================================
Create Database and Schemas
=============================================================
Script Purpose:
    This script creates a new database named 'data_warehouse_analytics' after checking if it already exists. 
    If the database exists, it is dropped and recreated. Additionally, this script creates a schema called gold
	
WARNING:
    Running this script will drop the entire 'data_warehouse_analytics' database if it exists. 
    All data in the database will be permanently deleted. Proceed with caution 
    and ensure you have proper backups before running this script.
*/

-- Terminate existing connections to the database
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'data_warehouse_analytics'
  AND pid <> pg_backend_pid();

-- Drop and recreate the 'data_warehouse_analytics' database
DROP DATABASE IF EXISTS data_warehouse_analytics;

-- Create the 'data_warehouse_analytics' database
CREATE DATABASE data_warehouse_analytics;

-- Connect to the new database
\c data_warehouse_analytics;

-- Create Schemas
CREATE SCHEMA IF NOT EXISTS gold;

-- Create Tables
CREATE TABLE gold.dim_customers(
	customer_key INTEGER,
	customer_id INTEGER,
	customer_number VARCHAR(50),
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	country VARCHAR(50),
	marital_status VARCHAR(50),
	gender VARCHAR(50),
	birthdate DATE,
	create_date DATE
);

CREATE TABLE gold.dim_products(
	product_key INTEGER,
	product_id INTEGER,
	product_number VARCHAR(50),
	product_name VARCHAR(50),
	category_id VARCHAR(50),
	category VARCHAR(50),
	subcategory VARCHAR(50),
	maintenance VARCHAR(50),
	cost INTEGER,
	product_line VARCHAR(50),
	start_date DATE 
);

CREATE TABLE gold.fact_sales(
	order_number VARCHAR(50),
	product_key INTEGER,
	customer_key INTEGER,
	order_date DATE,
	shipping_date DATE,
	due_date DATE,
	sales_amount INTEGER,
	quantity SMALLINT,
	price INTEGER 
);

-- Clear existing data
TRUNCATE TABLE gold.dim_customers;

-- Load data using COPY command (PostgreSQL equivalent of BULK INSERT)
-- Note: Update the file paths to match your PostgreSQL environment
\COPY gold.dim_customers FROM 'C:\sql\sql-data-analytics-project\datasets\csv-files\gold.dim_customers.csv' WITH (FORMAT CSV, HEADER true);

TRUNCATE TABLE gold.dim_products;

\COPY gold.dim_products FROM 'C:\sql\sql-data-analytics-project\datasets\csv-files\gold.dim_products.csv' WITH (FORMAT CSV, HEADER true);

TRUNCATE TABLE gold.fact_sales;

\COPY gold.fact_sales FROM 'C:\sql\sql-data-analytics-project\datasets\csv-files\gold.fact_sales.csv' WITH (FORMAT CSV, HEADER true);