
# A Complete Guide to Building and Analyzing a Data Warehouse

This document summarizes the complete journey of building a data warehouse from scratch, translating it to a new database system, and performing a deep-dive analysis. It serves as a record of all the assignments and key lessons from our project.

---

## Phase 1: Project Setup and Environment

This phase was about making the correct architectural decisions and setting up a professional, repeatable development environment.

#### 1. Choosing the Right Database
*   **Assignment:** We started with the goal of translating a T-SQL project to a new database dialect.
*   **Key Lesson:** We had a deep discussion about the architectural differences between MySQL and PostgreSQL, specifically how they handle schemas. We learned that in PostgreSQL, a schema is a namespace within a database, while in MySQL, a schema is a synonym for a database. We chose PostgreSQL to correctly replicate the `database.schema.table` hierarchy of the original project.

#### 2. Adopting Naming Conventions
*   **Assignment:** We decided on a professional naming convention for our database.
*   **Key Lesson:** We learned that using generic names like `DataWarehouse` is not scalable. We adopted the `snake_case` convention and chose the name `data_warehouse` to ensure our project is well-organized and avoids conflicts with other projects.

#### 3. Setting up the Docker Environment
*   **Assignment:** We set up a PostgreSQL server running inside a Docker container.
*   **Key Lesson:** We learned how to use Docker volumes (`-v` flag) to create a "shared folder" between our local machine and the Docker container. This was the key to solving the file access issue and enabling server-side data loading with the `COPY` command.

#### 4. Configuring the Database Client (DBeaver)
*   **Assignment:** We troubleshooted and correctly configured our DBeaver connection.
*   **Key Lesson:** We learned that GUI clients like DBeaver have their own connection settings. We learned how to edit the connection and clear the "Database" field to ensure that all databases on the server are visible. We also learned how to switch the active database for our SQL editor using the dropdown menu, which is the PostgreSQL equivalent of the `USE` command in MySQL.

#### 5. Setting up the Git Monorepo
*   **Assignment:** We created a local Git monorepo and pushed it to a remote repository on GitHub.
*   **Key Lesson:** We learned how to structure a monorepo to hold multiple, related projects. We initialized a Git repository at the root of our workspace and added our data warehouse and data analytics projects as subdirectories.

---

## Phase 2: Building the Data Warehouse (ETL)

This phase was about translating the DDL and ETL scripts for each layer of the data warehouse.

#### 1. The Bronze Layer (Raw Data Ingestion)
*   **Assignment 1 (DDL):** Translate `ddl_bronze.sql` to PostgreSQL. We learned to replace `IF OBJECT_ID`, `GO`, `NVARCHAR`, and `DATETIME` with their PostgreSQL equivalents (`DROP TABLE IF EXISTS`, `VARCHAR`, `TIMESTAMP`).
*   **Assignment 2 (ETL):** Translate `proc_load_bronze.sql`. We learned to replace the T-SQL `BULK INSERT` command with the PostgreSQL `COPY` command. We also learned how to create a proper PostgreSQL `PROCEDURE` with logging (`RAISE NOTICE`) and error handling (`EXCEPTION` block).

#### 2. The Silver Layer (Cleansing and Transformation)
*   **Assignment 1 (DDL):** Translate `ddl_silver.sql`. We learned how to translate the `DEFAULT GETDATE()` clause to `DEFAULT NOW()` or `DEFAULT CURRENT_TIMESTAMP`.
*   **Assignment 2 (ETL):** Translate `proc_load_silver.sql`. This was a major assignment where we learned to translate various T-SQL functions to their PostgreSQL equivalents:
    *   `LEN()` -> `LENGTH()` (and how to `CAST` to `VARCHAR` first)
    *   `ISNULL()` -> `COALESCE()`
    *   Date arithmetic (`- 1`) -> ` - INTERVAL '1 day'`

#### 3. The Gold Layer (Presentation and Analytics)
*   **Assignment 1 (DDL):** Translate `ddl_gold.sql`. We learned that this layer was built using `VIEW`s and how to translate the `DROP VIEW` syntax.
*   **Assignment 2 & 3 (Reports):** Translate `12_report_customers.sql` and `13_report_products.sql`. This was our final "exam", where we applied all our translation skills to create the final, comprehensive reporting views.

---

## Phase 3: Data Analytics

This phase was about using the data warehouse we built to find real business insights.

*   **Lesson 1: Database Exploration:** We learned how to use the `INFORMATION_SCHEMA` to explore the metadata of our database.
*   **Lesson 2: Dimension Exploration:** We learned how to use `DISTINCT` and `ORDER BY` to explore the content of our dimension tables. We also performed our first **data quality investigation** by diagnosing the cause of `NULL` values in the `dim_products` view.
*   **Lesson 3: Date Range Exploration:** We learned how to use PostgreSQL's powerful date functions (`AGE`, `EXTRACT`) and the `INTERVAL` data type to analyze the time span of our data.
*   **Lesson 4: Measures Exploration:** We learned how to use aggregate functions (`SUM`, `COUNT`, `AVG`, `DISTINCT`) to calculate high-level KPIs. We also learned how to use `UNION ALL` to create a summary report.
*   **Lesson 5: Magnitude Analysis:** We learned how to use the `GROUP BY` clause to "slice and dice" our data and break down our KPIs by different dimensions.
*   **Lesson 6: Ranking Analysis:** We learned how to answer "Top N" questions using both the simple `LIMIT` clause and the more powerful `RANK()` window function.
*   **Lesson 7: Change Over Time Analysis:** We learned how to analyze trends by grouping data by time periods. We learned three different methods for this: `EXTRACT`, `DATE_TRUNC`, and `TO_CHAR`.
*   **Lesson 8: Cumulative Analysis:** We learned how to calculate running totals and moving averages using window functions (`SUM() OVER (...)`, `AVG() OVER (...)`).
*   **Lesson 9: Performance Analysis:** We learned how to perform Year-over-Year analysis using the `LAG()` window function and how to compare performance against an average using `PARTITION BY`.
*   **Lesson 10: Segmentation Analysis:** We learned how to use `CASE` statements to segment our data into meaningful groups. This led to our most important insights.
*   **Lesson 11: Part-to-Whole Analysis:** We learned how to calculate the percentage contribution of each part to the whole, using the empty `OVER ()` clause in a window function.

### Our Final Data Story

Through this process, we uncovered a deep and compelling story about the business, identifying its core strengths, its strategic flaws (the "leaky bucket" and product concentration), and a clear, data-driven path to future growth. This was documented in the `data-story.md` file.
