import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element(By.CSS_SELECTOR, '#peopleRule')
    people_checked = people_radio.get_attribute("checked")

    robot_radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    robot_checked = robot_radio.get_attribute("checked")

    time.sleep(10)
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button_disabled = button.get_attribute("disabled")

    assert button_disabled is not None, 'Radio button is not disabled after 10 sec'
    assert people_checked is not None, 'People radio is not selected by Default'
    assert robot_checked is None, 'Robot radio is selected by Default'

finally:
    browser.quit()

