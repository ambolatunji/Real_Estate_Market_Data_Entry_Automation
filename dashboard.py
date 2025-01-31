import streamlit as st
import pandas as pd

st.title("📊 Real Estate Market Dashboard")

df = pd.read_csv("cleaned_real_estate_data.csv")

st.dataframe(df)

st.bar_chart(df["Price"])
st.write("✅ Data Visualization Completed!")
