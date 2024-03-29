import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def calc(x):
    return math.log(abs(12 * math.sin(int(x))))


link = 'https://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(x))

# Прокрутка с помощью javascript
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    browser.execute_script("arguments[0].scrollIntoView(true);", button)

#
# # Прокрутка с помощью Keys
#     browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END) #или Home если наверх
# # Убрать футер
#     browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)
#

    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()

    button.click()

finally:
    time.sleep(5)
    browser.quit()
