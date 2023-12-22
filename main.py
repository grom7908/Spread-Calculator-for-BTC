from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_crypto_price(url, accept_locator, price_locator):
    driver = webdriver.Chrome()

    try:
        driver.get(url)
        time.sleep(2)

        find_accept = driver.find_element(*accept_locator)
        find_accept.click()

        find_price = driver.find_element(*price_locator)
        crypto_price = find_price.get_attribute('innerHTML')

        print(f"Cryptocurrency price is {crypto_price}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()


url_binance = "https://www.binance.com/en"
accept_locator_binance = (By.ID, "onetrust-accept-btn-handler")
price_locator_binance = (
    By.XPATH, "/html/body/div[3]/div/main/div[1]/div/div/div[2]/div[1]/div/div/a[1]/div[2]/div/div")

get_crypto_price(url_binance, accept_locator_binance, price_locator_binance)
