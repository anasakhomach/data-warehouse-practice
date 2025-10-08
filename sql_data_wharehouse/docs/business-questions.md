
# Business Questions for Data Warehouse Analysis

This document contains a categorized list of business questions that can be answered using the data warehouse. Use these questions as exercises to practice your SQL and data analysis skills.

---

## Tier 1: Foundational Questions

*(These are common, high-value questions that form the foundation of business intelligence. The difficulty is low, as they can be answered with simple aggregations and `GROUP BY` clauses.)*

1.  **Overall Performance:** What are our all-time total sales revenue, total items sold, and total number of unique orders?
2.  **Customer Base:** How many unique customers have we ever had? How many of them have made at least one purchase?
3.  **Product Catalog:** How many unique products do we have in our catalog? What is the distribution of these products across different cost ranges (`<100`, `100-500`, etc.)?
4.  **Geographic Distribution:** How many customers do we have in each country?
5.  **Basic Ranking:** Who are our top 10 customers by total revenue? What are our top 10 best-selling products by total revenue?

---

## Tier 2: Deep-Dive Questions

*(These questions are common in more mature businesses. They are high-value and have a medium difficulty, as they often require window functions, CTEs, and more complex joins.)*

1.  **Trend Analysis:** What is our month-over-month trend for total sales, number of customers, and quantity sold?
2.  **Performance Analysis:** How did each product's sales in 2013 compare to its sales in 2012 (Year-over-Year growth)? How did each product's sales in 2013 compare to its own average sales across all years?
3.  **Part-to-Whole:** What percentage of our total revenue does each product category (`Bikes`, `Accessories`, `Clothing`) contribute?
4.  **Customer Segmentation Value:** What is the total revenue and average order value (AOV) for each customer segment (`VIP`, `Regular`, `New`)?
5.  **Customer Demographics:** What is the breakdown of our `VIP` customer segment by age group?
6.  **Customer Recency:** Who are our most "at-risk" customers? (i.e., who are the top 10 customers with the highest `recency` score?).

---

## Tier 3: Advanced Strategic Questions

*(These questions are less common but can provide very high value by uncovering deeper strategic insights. They have a high difficulty and may require multiple complex queries, subqueries, and a deep interpretation of the results.)*

1.  **The "One and Done" Problem:** Who are our "one-and-done" customers (customers who have only ever made one order)? What product did they buy on their first and only order? Does this give us a clue as to which products are failing to create loyal customers?
2.  **Customer Lifetime Value (LTV):** What is the average total revenue we can expect from a customer in each segment (`VIP`, `Regular`, `New`) over their entire lifespan? (Hint: This is a more advanced version of the AOV calculation).
3.  **Product Correlation (Market Basket Analysis):** Are there products that are frequently bought together in the same order? (e.g., "Customers who bought Product A also bought Product B"). This is a very advanced query that often requires self-joins.
4.  **Age and Category Correlation:** Is there a correlation between a customer's `age_group` and the `category` of products they buy? Do younger customers buy different types of products than older customers?
5.  **Sales Velocity:** For the products that were introduced in 2013, how long did it take for them to generate their first $10,000 in sales? Which new products were the fastest to grow?
