import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def calc(x, y):
    return str(x + y)


link = 'http://suninjuly.github.io/selects2.html'
# link = 'http://suninjuly.github.io/selects2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.CSS_SELECTOR, '#num1').text)
    y = int(browser.find_element(By.CSS_SELECTOR, '#num2').text)

    dropdown = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))
    dropdown.select_by_value(calc(x, y))

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    time.sleep(5)
    browser.quit()
