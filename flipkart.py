# importing the necessary libraries
import pandas as pd
from time import sleep #to sleep screen
from selenium import webdriver #for using selenium by webdriver
from selenium.webdriver.common.by import By #for using By commands ex:By.XPATH
from selenium.webdriver.common.keys import Keys #for sending keys



def kart_item(kart):


    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")


    driver = webdriver.Chrome("chromedriver", options=options)

    #Getting the url
    url = "https://www.flipkart.com/"
    driver.get(url)
    search = driver.find_element(By.CLASS_NAME, '_3704LK')
    search_send = search.send_keys(kart)
    search.send_keys(Keys.RETURN)

    close_popup = driver.find_element(By.CSS_SELECTOR, '._2KpZ6l._2doB4z').click()

    sleep(1)
    search_list = driver.find_elements(By.CSS_SELECTOR, '._1fQZEK')
    result = ""
    for result in search_list:
        result = result.get_attribute("href")
        break

    sleep(1)
    driver.get(result)

    ProductData = []
    try:
        ProductRating = driver.find_element(By.CSS_SELECTOR, '._3LWZlK').text
    except:
        ProductRating = ""
    try:
        OriginalPrice = driver.find_element(By.CSS_SELECTOR, '._3I9_wc._2p6lqe').text
    except:
        OriginalPrice = ""
    try:
        ProductStatus = driver.find_element(By.CSS_SELECTOR, '._16FRp0').text
    except:
        ProductStatus = "Available"
    try:
        DiscountAmount = driver.find_element(By.CSS_SELECTOR, '._1V_ZGU').text
        DiscountAmount = DiscountAmount.split(" ")[1]

    except:
        DiscountAmount = "No Discount"
    try:
        OfferPrice = driver.find_element(By.CSS_SELECTOR, '._30jeq3._16Jk6d').text
    except:
        OfferPrice = "No Offers Available"

    ProductDetails = {"Rating" : ProductRating,
                      "Original Price" : OriginalPrice,
                      "Product Status" : ProductStatus,
                      "Discount Amount" : DiscountAmount,
                      "Offer Price" : OfferPrice,
                      "Link": result}
    ProductData.append(ProductDetails)
    driver.quit()

    df = pd.DataFrame(ProductData)

    return df

