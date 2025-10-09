import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# --- Page Configuration ---
# Set the page title, icon, and layout
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# --- Dashboard Title ---
st.title("Sales Analytics Dashboard")

st.write("Welcome to our sales dashboard! We will build our visuals here.")

# --- Database Connection ---
# Using the modern st.connection
st.success("Attempting to connect to the database using st.connection...")

try:
    # Test connection
    test_conn = st.connection("postgresql", type="sql")
    df = test_conn.query('SELECT COUNT(*) FROM gold.fact_sales;', ttl=600)
    st.success(f"Connection successful! The fact_sales table has {df.iloc[0,0]:,} rows.")

except Exception as e:
    st.error(f"Could not connect to database. Error: {e}")

# --- Data Loading Functions (to be added) ---
# --- Data Loading Functions ---
@st.cache_data
def load_segmentation_data():
    conn = st.connection("postgresql", type="sql")
    query = "SELECT customer_segment FROM gold.report_customers;"
    df = conn.query(query, ttl=600)
    return df

@st.cache_data
def load_aov_data():
    conn = st.connection("postgresql", type="sql")
    query = """
        SELECT customer_segment, AVG(avg_order_value) AS average_aov
        FROM gold.report_customers
        GROUP BY customer_segment;
    """
    df = conn.query(query, ttl=600)
    return df

@st.cache_data
def load_category_revenue_data():
    conn = st.connection("postgresql", type="sql")
    query = """
        WITH category_sales AS (
            SELECT p.category, SUM(f.sales_amount) AS total_sales
            FROM gold.fact_sales f
            LEFT JOIN gold.dim_products p ON p.product_key = f.product_key
            GROUP BY p.category
        )
        SELECT category, total_sales
        FROM category_sales
        ORDER BY total_sales DESC;
    """
    df = conn.query(query, ttl=600)
    return df

@st.cache_data
def load_vip_age_data():
    conn = st.connection("postgresql", type="sql")
    query = """
        SELECT age_group
        FROM gold.report_customers
        WHERE customer_segment = 'VIP';
    """
    df = conn.query(query, ttl=600)
    return df

@st.cache_data
def load_monthly_sales_data():
    conn = st.connection("postgresql", type="sql")
    query = """
        SELECT DATE_TRUNC('month', order_date::date) AS sales_month, SUM(sales_amount) AS total_sales
        FROM gold.fact_sales
        WHERE order_date IS NOT NULL
        GROUP BY sales_month
        ORDER BY sales_month;
    """
    df = conn.query(query, ttl=600)
    return df

@st.cache_data
def load_main_kpis():
    conn = st.connection("postgresql", type="sql")
    # A single query to get all main KPIs efficiently
    query = """
        SELECT
            (SELECT SUM(sales_amount) FROM gold.fact_sales) AS total_sales,
            (SELECT COUNT(DISTINCT order_number) FROM gold.fact_sales) AS total_orders,
            (SELECT COUNT(DISTINCT customer_key) FROM gold.dim_customers) AS total_customers,
            (SELECT AVG(avg_order_value) FROM gold.report_customers) AS average_aov;
    """
    # conn.query returns a DataFrame, so we get the first row as a tuple
    df = conn.query(query, ttl=600)
    kpi_data = (df.iloc[0]['total_sales'], df.iloc[0]['total_orders'], 
                df.iloc[0]['total_customers'], df.iloc[0]['average_aov'])
    return kpi_data


