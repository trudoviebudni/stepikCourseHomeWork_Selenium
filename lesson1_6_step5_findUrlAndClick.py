import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

base_link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(base_link)

    url = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = browser.find_element(By.LINK_TEXT, url)
    link.click()

    first_name = browser.find_element(By.NAME, "first_name")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.NAME, "last_name")
    last_name.send_keys("Petrov")
    city = browser.find_element(By.CSS_SELECTOR, ".city")
    city.send_keys("Smolensk")
    country = browser.find_element(By.ID, "country")
    country.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    time.sleep(15)
    browser.quit()
