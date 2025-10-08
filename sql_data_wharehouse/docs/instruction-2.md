
# Instructions for Loading Data with DBeaver

This document provides step-by-step instructions for loading data from a local CSV file into a PostgreSQL table using DBeaver's "Import Data" feature. This is a **client-side** import, which is the correct method when your database server (e.g., in a Docker container) does not have direct access to your local files.

### Your Assignment

Follow these instructions to load the data from `cust_info.csv` into the `bronze.crm_cust_info` table.

---

### Step-by-Step Guide

1.  **Navigate to the Table:**
    *   In the DBeaver "Database Navigator" panel on the left, expand the folders until you find your target table.
    *   The path is: `DataWarehouse` -> `Schemas` -> `bronze` -> `Tables` -> `crm_cust_info`.

2.  **Open the Import Data Wizard:**
    *   **Right-click** on the `crm_cust_info` table.
    *   From the context menu, select **Import Data**.

3.  **Select the Data Source:**
    *   A wizard window titled "Import data" will appear.
    *   For the "Choose source type", select **CSV**.
    *   Click **Next**.

4.  **Select the Input File:**
    *   You are now on the "Select input CSV file(s)" screen.
    *   Click the **Select File(s)...** button.
    *   In the file browser, navigate to and select the `cust_info.csv` file from your local machine. The path is `C:\Users\Nitro\SQL\sql_data_wharehouse\datasets\source_crm\cust_info.csv`.
    *   Click **Open**.

5.  **Configure Importer Settings:**
    *   Click **Next**.
    *   You will now see the "Importer settings" screen. DBeaver is usually smart enough to auto-detect the correct settings, but you should verify them:
        *   **Delimiter:** Should be set to `,` (comma).
        *   **Header:** Should be checked (meaning the first row is the header).
        *   The preview at the bottom of the window should show your data correctly formatted in columns.

6.  **Configure Data Load Settings:**
    *   Click **Next**.
    *   You are now on the "Tables mapping" screen. This is where you map the columns from your CSV file to the columns in your database table.
    *   DBeaver should automatically map the columns based on their names. Verify that the mapping is correct (e.g., `cst_id` from the source file is mapped to `cst_id` in the target table).

7.  **Start the Import:**
    *   Click **Next**.
    *   You will see the final "Confirm data load" screen, which summarizes the import task.
    *   Click the **Proceed** button.
    *   DBeaver will now execute the import. You will see a progress window, and upon completion, it will show you the status and how many rows were loaded.

8.  **Verify the Data:**
    *   After the import is complete, you can verify that the data has been loaded correctly by right-clicking on the `crm_cust_info` table and selecting "View Data" (or simply running `SELECT * FROM bronze.crm_cust_info;` in an SQL editor).

---

Once you have successfully loaded the data for this table, report back to me. We will then proceed to load the data for the remaining tables.
