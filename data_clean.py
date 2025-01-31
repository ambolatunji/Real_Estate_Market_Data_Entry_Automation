import pandas as pd
import re

def clean_real_estate_data(csv_file):
    df = pd.read_csv(csv_file)

    # Remove unnecessary characters from price
    df["Price"] = df["Price"].apply(lambda x: re.sub(r"[^0-9]", "", x)) 

    # Convert Price to Numeric
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

    # Drop any rows with missing addresses
    df.dropna(subset=["Address"], inplace=True)

    df.to_csv("cleaned_real_estate_data.csv", index=False)
    print("✅ Data Cleaned & Saved to CSV!")

if __name__ == "__main__":
    clean_real_estate_data("real_estate_data.csv")
