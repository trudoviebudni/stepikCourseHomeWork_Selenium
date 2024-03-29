import time
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
# импортирую Keys, чтобы взаимодействовать с клавишами
from selenium.webdriver.common.keys import Keys


# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(3)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://www.google.com")
time.sleep(3)

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# Ищем поле для ввода текста
textarea = driver.find_element(By.CLASS_NAME, "gLFyf")

# Напишем текст ответа в найденное поле
textarea.send_keys("Привет гугл")
time.sleep(3)

# Найдем кнопку, которая отправляет введенное решение
# submit_button = driver.find_element(By.NAME, "btnK")

# Нажать кнопку Enter
textarea.send_keys(Keys.RETURN)
time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()
