import time
import math

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

login = ""  # your login
password = ""  # your password
params = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.mark.parametrize('link', params)
def test_login_and_submit_answer_stepik(browser, link):
    # авторизация
    browser.get(link)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'auth=login')]"))
    ).click() # кнопка входа

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='login']"))
    ).send_keys(login) # вводим логин

    browser.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password) # вводим пароль
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(browser, 10).until_not(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.auth-modal'))
    ) # Ждем пока поп-ап с авторизацией исчезнет

    # Пробуем сбросить поле ввода ответа, на случай если в него уже было что-то отправлено
    try:
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.again-btn"))
        ).click() # жмем кнопку "Решить снова"/"Сбросить"

        WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-popup__overlay footer button:nth-child(1)"))
        ).click() # если попадаем на сброс, подтверждаем его
        # Так как после закрытия поп-ап окна поле ввода не блокируется, то писать в него можно еще до момента
        # фактического сброса поля. Поэтому пришлось делать принудительную остановку для ожидания сброса.
        time.sleep(1)
    except (TimeoutException, NoSuchElementException):
        pass

    # Ждем пока поле ввода станет доступным
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.textarea"))
    ).send_keys(math.log(int(time.time())))  # считаем и вписываем ответ

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
    ).click() # отправляем ответ

    option_feedback = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.smart-hints p"))
    ).text # ловим фидбэк
    assert option_feedback == "Correct!"
