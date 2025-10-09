# Comprehensive Visualization Plan (The Lab)

This document outlines a comprehensive plan for exploring our data visually within the Jupyter Notebook environment. The goal is to create every potential visual derived from our analytical scripts.

### 1. Visualization Plan

---

### **Group A: High-Level Metrics & Overview**

#### **Visual 1: Executive KPI Cards**
-   **Source Query:** `04_measures_exploration.pgsql.sql`
-   **Business Question:** What are the overall, high-level performance numbers for the business?
-   **Chart Type:** KPI Cards (displaying single numbers).
-   **Library:** Matplotlib/Plotly for text rendering.
-   **Description:** A series of cards for `Total Sales`, `Total Quantity Sold`, `Total Orders`, and `Total Unique Customers`.

#### **Visual 2: Data Time Range**
-   **Source Query:** `03_date_range_exploration.pgsql.sql`
-   **Business Question:** What is the time period covered by our data?
-   **Chart Type:** KPI Cards or a simple timeline text summary.
-   **Library:** Matplotlib/Plotly for text rendering.
-   **Description:** Displays the `first_order_date`, `last_order_date`, and total time span in months.

#### **Visual 3: Customer Distribution by Country**
-   **Source Query:** `05_magnitude_analysis.pgsql.sql` (total customers by countries)
-   **Business Question:** Where are our customers located?
-   **Chart Type:** Bar Chart.
-   **Library:** **Seaborn (`barplot`)**. It's clean and effective for ranking categorical data.
-   **Description:** A bar chart ranking countries by the number of customers.

---

### **Group B: Customer-Centric Analysis**

#### **Visual 4: Customer Segmentation**
-   **Source Query:** `10_data_segmentation.pgsql.sql`
-   **Business Question:** How are our customers segmented by value and loyalty?
-   **Chart Type:** Bar Chart.
-   **Library:** **Seaborn (`countplot`)**. Best for showing counts of categories.
-   **Description:** The key "leaky bucket" visual. Shows the count of `VIP`, `Regular`, and `New` customers.

#### **Visual 5: Average Order Value (AOV) by Segment**
-   **Source Query:** `12_report_customers.pgsql.sql` (calculates `avg_order_value`)
-   **Business Question:** How much more valuable are VIP customers?
-   **Chart Type:** Bar Chart.
-   **Library:** **Seaborn (`barplot`)**.
-   **Description:** Compares the AOV for each customer segment, highlighting the value of VIPs.

#### **Visual 6: VIP Customer Age Demographics**
-   **Source Query:** `12_report_customers.pgsql.sql` (calculates `age_group`)
-   **Business Question:** What is the age distribution of our most valuable customers?
-   **Chart Type:** Bar Chart.
-   **Library:** **Seaborn (`countplot`)** on the filtered VIP data.
-   **Description:** Shows the count of VIP customers in each age bracket, revealing the reliance on an older demographic.

#### **Visual 7: Top 10 Customers by Revenue**
-   **Source Query:** `06_ranking_analysis.pgsql.sql`
-   **Business Question:** Who are our individual top performers?
-   **Chart Type:** Horizontal Bar Chart.
-   **Library:** **Plotly (`bar`)**. Interactivity is useful here to show exact revenue on hover.
-   **Description:** A ranked list of the top 10 individual customers by their total lifetime spending.

---

### **Group C: Product-Centric Analysis**

#### **Visual 8: Revenue Contribution by Product Category**
-   **Source Query:** `11_part_to_whole_analysis.pgsql.sql`
-   **Business Question:** What is the revenue breakdown by product category?
-   **Chart Type:** Donut Chart.
-   **Library:** **Plotly (`pie` with a `hole`)**. The interactivity and clean look are perfect for this.
-   **Description:** The key "revenue concentration" visual, showing the ~96.5% dominance of `Bikes`.

#### **Visual 9: Top 5 & Bottom 5 Products by Revenue**
-   **Source Query:** `06_ranking_analysis.pgsql.sql`
-   **Business Question:** Which specific products are our best-sellers and worst-sellers?
-   **Chart Type:** Two Horizontal Bar Charts.
-   **Library:** **Seaborn (`barplot`)**.
-   **Description:** One chart for the top 5 products by revenue and a separate one for the bottom 5, providing a full view of product performance.

#### **Visual 10: Product Cost Segmentation**
-   **Source Query:** `10_data_segmentation.pgsql.sql`
-   **Business Question:** How are our products distributed across different cost brackets?
-   **Chart Type:** Bar Chart.
-   **Library:** **Seaborn (`countplot`)**.
-   **Description:** Shows the number of products in ranges like 'Below 100', '100-500', etc.

---

### **Group D: Time-Series Analysis**

#### **Visual 11: Monthly Sales Trend**
-   **Source Query:** `07_change_over_time_analysis.pgsql.sql`
-   **Business Question:** How has our revenue performed month-over-month?
-   **Chart Type:** Line Chart.
-   **Library:** **Plotly (`line`)**. The ability to zoom and pan through time is critical for time-series analysis.
-   **Description:** A line chart of total sales revenue over time.

#### **Visual 12: Cumulative Revenue Growth**
-   **Source Query:** `08_cumulative_analysis.pgsql.sql`
-   **Business Question:** What is the long-term growth trajectory of the business?
-   **Chart Type:** Area Chart.
-   **Library:** **Plotly (`area`)**.
-   **Description:** An area chart showing the running total of sales, which provides a smooth curve of overall business growth.

#### **Visual 13: Year-over-Year Product Performance**
-   **Source Query:** `09_performance_analysis.pgsql.sql`
-   **Business Question:** How did product sales change from one year to the next?
-   **Chart Type:** Grouped Bar Chart.
-   **Library:** **Plotly (`bar`)**. Plotly makes creating grouped bar charts straightforward.
-   **Description:** For a selection of key products, this chart will show bars for 2012 and 2013 sales side-by-side, making YoY comparison easy.

### 2. Dashboard Layout (for the future "Art Gallery")

-   **Structure:** A tabbed layout in Streamlit would be ideal to manage this large number of visuals.
    -   **Tab 1: "Executive Summary"**: Contains the core story (Visuals 1, 4, 5, 8, 11).
    -   **Tab 2: "Customer Deep-Dive"**: Contains all customer-related visuals (6, 7, etc.).
    -   **Tab 3: "Product Deep-Dive"**: Contains all product-related visuals (9, 10, 13, etc.).

### 3. Analytical Report Outline

1.  **Executive Summary:** State the main findings (leaky bucket, revenue concentration).
2.  **Core Insights (The Main Story):** Use the visuals from the "Executive Summary" tab to tell the primary narrative.
3.  **Appendix A: Detailed Customer Analysis:** Include and discuss the more granular customer charts.
4.  **Appendix B: Detailed Product Analysis:** Include and discuss the more granular product charts.
5.  **Strategic Recommendations:** Propose actions based on the core insights.