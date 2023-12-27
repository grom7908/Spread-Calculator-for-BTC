from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re


def get_crypto_price(url, accept_locator, price_locator, output_label):
    driver = webdriver.Chrome()

    try:
        driver.get(url)
        time.sleep(2)

        if accept_locator:
            find_accept = driver.find_element(*accept_locator)
            find_accept.click()

        find_price = driver.find_element(*price_locator)
        crypto_price_str = find_price.text.strip()

        match = re.search(r'\d[\d.,]*', crypto_price_str)
        numeric_price = match.group() if match else None

        output_label.config(text=f"BTC price is {numeric_price}$")

    except Exception as e:
        output_label.config(text=f"An error occurred: {e}")

    finally:
        driver.quit()


url_binance = "https://www.binance.com/en"
accept_locator_binance = (By.ID, "onetrust-accept-btn-handler")
price_locator_binance = (
    By.XPATH, "/html/body/div[3]/div/main/div[1]/div/div/div[2]/div[1]/div/div/a[1]/div[2]/div/div")

url_bybit = "https://www.bybit.com/en"
price_locator_bybit = (
    By.CSS_SELECTOR, ".SectionList_price__3cLEn.SectionList_right__1nar7")

url_okx = "https://www.okx.com"
accept_locator_okx = (By.ID, "onetrust-accept-btn-handler")
price_locator_okx = (By.CSS_SELECTOR, "a.ticker-item")


# get_crypto_price(url_binance, accept_locator_binance, price_locator_binance)
# get_crypto_price(url_bybit, None, price_locator_bybit)
# get_crypto_price(url_okx, accept_locator_okx, price_locator_okx)