# --- Charting Functions (to be added) ---
# --- Charting Functions ---
def create_segmentation_chart(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.set_style("whitegrid")

    sns.countplot(
        ax=ax,
        data=df,
        x='customer_segment',
        order=['VIP', 'Regular', 'New'],
        palette=['#4c72b0', '#55a868', '#c44e52']
    )

    ax.set_title('Customer Segmentation Breakdown (The "Leaky Bucket")', fontsize=16)
    ax.set_xlabel('Customer Segment', fontsize=12)
    ax.set_ylabel('Number of Customers', fontsize=12)

    for p in ax.patches:
        ax.annotate(f'{int(p.get_height()):,}',
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center',
                    xytext=(0, 9),
                    textcoords='offset points')
    return fig

def create_aov_chart(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.set_style("whitegrid")

    sns.barplot(
        ax=ax,
        data=df,
        x='customer_segment',
        y='average_aov',
        order=['VIP', 'Regular', 'New'],
        palette=['#4c72b0', '#55a868', '#c44e52']
    )

    ax.set_title('Average Order Value (AOV) by Segment', fontsize=16)
    ax.set_xlabel('Customer Segment', fontsize=12)
    ax.set_ylabel('Average Order Value ($)', fontsize=12)

    for p in ax.patches:
        ax.annotate(f'${p.get_height():,.2f}',
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center',
                    xytext=(0, 9),
                    textcoords='offset points')
    return fig

def create_category_donut_chart(df):
    fig = px.pie(
        df,
        names='category',
        values='total_sales',
        title='Revenue Contribution by Product Category',
        hole=0.4,
        color_discrete_sequence=px.colors.sequential.Blues_r
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(showlegend=False)
    return fig

def create_vip_age_chart(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.set_style("whitegrid")

    age_order = ['Under 20', '20-29', '30-39', '40-49', '50 and above']

    sns.countplot(
        ax=ax,
        data=df,
        x='age_group',
        order=age_order,
        palette='viridis_r'
    )

    ax.set_title('Age Distribution of VIP Customers', fontsize=16)
    ax.set_xlabel('Age Group', fontsize=12)
    ax.set_ylabel('Number of VIP Customers', fontsize=12)

    for p in ax.patches:
        ax.annotate(f'{int(p.get_height()):,}',
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center',
                    xytext=(0, 9),
                    textcoords='offset points')
    return fig

def create_monthly_sales_chart(df):
    fig = px.line(
        df,
        x='sales_month',
        y='total_sales',
        title='Monthly Sales Trend'
    )
    fig.update_layout(
        yaxis_title='Total Sales ($)',
        xaxis_title='Date'
    )
    return fig


# --- Dashboard Layout (to be added) ---
# --- Dashboard Layout ---

# --- Top Row: KPI Cards ---
# Load the KPI data
kpis = load_main_kpis()
# Unpack the tuple into individual variables
total_sales, total_orders, total_customers, average_aov = kpis

# Create four columns for the four KPIs
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

# Create a metric card in each column
kpi1.metric(
    label="Total Sales 💵",
    value=f"${total_sales/1_000_000:.2f}M"
)

kpi2.metric(
    label="Total Orders 🛒",
    value=f"{int(total_orders):,}"
)

kpi3.metric(
    label="Total Customers 👥",
    value=f"{int(total_customers):,}"
)

kpi4.metric(
    label="Avg. Order Value ＄",
    value=f"${average_aov:,.2f}"
)

# Add a divider after KPIs
st.divider()

st.header("Customer Analysis: The 'Leaky Bucket'")

# Create two columns
col1, col2 = st.columns(2)

# --- Place the first chart in column 1 ---
with col1:
    segment_df = load_segmentation_data()
    segment_fig = create_segmentation_chart(segment_df)
    st.pyplot(segment_fig)

# --- Place the second chart in column 2 ---
with col2:
    aov_df = load_aov_data()
    aov_fig = create_aov_chart(aov_df)
    st.pyplot(aov_fig)

# --- Add a divider for visual separation ---
st.divider()

# --- Second Section: Business Risk Analysis ---
st.header("Business Risk Analysis")
col3, col4 = st.columns(2)

# --- Place the donut chart in the first new column ---
with col3:
    category_df = load_category_revenue_data()
    category_fig = create_category_donut_chart(category_df)
    # Use st.plotly_chart for Plotly visuals
    st.plotly_chart(category_fig, use_container_width=True)

# --- Place the VIP age chart in the second new column ---
with col4:
    vip_age_df = load_vip_age_data()
    vip_age_fig = create_vip_age_chart(vip_age_df)
    st.pyplot(vip_age_fig)

# --- Add a final divider ---
st.divider()

# --- Third Section: Historical Performance ---
st.header("Historical Performance")

monthly_sales_df = load_monthly_sales_data()
monthly_sales_fig = create_monthly_sales_chart(monthly_sales_df)
st.plotly_chart(monthly_sales_fig, use_container_width=True)