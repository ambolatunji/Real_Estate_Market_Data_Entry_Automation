#Google sheets Integration
import gspread
import pandas as pd

from oauth2client.service_account import ServiceAccountCredentials

def upload_to_google_sheets(csv_file, sheet_name):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("google_sheets_credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open(sheet_name).sheet1
    df = pd.read_csv(csv_file)
    sheet.update([df.columns.values.tolist()] + df.values.tolist())

    print("✅ Data Uploaded to Google Sheets!")

if __name__ == "__main__":
    upload_to_google_sheets("cleaned_real_estate_data.csv", "Real Estate Data")

#MySQL integration

import pymysql
import pandas as pd

def upload_to_mysql(csv_file):
    connection = pymysql.connect(host="localhost", user="root", password="password", database="real_estate_db")
    cursor = connection.cursor()

    df = pd.read_csv(csv_file)
    cursor.execute("CREATE TABLE IF NOT EXISTS properties (Price INT, Address TEXT, Link TEXT)")

    for _, row in df.iterrows():
        cursor.execute("INSERT INTO properties (Price, Address, Link) VALUES (%s, %s, %s)",
                       (row["Price"], row["Address"], row["Link"]))
    
    connection.commit()
    connection.close()
    print("✅ Data Uploaded to MySQL!")

if __name__ == "__main__":
    upload_to_mysql("cleaned_real_estate_data.csv")
