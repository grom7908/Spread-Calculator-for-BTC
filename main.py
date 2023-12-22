import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.binance.com/en"
driver.get(url)
time.sleep(2)

find_accept1 = driver.find_element(By.ID, "onetrust-accept-btn-handler")
find_accept1.click()

find_btc_1 = driver.find_element(
    By.XPATH, "/html/body/div[3]/div/main/div[1]/div/div/div[2]/div[1]/div/div/a[1]/div[2]/div/div")
find_btc_1 = find_btc_1.get_attribute('innerHTML')
print("BTC price is " + find_btc_1)
