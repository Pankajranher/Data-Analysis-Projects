import streamlit as st 
import pandas as pd
from data_analysis.data_cleaning import loading_and_cleaning_data 
from data_analysis.eda import get_kpis, get_sales_by_category
from visuals.charts import sales_trend, top_products

st.title("Sales Data Analysis Dashboard by Pankaj")

file_path = "data\\sales_data.csv"
df = loading_and_cleaning_data(file_path)

region = st.sidebar.multiselect("Select Region", options=df['Region'].unique(), default=df['Region'].unique())
category = st.sidebar.multiselect("Select Category", options=df['Category'].unique(), default=df['Category'].unique())

df_filtered = df[df['Region'].isin(region) & df['Category'].isin(category)]

kpis = get_kpis(df_filtered)
st.metric("Total Sales", f"${kpis['Total Sales']:.2f}")
st.metric("Total Profit", f"${kpis['Total Profit']:.2f}")
st.metric("Total Quantity", f"{int(kpis['Total Quantity'])}")
st.metric("Average Discount", f"{kpis['Average Discount']:.2%}")

st.plotly_chart(sales_trend(df_filtered))
st.plotly_chart(top_products(df_filtered))