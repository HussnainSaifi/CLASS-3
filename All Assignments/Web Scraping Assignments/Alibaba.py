from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

url = "https://www.alibaba.com/trade/search?SearchText=mobile"

driver = webdriver.Chrome()
driver.get(url)


time.sleep(15)

data = []

items = driver.find_elements(By.XPATH, "//div[contains(@class,'search-card')]")

print("Found items:", len(items))

for item in items:
    try:
        text = item.text.split("\n")

        # name
        name = text[0] if len(text) > 0 else "N/A"

        # price
        price = "N/A"
        for t in text:
            if "$" in t or "USD" in t:
                price = t
                break

        # link
        try:
            link = item.find_element(By.TAG_NAME, "a").get_attribute("href")
        except:
            link = "N/A"

        
        if name != "N/A":
            data.append({
                "name": name[:70],
                "price": price,
                "link": link
            })

    except:
        continue

driver.quit()


filename = r"All Assignments\Web Scraping\alibaba.csv"

with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, ["name", "price", "link"])
    writer.writeheader()
    writer.writerows(data)

print("DONE 🚀 Alibaba scraping complete")
print("Total products:", len(data))