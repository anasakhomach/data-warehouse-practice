
# Data Engineering and Analytics Practice Monorepo

This repository contains a collection of projects for practicing end-to-end data engineering and data analytics workflows.

---

## Projects

This monorepo contains the following projects:

### 1. SQL Data Warehouse Project (`sql_data_wharehouse`)

*   **Goal:** To build a complete, three-layer (Bronze, Silver, Gold) data warehouse from scratch.
*   **Process:** This project involved translating a data warehouse from T-SQL (SQL Server) to PostgreSQL. It includes the full ETL process for ingesting, cleansing, transforming, and modeling the data.
*   **Key Artifacts:**
    *   `scripts/`: Contains the DDL and ETL scripts for each layer.
    *   `docs/`: Contains the data story, business questions, and all the instructions and assignments from the project.

### 2. SQL Data Analytics Project (`sql-data-analytics-project`)

*   **Goal:** To use the data warehouse to perform a deep-dive analysis and uncover business insights.
*   **Process:** This project involves working through a series of analytical SQL scripts to learn various techniques, including time-series analysis, performance analysis, customer segmentation, and more.
*   **Key Artifacts:**
    *   `scripts/`: Contains the original T-SQL analytics scripts (used as a reference) and our translated `.pgsql.sql` solutions.

### 3. Python Visualization Project (`notebooks/` and `streamlit_apps/`)

*   **Goal:** To take the insights from the analysis and create a suite of visualizations and a final, shareable web-based dashboard.
*   **Process:** This project uses Python to connect to the PostgreSQL database, query the data using our analytical SQL, and visualize the results.

---

## Technology Stack

*   **Database:** PostgreSQL (running in Docker)
*   **ETL & Analytics:** SQL
*   **Orchestration:** Manual (with a view to learning Airflow/dbt in the future)
*   **Visualization & App:** Python (with pandas, psycopg2, seaborn, plotly, and Streamlit)
*   **Environment Management:** `uv`
*   **IDE / Client:** DBeaver and JupyterLab

---

## How to Use

1.  **Set up the Environment:** Follow the instructions in `sql_data_wharehouse/docs/instruction-7.md` and `sql_data_wharehouse/docs/instruction-dbeaver-setup.md` to set up the PostgreSQL Docker container and the DBeaver connection.
2.  **Set up the Python Environment:** Follow the instructions in `sql_data_wharehouse/docs/assignments.md` (Phase 1) to set up the Python virtual environment using `uv`.
3.  **Build the Data Warehouse:** Execute the scripts in the `sql_data_wharehouse/scripts/` directory in the correct order (init, ddl, load procedures) to build and populate the data warehouse.
4.  **Perform the Analysis:** Work through the translated `.pgsql.sql` scripts in the `sql-data-analytics-project/scripts/` directory.
