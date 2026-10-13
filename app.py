import streamlit as st
import pandas as pd
st.title("SALES DATA ANALYSIS DASHBOARD")
df = pd.read_csv("Sales_data_sample.csv")
st.header("SALES DATA")
show_data = st.checkbox("Show Data")
if show_data:
    st.dataframe(df)
st.metric( "Total Sales",                                                                                                                                                          
            "₹1683480.18")
st.metric( "LOSS",
            "-157290.24")
st.metric( "MAX DISCOUNT",
            "600.05")
st.metric( "MIN DISCOUNT",
            "36.6555")
st.metric( "TOTAL ORDERS",
            "499")
st.metric( "LOSS ORDER COUNT",
            "275")
st.metric( "PROFIT ORDER COUNT",
            "224")
st.metric( "AVERAGE SALES",
            "3373.708")
st.metric("No of products","4")
st.header("Filter Data") 
city = st.selectbox(
    "Select City", ["All"] + list(df["REGION"].unique()) )
if city != "All":
    filtered_df = df[df["REGION"] == city]
else: filtered_df = df 
PRODUCTS = st.selectbox(
    "Select PRODUCTS", ["All"] + list(df["PRODUCTLINE"].unique()) )
if PRODUCTS != "All":
    filtered_df = df[df["PRODUCTLINE"] == PRODUCTS]
else: filtered_df = df
year = st.selectbox(
    "Select year",["All"] + ["2003", "2004", "2005"])
PRICE_range = st.slider( "Select PRICE Range", 0, 100 )
option = st.radio( "Select Gender", ["Male", "Female", "Other"] )
df.columns = df.columns.str.strip().str.upper()
st.write(option) 
st.header("SALES ANALYSIS")
st.header("Sales by Product")
sales_by_product = df.groupby("PRODUCTLINE")["SALES"].sum()
print(sales_by_product)
st.bar_chart(sales_by_product)
st.header("LOSS ANALYSIS")
st.header("loss by Product")
loss_by_product = ( df.groupby("PRODUCTLINE")["PROFIT"].sum() )
st.area_chart(loss_by_product)
st.header("year_wise_Sales")
year_wise_Sales = ( df.groupby("ORDERDATE")["SALES"].sum() )
st.line_chart(year_wise_Sales)
st.header("Region_wise_Sales")
Region_wise_Sales = ( df.groupby("REGION")["SALES"].sum() )
st.bar_chart(Region_wise_Sales)
