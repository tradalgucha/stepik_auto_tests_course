from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Посчитать сумму

    def calc(x1, x2):
        return str(int(x1) + int(x2))

    #  Считать значение для переменной x1:
    x1_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x1 = x1_element.text
    #  Считать значение для переменной x2:
    x2_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    x2 = x2_element.text
    #  Посчитать математическую функцию от x
    y = calc(x1, x2)

    #  Выбрать ответ в дропдауне.
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)  # ищем элемент с текстом "y"


    # ждем загрузки страницы
    time.sleep(1)

    # тыкнуть Сабмит
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()