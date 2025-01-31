import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

# Set up WebDriver (Download ChromeDriver and set path accordingly)
service = Service("chromedriver.exe")  # Update this path
driver = webdriver.Chrome(service=service)

def scrape_zillow():
    url = "https://www.zillow.com/homes/for_sale/"
    driver.get(url)
    time.sleep(5)  # Allow page to load

    soup = BeautifulSoup(driver.page_source, "html.parser")
    listings = soup.find_all("article", class_="list-card")

    data = []
    for listing in listings:
        try:
            price = listing.find("div", class_="list-card-price").text.strip()
            address = listing.find("address").text.strip()
            link = listing.find("a", class_="list-card-link")["href"]
            data.append({"Price": price, "Address": address, "Link": link})
        except AttributeError:
            continue

    driver.quit()
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = scrape_zillow()
    df.to_csv("real_estate_data.csv", index=False)
    print("✅ Data Scraped & Saved to CSV!")
