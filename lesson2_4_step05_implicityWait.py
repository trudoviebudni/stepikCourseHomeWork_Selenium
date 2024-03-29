import time

from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'https://suninjuly.github.io/wait1.html'


try:
    browser = webdriver.Chrome()
    #в течение 5 сек каждые 0.5 сек будет проверяться возможность исполнения команды, прежде чем скрипт упадет
    browser.implicitly_wait(5)
    browser.get(link)

    browser.find_element(By.ID, 'verify').click()

    assert "successful" in browser.find_element(By.ID, 'verify_message').text

finally:
    time.sleep(5)
    browser.quit()