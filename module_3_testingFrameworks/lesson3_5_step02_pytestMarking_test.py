import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


# создал файл pytest.ini в корневом каталоге проекта. Там указал все маркировки. Пример для запуска: pytest -vsm smoke
class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    # 2 марки
    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page_1(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    # встроенная марка (пропустить тест)
    @pytest.mark.skip
    def test_guest_should_see_login_link_1(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    # мы знаем что тест падает, и пока разрабы фиксят баг, мы помечаем тест таким образом.
    # Но не скипаем его, чтобы не забыть
    # Когда баг починят, мы это узнаем, так как теперь тест будет отмечен как
    # XPASS (“unexpectedly passing” — неожиданно проходит). И метку можно будет удалить.\
    # параметр запуска тестов reason (-rx) позволяет увидеть причину почему помеченный xfail тест упал
    # pytest -sv -rx .\module_3_testingFrameworks\lesson3_5_step02_pytestMarking_test.py

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")

    # здесь я поменял селектор на правильный. Результат будет xpass вместо xfailed
    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page_1(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")
"""
pytest -s -v -m "not smoke" # Запустить все тесты без метки smoke
pytest -s -v -m "smoke or regression" # Запустить все smoke и regression тесты
pytest -s -v -m "smoke and win10" # Запустить тесты имеющие одновременно метки smoke и win10
pytest -sv -rx # помеченные xfail тесты будут выдавать причину падения в консоле
pytest -rX -v test_fixture10b.py # большая X позволяет получить подробную инфу по xPass тестам
"""