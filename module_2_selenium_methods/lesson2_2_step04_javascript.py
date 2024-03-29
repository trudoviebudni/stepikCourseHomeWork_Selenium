import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    # browser.execute_script("document.title='Script executing';")
    # browser.execute_script("alert('Robots at work');")
    # browser.execute_script("document.title='Script executing';alert('Robots at work');")

    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    time.sleep(4)
    browser.quit()