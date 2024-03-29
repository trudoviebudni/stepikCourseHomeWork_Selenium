import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return math.log(abs(12 * math.sin(int(x))))


link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    current_window = browser.current_window_handle
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(1)

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))
    time.sleep(1)

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(1)

    alert = browser.switch_to.alert
    alert_text = alert.text.split(': ')[-1]
    alert.accept()
    time.sleep(1)

    browser.switch_to.window(current_window)
    browser.execute_script('alert("GOOD FUCKING JOB - " + arguments[0]);', alert_text)

finally:
    time.sleep(5)
    browser.quit()