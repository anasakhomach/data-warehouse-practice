
# Instructions for Translating `ddl_bronze.sql` to PostgreSQL

This document provides the exact instructions to translate the `ddl_bronze.sql` script from T-SQL (SQL Server's dialect) to PostgreSQL's SQL dialect.

### Your Assignment

1.  **Create a new file:** In the `scripts/bronze` directory, create a new file named `ddl_bronze.pgsql.sql`.
2.  **Translate the script:** Use the instructions below to translate the original T-SQL code and write the final, correct PostgreSQL script into your new file.
3.  **Execute the script:** Run your new `ddl_bronze.pgsql.sql` script in DBeaver to create all the tables in the `bronze` schema.

---

### Translation Rules

#### 1. Syntax Changes

*   **Dropping Tables:** Replace all the `IF OBJECT_ID(...) ... DROP TABLE ...` blocks with the simpler PostgreSQL equivalent: `DROP TABLE IF EXISTS schema_name.table_name;`
*   **`GO` Keyword:** Remove all instances of the `GO` keyword. PostgreSQL uses the semicolon (`;`) as the statement terminator, which is already present.

#### 2. Data Type Translations

*   **`NVARCHAR(n)`:** Replace all instances of `NVARCHAR(n)` with `VARCHAR(n)`.
*   **`DATETIME`:** Replace all instances of `DATETIME` with `TIMESTAMP`.
*   **`INT` and `DATE`:** These data types are standard and should remain the same.

---

### Final Translated Script

Here is the complete, final translated script for you to use. This is the code that should be in your `ddl_bronze.pgsql.sql` file.

```sql
/*
===============================================================================
DDL Script: Create Bronze Tables (PostgreSQL)
===============================================================================
*/

DROP TABLE IF EXISTS bronze.crm_cust_info;

CREATE TABLE bronze.crm_cust_info (
    cst_id              INT,
    cst_key             VARCHAR(50),
    cst_firstname       VARCHAR(50),
    cst_lastname        VARCHAR(50),
    cst_marital_status  VARCHAR(50),
    cst_gndr            VARCHAR(50),
    cst_create_date     DATE
);

DROP TABLE IF EXISTS bronze.crm_prd_info;

CREATE TABLE bronze.crm_prd_info (
    prd_id       INT,
    prd_key      VARCHAR(50),
    prd_nm       VARCHAR(50),
    prd_cost     INT,
    prd_line     VARCHAR(50),
    prd_start_dt TIMESTAMP,
    prd_end_dt   TIMESTAMP
);

DROP TABLE IF EXISTS bronze.crm_sales_details;

CREATE TABLE bronze.crm_sales_details (
    sls_ord_num  VARCHAR(50),
    sls_prd_key  VARCHAR(50),
    sls_cust_id  INT,
    sls_order_dt INT,
    sls_ship_dt  INT,
    sls_due_dt   INT,
    sls_sales    INT,
    sls_quantity INT,
    sls_price    INT
);

DROP TABLE IF EXISTS bronze.erp_loc_a101;

CREATE TABLE bronze.erp_loc_a101 (
    cid    VARCHAR(50),
    cntry  VARCHAR(50)
);

DROP TABLE IF EXISTS bronze.erp_cust_az12;

CREATE TABLE bronze.erp_cust_az12 (
    cid    VARCHAR(50),
    bdate  DATE,
    gen    VARCHAR(50)
);

DROP TABLE IF EXISTS bronze.erp_px_cat_g1v2;

CREATE TABLE bronze.erp_px_cat_g1v2 (
    id           VARCHAR(50),
    cat          VARCHAR(50),
    subcat       VARCHAR(50),
    maintenance  VARCHAR(50)
);
```
