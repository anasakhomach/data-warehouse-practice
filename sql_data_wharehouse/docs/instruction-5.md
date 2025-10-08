# Instructions for Loading the Entire Bronze Layer

This document provides the complete script and instructions for loading all the tables in the `bronze` schema from their respective CSV files.

---

### Option 1: Simple Loading Script

A simple way to load the data is to run a script of `TRUNCATE` and `COPY` commands. This is good for a one-time load.

```sql
-- Loading bronze.crm_cust_info
TRUNCATE TABLE bronze.crm_cust_info;
COPY bronze.crm_cust_info
FROM '/data/source_crm/cust_info.csv'
WITH (FORMAT CSV, HEADER true, DELIMITER ',');

-- (repeat for all other tables...)
```

---

### Option 2: Professional Stored Procedure (Recommended)

The professional and repeatable way to handle this process is to create a **Stored Procedure**. This encapsulates the entire loading logic into a single, reusable command. It also allows for logging and error handling.

Your assignment is to create and execute this stored procedure.

1.  **Create a new file:** In the `scripts/bronze` directory, create a new file named `load_bronze.pgsql.sql` (or update your existing one).
2.  **Write the procedure:** Use the complete script provided below. This is your own translated code, corrected to use the modern `CREATE PROCEDURE` syntax.
3.  **Execute the script:** Run this script in DBeaver. This will not load the data directly, but it will *create* the `load_bronze` procedure in the database.
4.  **Run the procedure:** After the procedure is created, you can execute it at any time by running the simple command: `CALL bronze.load_bronze();`

#### Complete Bronze Layer Loading Procedure

