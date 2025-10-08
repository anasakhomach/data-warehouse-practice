
# How to Fix Hidden Databases in DBeaver

This document explains how to solve a common issue in DBeaver where newly created databases do not appear in the Database Navigator.

### The Problem

You have successfully run the `CREATE DATABASE` command, and you have even received an error message confirming that the database "already exists" when you try to run it again. However, the new database is not visible in the Database Navigator panel, even after refreshing.

### The Cause

This usually happens because your DBeaver connection is configured to only show a specific database (e.g., the default `postgres` database) instead of all the databases on the server.

### The Solution

You need to edit your DBeaver connection settings to remove this filter.

---

### Step-by-Step Instructions

1.  **Find Your Connection:**
    *   In the DBeaver "Database Navigator" panel on the left, find the top-level item for your PostgreSQL connection (it will have a PostgreSQL elephant icon).

2.  **Edit the Connection:**
    *   **Right-click** on the connection icon.
    *   From the context menu, select **Edit Connection**.

3.  **Go to the "General" Tab:**
    *   A settings window will pop up. Make sure you are on the **General** or **Main** tab (it's usually the first tab).

4.  **Find the "Database" Field:**
    *   In the "Connection Settings" section, you will see a field labeled **Database**.
    *   Most likely, this field currently has `postgres` written in it.

5.  **Clear the "Database" Field:**
    *   **Delete all the text** in the "Database" field, leaving it completely **empty**.
    *   This tells DBeaver: "Show me all the databases on this server."

6.  **Save and Reconnect:**
    *   Click the **Finish** or **OK** button at the bottom to save your changes.
    *   Back in the Database Navigator, **right-click** on your connection again and select **Disconnect**.
    *   **Right-click** one more time and select **Connect**.

7.  **Verify the Result:**
    *   Your database list should now refresh, and your `DataWarehouse` database should be visible alongside the `postgres` database.
