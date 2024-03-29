import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#2 версии страницы регистрации. Одна из них с багом
#link = "https://suninjuly.github.io/registration1.html"
link = "https://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
# подбираю уникальные селекторы
    first_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")

    first_name.send_keys("a")
    last_name.send_keys("a")
    email.send_keys("a")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(2)

    assert "Congratulations! You have successfully registered!" == browser.find_element(By.TAG_NAME, "h1").text

finally:
    time.sleep(5)
    browser.quit()