import pytest
from selenium import webdriver


# позволяет автоматически импортировать фикстуры из данного модуля в разные тесты
@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
