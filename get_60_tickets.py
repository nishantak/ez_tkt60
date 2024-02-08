import time, traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


try:
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    # Open BKMS
    driver.get("https://in.bookmyshow.com")
    time.sleep(1.25)

    # Select city | Selects by class_name (not optimal)
    city_field = driver.find_element(by=By.CLASS_NAME, value="bwc__sc-1iyhybo-6.ilhhay")
    city_name = "Vellore"
    city_field.send_keys(city_name)
    time.sleep(0.75)
    driver.find_element(by=By.CLASS_NAME, value="bwc__sc-ttnkwg-14.flGQbT").click()
    time.sleep(1)

    # Find search | Selects by XML path (optimal)
    search_box = driver.find_element(by=By.XPATH, value="//*[@id=\"4\"]")
    search_box.click()
    input_field = driver.find_element(by=By.XPATH, value="//*[@id=\"super-container\"]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div/div/div/input")
    # Search film
    filmname = "Teri Baaton Mein Aisa Uljha Jiya" 
    input_field.send_keys(filmname)
    time.sleep(1000)

except Exception as e:
    print(e)
    #traceback.print_exc()

finally:
    driver.quit()

