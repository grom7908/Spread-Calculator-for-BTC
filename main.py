from selenium import webdriver
from selenium.webdriver.common.by import By #importing all required libraries
import time
import re


def get_crypto_price(url, accept_locator, price_locator, output_label): #defining function that gets crypto price 
    driver = webdriver.Chrome() #driver is chrome

    try: 
        driver.get(url) #driver gets url
        time.sleep(2) #give driver time to load page

        if accept_locator: #if click to accept cookies is required then it does it 
            find_accept = driver.find_element(*accept_locator)
            find_accept.click()

        find_price = driver.find_element(*price_locator) #finds the element containing the cryptocurrency price
        crypto_price_str = find_price.text.strip() #retrieves and strips the text content of the found element

        match = re.search(r'\d[\d.,]*', crypto_price_str) #searches for a numeric pattern in the stripped text
        numeric_price = match.group() if match else None  #extracts the matched numeric value if found, else None

        output_label.config(text=f"BTC price is {numeric_price}$") #output

    except Exception as e:
        output_label.config(text=f"An error occurred: {e}") #output if an error exists

    finally:
        driver.quit() #quits the driver


url_binance = "https://www.binance.com/en" #url
accept_locator_binance = (By.ID, "onetrust-accept-btn-handler") #find accept locator with its id
price_locator_binance = (
    By.XPATH, "/html/body/div[3]/div/main/div[1]/div/div/div[2]/div[1]/div/div/a[1]/div[2]/div/div") #find price by full xpath

url_bybit = "https://www.bybit.com/en"
price_locator_bybit = (
    By.CSS_SELECTOR, ".SectionList_price__3cLEn.SectionList_right__1nar7") #by css selector

url_okx = "https://www.okx.com"
accept_locator_okx = (By.ID, "onetrust-accept-btn-handler")
price_locator_okx = (By.CSS_SELECTOR, "a.ticker-item")

