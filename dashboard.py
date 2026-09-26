import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="E-Commerce Sales Performance", page_icon="📊", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/amazon_sales_cleaned.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

st.title("E-Commerce Sales Performance Analysis")
st.caption("Interactive portfolio dashboard built with Python, Pandas, and Plotly.")

# Sidebar filters
st.sidebar.header("Filters")
categories = st.sidebar.multiselect("Category", sorted(df["Category"].dropna().unique()), default=sorted(df["Category"].dropna().unique()))
fulfilment = st.sidebar.multiselect("Fulfilment", sorted(df["Fulfilment"].dropna().unique()), default=sorted(df["Fulfilment"].dropna().unique()))
status = st.sidebar.multiselect("Status", sorted(df["Status"].dropna().unique()), default=sorted(df["Status"].dropna().unique()))

f = df[df["Category"].isin(categories) & df["Fulfilment"].isin(fulfilment) & df["Status"].isin(status)].copy()

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Reported Order Value", f["Amount"].sum())
col2.metric("Unique Orders", f["Order ID"].nunique())
col3.metric("Quantity", f["Qty"].sum())
col4.metric("Unique Styles", f["Style"].nunique())

st.divider()

left, right = st.columns(2)

monthly = f.assign(Month=f["Date"].dt.to_period("M").astype(str)).groupby("Month", as_index=False)["Amount"].sum()
fig_month = px.line(monthly, x="Month", y="Amount", markers=True, title="Monthly Reported Order Value")
left.plotly_chart(fig_month, use_container_width=True)

cat = f.groupby("Category", as_index=False)["Amount"].sum().sort_values("Amount", ascending=False).head(10)
fig_cat = px.bar(cat.sort_values("Amount"), x="Amount", y="Category", orientation="h", title="Top Categories by Reported Order Value")
right.plotly_chart(fig_cat, use_container_width=True)

left, right = st.columns(2)

states = f.groupby("ship-state", as_index=False)["Amount"].sum().sort_values("Amount", ascending=False).head(10)
fig_state = px.bar(states.sort_values("Amount"), x="Amount", y="ship-state", orientation="h", title="Top States by Reported Order Value")
left.plotly_chart(fig_state, use_container_width=True)

statuses = f["Status"].value_counts().reset_index()
statuses.columns = ["Status", "Order Lines"]
fig_status = px.bar(statuses, x="Status", y="Order Lines", title="Order Status Distribution")
right.plotly_chart(fig_status, use_container_width=True)

st.subheader("Top 10 Product Styles")
styles = f.groupby("Style", as_index=False)["Amount"].sum().sort_values("Amount", ascending=False).head(10)
st.dataframe(styles, use_container_width=True, hide_index=True)

st.caption("Note: Amount represents reported order-line value in the source dataset. Cancellations and returns are not automatically treated as recognized revenue.")
