import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# Open BKMS
driver.get("https://in.bookmyshow.com")
time.sleep(2)

# Select city, Vellore
city_field = driver.find_element(by=By.CLASS_NAME, value="bwc__sc-1iyhybo-6.ilhhay")
city_field.send_keys("Vellore")
time.sleep(1)
driver.find_element(by=By.CLASS_NAME, value="bwc__sc-ttnkwg-14.flGQbT").click()
time.sleep(2)


title = driver.title

