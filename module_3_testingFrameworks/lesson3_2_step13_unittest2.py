import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration(unittest.TestCase):

    # неявная инициализация драйвера
    def setUp(self):
        self.driver = webdriver.Chrome()

    # неявное завершение работы драйвер
    def tearDown(self):
        self.driver.quit()

    def fill_registration_form(self, link):
        self.driver.get(link)

        # ожидание загрузки элементов формы
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.first_block .first')))

        self.driver.find_element(By.CSS_SELECTOR, 'div.first_block .first').send_keys('aa')
        self.driver.find_element(By.CSS_SELECTOR, 'div.first_block .second').send_keys('aa')
        self.driver.find_element(By.CSS_SELECTOR, 'div.first_block .third').send_keys('aa')
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # ожидание загрузки заголовка
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1')))
        return self.driver.find_element(By.CSS_SELECTOR, 'h1').text

    def test_registration_1(self):
        actual_result = self.fill_registration_form('https://suninjuly.github.io/registration1.html')
        self.assertEqual(actual_result, 'Congratulations! You have successfully registered!')

    def test_registration_2(self):
        actual_result = self.fill_registration_form('https://suninjuly.github.io/registration2.html')
        self.assertEqual(actual_result, 'Congratulations! You have successfully registered!')


if __name__ == "__main__":
    unittest.main()