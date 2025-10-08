
# Instructions for a Complete Environment Reset

This document provides a complete, step-by-step guide to reset your project environment from scratch. Following these steps carefully will resolve the issues of the disappearing database and the schemas being created in the wrong place.

**The most important part of these instructions is to always check which database your SQL editor is connected to before you run any script.**

---

### Part 1: Reset the Docker Container

First, we will destroy the old container and create a new, clean one with the correct settings.

1.  **Open your terminal** (PowerShell or Command Prompt).
2.  **Remove the old container** by running this command:
    ```sh
    docker rm -f my-postgres-container
    ```
3.  **Create the new container** by running your correct `docker run` command. **Make sure to use your correct password.**
    ```sh
    docker run --name my-postgres-container -e POSTGRES_PASSWORD=123 -p 5432:5432 -v C:\Users\Nitro\SQL\sql_data_wharehouse\datasets:/data -d postgres
    ```

---

### Part 2: Create the `DataWarehouse` Database

Now, we will create our main database.

1.  **Open DBeaver** and connect to your PostgreSQL server.
2.  **Open a new SQL editor** (`File -> New -> SQL Editor`).
3.  **IMPORTANT:** At the top of the SQL editor window, there is a dropdown menu to select the active database. **Make sure it is set to `postgres`** (the default database).
4.  **Run the following script** in this editor to create your `DataWarehouse` database:
    ```sql
    -- Terminate all other connections to the 'DataWarehouse' database
    SELECT pg_terminate_backend(pg_stat_activity.pid)
    FROM pg_stat_activity
    WHERE pg_stat_activity.datname = 'DataWarehouse'
      AND pid <> pg_backend_pid();

    -- Drop the database if it exists
    DROP DATABASE IF EXISTS DataWarehouse;

    -- Create the database
    CREATE DATABASE DataWarehouse;
    ```
5.  After the script runs, **refresh your database list** in the Database Navigator. You should now see the `DataWarehouse` database.

---

### Part 3: Create the Schemas (The Correct Way)

This is the most critical part. We will now create the schemas *inside* the correct database.

1.  **Open a new SQL editor**.
2.  **IMPORTANT:** At the top of this new editor, use the dropdown menu to **change the active database to `DataWarehouse`**. This is the step that was causing the problems before.
3.  **Run the following script** in this editor:
    ```sql
    CREATE SCHEMA IF NOT EXISTS bronze;
    CREATE SCHEMA IF NOT EXISTS silver;
    CREATE SCHEMA IF NOT EXISTS gold;
    ```
4.  **Verify the result:** In the Database Navigator, expand your `DataWarehouse` database, then expand the `Schemas` folder. You should now see `bronze`, `silver`, and `gold` *inside* `DataWarehouse`.

---

### Part 4: Create the Bronze Tables

Now that you are correctly connected to the `DataWarehouse` database, you can create the tables.

1.  **In the same SQL editor** (which is still connected to the `DataWarehouse` database), open your `ddl_bronze.pgsql.sql` file (`scripts/bronze/ddl_bronze.pgsql.sql`).
2.  **Execute the entire script** to create all the bronze tables.
3.  **Verify the result:** In the Database Navigator, expand the `bronze` schema, then the `Tables` folder. You should see all your newly created bronze tables.

---

### Part 5: Load the Bronze Data

Finally, let's load the data.

1.  **In the same SQL editor**, open your `load_bronze.pgsql.sql` file (`scripts/bronze/load_bronze.pgsql.sql`).
2.  **Execute the script** to create the `load_bronze` stored procedure.
3.  **In the same editor**, run the procedure to load the data:
    ```sql
    CALL bronze.load_bronze();
    ```
4.  **Verify the result:** Right-click on one of the bronze tables (e.g., `crm_cust_info`) and select "View Data". You should see the data from the CSV file.

---

Follow these steps exactly. Once you have completed all of them, your environment will be correctly set up, and you will be ready to continue with the silver layer. Report back to me when you are done.
