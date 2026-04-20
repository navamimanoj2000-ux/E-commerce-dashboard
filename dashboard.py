import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("E-Commerce Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_data.csv")
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Month'] = df['InvoiceDate'].dt.month
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    return df

df = load_data()

# Sidebar filter
st.sidebar.header("Filters")
country = st.sidebar.selectbox("Select Country", df['Country'].unique())

filtered_df = df[df['Country'] == country]

# KPIs
st.subheader("Key Metrics")
st.write("Total Transactions:", len(filtered_df))
st.write("Total Revenue:", filtered_df['Revenue'].sum())

# Top products
st.subheader("Top 10 Products")
top_products = filtered_df.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots()
sns.barplot(x=top_products.values, y=top_products.index, ax=ax)
st.pyplot(fig)

# Top countries (global, not filtered)
st.subheader("Top Countries")
top_countries = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False).head(10)

fig2, ax2 = plt.subplots()
sns.barplot(x=top_countries.index, y=top_countries.values, ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)

# Monthly trend
st.subheader("Monthly Revenue Trend")
monthly_sales = filtered_df.groupby('Month')['Revenue'].sum()

st.line_chart(monthly_sales)