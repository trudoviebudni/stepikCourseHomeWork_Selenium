import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    forms = browser.find_elements(By.TAG_NAME, "input")
    for form in forms:
        form.send_keys("a")

    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    time.sleep(10)
    browser.quit()