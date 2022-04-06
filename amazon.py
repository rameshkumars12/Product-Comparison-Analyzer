# importing the necessary libraries
import pandas as pd
from time import sleep #to sleep screen
from selenium import webdriver #for using selenium by webdriver
from selenium.webdriver.common.by import By #for using By commands ex:By.XPATH
from selenium.webdriver.common.keys import Keys #for sending keys
from bs4 import BeautifulSoup


def azon(search_item):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome("chromedriver.exe", options=options)

    url = "https://www.amazon.in/"
    driver.get(url)
    search = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
    search_send = search.send_keys(search_item)
    search.send_keys(Keys.RETURN)


    sleep(1)
    search_list = driver.find_elements(By.CSS_SELECTOR,'.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal')
    result = ""
    for result in search_list:
        result = result.get_attribute("href")
        break

    driver.get(result)

    ProductData = []
    try:
        ProductRating = driver.find_element(By.ID,'acrPopover').get_attribute('title')
        ProductRating = ProductRating.split(" ")[0]
    except:
        ProductRating = "No Ratings"
    try:
        OriginalPrice = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr[1]/td[2]/span[1]/span[2]').text
        OriginalPrice = OriginalPrice.split(".")[0]

    except:
        OriginalPrice = ""
    try:
        ProductStatus = driver.find_element(By.CSS_SELECTOR, '._16FRp0').text
    except:
        ProductStatus = "Available"
    try:
        DiscountAmount = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr[3]/td[2]/span[1]/span/span[2]').text
        DiscountAmount = DiscountAmount.split(".")[0]

    except:
        DiscountAmount = "No Offers Available"
    try:
        OfferPrice = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]').text
        OfferPrice = OfferPrice.split(".")[0]

    except:
        OfferPrice = "No Offers Available"

    ProductDetails = {"Rating": ProductRating,
                      "Original Price": OriginalPrice,
                      "Product Status": ProductStatus,
                      "Discount Amount": DiscountAmount,
                      "Offer Price": OfferPrice,
                      "Link": result}
    ProductData.append(ProductDetails)
    driver.quit()

    df = pd.DataFrame(ProductData)
    return df



