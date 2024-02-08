import time, traceback, random

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

try:
    # options = uc.ChromeOptions()
    # options.headless = True
    # options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
    # options.add_argument("--disable-extensions")
 
    driver = uc.Chrome()

    driver.delete_all_cookies()

    # Open BKMS
    driver.get("https://in.bookmyshow.com")
    time.sleep(random.uniform(1, 2))

    # Select city | Selects by class_name (not optimal)
    city_field = driver.find_element(By.CLASS_NAME, "bwc__sc-1iyhybo-6.ilhhay")
    city_name = "Vellore"
    city_field.send_keys(city_name)
    time.sleep(random.uniform(0.5, 1))
    driver.find_element(By.CLASS_NAME, "bwc__sc-ttnkwg-14.flGQbT").click()
    time.sleep(random.uniform(0.75, 1.25))

    # Find search box | Selects by XML path (better)
    search_box = driver.find_element(By.XPATH, "//*[@id=\"4\"]")
    search_box.click()
    time.sleep(random.uniform(0.5,0.75))

    # Search film
    input_field = driver.find_element(By.XPATH, "//*[@id=\"super-container\"]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div/div/div/input")
    filmname = "Teri Baaton Mein Aisa Uljha Jiya" 
    input_field.send_keys(filmname)
    time.sleep(random.uniform(0.5, 1))
    driver.find_element(By.CLASS_NAME, "bwc__sc-1iyhybo-13.kqrJYR").click()
    time.sleep(random.uniform(0.5, 1))
    driver.find_element(By.XPATH, "//button[contains(., 'Book tickets')]").click()  # Selects dynamically (even better)
    time.sleep(1000)


except Exception as e:
    print(e)
    # traceback.print_exc()

finally:
    driver.delete_all_cookies()
    driver.quit()