```sql
/*
===============================================================================
Stored Procedure: Load Bronze Layer (Source -> Bronze) - PostgreSQL Version
File: proc_load_bronze.pgsql.sql
===============================================================================
*/

CREATE OR REPLACE PROCEDURE bronze.load_bronze()
LANGUAGE plpgsql
AS $$
DECLARE
    start_time TIMESTAMP;
    end_time TIMESTAMP;
    batch_start_time TIMESTAMP;
    batch_end_time TIMESTAMP;
    duration_seconds INTEGER;
    total_duration_seconds INTEGER;
BEGIN
    BEGIN
        batch_start_time := NOW();
        RAISE NOTICE '================================================';
        RAISE NOTICE 'Loading Bronze Layer';
        RAISE NOTICE '================================================';

        RAISE NOTICE '------------------------------------------------';
        RAISE NOTICE 'Loading CRM Tables';
        RAISE NOTICE '------------------------------------------------';

        -- Loading bronze.crm_cust_info
        start_time := NOW();
        RAISE NOTICE '>> Truncating Table: bronze.crm_cust_info';
        TRUNCATE TABLE bronze.crm_cust_info;
        RAISE NOTICE '>> Inserting Data Into: bronze.crm_cust_info';
        COPY bronze.crm_cust_info
        FROM '/data/source_crm/cust_info.csv'
        WITH (FORMAT CSV, HEADER true, DELIMITER ',');
        end_time := NOW();
        duration_seconds := EXTRACT(EPOCH FROM (end_time - start_time))::INTEGER;
        RAISE NOTICE '>> Load Duration: % seconds', duration_seconds;
        RAISE NOTICE '>> -------------';

        -- Loading bronze.crm_prd_info
        start_time := NOW();
        RAISE NOTICE '>> Truncating Table: bronze.crm_prd_info';
        TRUNCATE TABLE bronze.crm_prd_info;
        RAISE NOTICE '>> Inserting Data Into: bronze.crm_prd_info';
        COPY bronze.crm_prd_info
        FROM '/data/source_crm/prd_info.csv'
        WITH (FORMAT CSV, HEADER true, DELIMITER ',');
        end_time := NOW();
        duration_seconds := EXTRACT(EPOCH FROM (end_time - start_time))::INTEGER;
        RAISE NOTICE '>> Load Duration: % seconds', duration_seconds;
        RAISE NOTICE '>> -------------';

        -- Loading bronze.crm_sales_details
        start_time := NOW();
        RAISE NOTICE '>> Truncating Table: bronze.crm_sales_details';
        TRUNCATE TABLE bronze.crm_sales_details;
        RAISE NOTICE '>> Inserting Data Into: bronze.crm_sales_details';
        COPY bronze.crm_sales_details
        FROM '/data/source_crm/sales_details.csv'
        WITH (FORMAT CSV, HEADER true, DELIMITER ',');
        end_time := NOW();
        duration_seconds := EXTRACT(EPOCH FROM (end_time - start_time))::INTEGER;
        RAISE NOTICE '>> Load Duration: % seconds', duration_seconds;
        RAISE NOTICE '>> -------------';

        RAISE NOTICE '------------------------------------------------';
        RAISE NOTICE 'Loading ERP Tables';
        RAISE NOTICE '------------------------------------------------';

        -- Loading bronze.erp_loc_a101
        start_time := NOW();
        RAISE NOTICE '>> Truncating Table: bronze.erp_loc_a101';
        TRUNCATE TABLE bronze.erp_loc_a101;
        RAISE NOTICE '>> Inserting Data Into: bronze.erp_loc_a101';
        COPY bronze.erp_loc_a101
        FROM '/data/source_erp/loc_a101.csv'
        WITH (FORMAT CSV, HEADER true, DELIMITER ',');
        end_time := NOW();
        duration_seconds := EXTRACT(EPOCH FROM (end_time - start_time))::INTEGER;
        RAISE NOTICE '>> Load Duration: % seconds', duration_seconds;
        RAISE NOTICE '>> -------------';

        -- Loading bronze.erp_cust_az12
        start_time := NOW();
        RAISE NOTICE '>> Truncating Table: bronze.erp_cust_az12';
        TRUNCATE TABLE bronze.erp_cust_az12;
        RAISE NOTICE '>> Inserting Data Into: bronze.erp_cust_az12';
        COPY bronze.erp_cust_az12
        FROM '/data/source_erp/cust_az12.csv'
        WITH (FORMAT CSV, HEADER true, DELIMITER ',');
        end_time := NOW();
        duration_seconds := EXTRACT(EPOCH FROM (end_time - start_time))::INTEGER;
        RAISE NOTICE '>> Load Duration: % seconds', duration_seconds;
        RAISE NOTICE '>> -------------';

        -- Loading bronze.erp_px_cat_g1v2
        start_time := NOW();
        RAISE NOTICE '>> Truncating Table: bronze.erp_px_cat_g1v2';
        TRUNCATE TABLE bronze.erp_px_cat_g1v2;
        RAISE NOTICE '>> Inserting Data Into: bronze.erp_px_cat_g1v2';
        COPY bronze.erp_px_cat_g1v2
        FROM '/data/source_erp/px_cat_g1v2.csv'
        WITH (FORMAT CSV, HEADER true, DELIMITER ',');
        end_time := NOW();
        duration_seconds := EXTRACT(EPOCH FROM (end_time - start_time))::INTEGER;
        RAISE NOTICE '>> Load Duration: % seconds', duration_seconds;
        RAISE NOTICE '>> -------------';

        batch_end_time := NOW();
        total_duration_seconds := EXTRACT(EPOCH FROM (batch_end_time - batch_start_time))::INTEGER;
        RAISE NOTICE '==========================================';
        RAISE NOTICE 'Loading Bronze Layer is Completed';
        RAISE NOTICE '   - Total Load Duration: % seconds', total_duration_seconds;
        RAISE NOTICE '==========================================';

    EXCEPTION
        WHEN OTHERS THEN
            RAISE NOTICE '==========================================';
            RAISE NOTICE 'ERROR OCCURRED DURING LOADING BRONZE LAYER';
            RAISE NOTICE 'Error Message: %', SQLERRM;
            RAISE NOTICE 'Error Code: %', SQLSTATE;
            RAISE NOTICE '==========================================';
            RAISE;
    END;
END;
$$;
```