import streamlit as st
import pandas as pd
import subprocess
import os

st.title("📊 Real Estate Market Dashboard")

# ✅ Run Web Scraper
st.write("🚀 Running Web Scraper...")
subprocess.run(["python", "main_scraper.py"])
st.write("✅ Scraping Completed!")

# ✅ Run Data Cleaning
st.write("🔍 Cleaning Data...")
subprocess.run(["python", "data_cleaning.py"])
st.write("✅ Data Cleaning Done!")

# ✅ Upload to Database
st.write("📤 Uploading Data to Database...")
subprocess.run(["python", "db_entry.py"])
st.write("✅ Data Successfully Uploaded!")

# ✅ Load Cleaned Data
st.write("📊 Loading Data for Visualization...")
df = pd.read_csv("cleaned_real_estate_data.csv")

# Display Data
st.dataframe(df)

# Plot Price Distribution
st.bar_chart(df["Price"])
st.write("✅ Data Visualization Ready!")
