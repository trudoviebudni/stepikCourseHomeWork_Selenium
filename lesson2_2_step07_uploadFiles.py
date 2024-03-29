import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

misc_dir = os.path.abspath(os.path.dirname(__file__)) + "\\resourses"
file_path = os.path.join(misc_dir, "file.txt")

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    inputs_text = browser.find_elements(By.CSS_SELECTOR, '.form-group input[required]')
    for el in inputs_text:
        el.send_keys('aa')

    browser.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


finally:
    time.sleep(5)
    browser.quit()



