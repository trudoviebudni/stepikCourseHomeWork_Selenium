import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return math.log(abs(12 * math.sin(int(x))))


link = 'https://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    browser.switch_to.alert.accept()

    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(x))

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    time.sleep(5)
    browser.quit()


