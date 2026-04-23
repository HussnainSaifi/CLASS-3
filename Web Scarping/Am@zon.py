from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

url = "https://www.amazon.com/s?k=mobile"

driver = webdriver.Chrome()
driver.get(url)

time.sleep(5)  

productList = []

products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

for p in products:
    product = {}

    try:
        # name
        product["name"] = p.find_element(By.TAG_NAME, "h2").text

        # price
        try:
            whole = p.find_element(By.CLASS_NAME, "a-price-whole").text
            fraction = p.find_element(By.CLASS_NAME, "a-price-fraction").text
            product["price"] = whole + "." + fraction
        except:
            product["price"] = "N/A"

        # ratting
        try:
            product["rating"] = p.find_element(By.CLASS_NAME, "a-icon-alt").text
        except:
            product["rating"] = "N/A"

        # solid
        text = p.text.lower()
        if "bought" in text:
            product["sold"] = "Available"
        else:
            product["sold"] = "Sold"

        productList.append(product)

    except:
        pass

filename = 'Web Scarping/inspirational_quotesMethod2.csv'

with open(filename, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, ["name", "price", "rating", "sold"])
    w.writeheader()
    for product in productList:
        w.writerow(product)

driver.quit()