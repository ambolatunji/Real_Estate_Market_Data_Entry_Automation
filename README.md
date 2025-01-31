
# 🏡 Real Estate Data Scraper & Entry Automation

This project scrapes real estate listings from Zillow, cleans and validates the data, then uploads it to Google Sheets or MySQL for further analysis.

## 🔹 Features:

- **Web Scraping**: Uses Selenium & BeautifulSoup to scrape listings.
- **Data Cleaning**: Ensures price formatting, removes duplicates.
- **Automated Data Entry**: Supports Google Sheets & MySQL.
- **Dashboard**: Uses Streamlit for data visualization.

## 🔧 How to Run:

1. Install dependencies: `pip install -r requirements.txt`
2. Run scraper: `python main_scraper.py`
3. Clean data: `python data_cleaning.py`
4. Upload to DB: `python db_entry.py`
5. Start Dashboard: `streamlit run dashboard.py`
