from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = " http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение переменной х
    import math
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # Находим элемент(сундук)
    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    # получаем аттрибут валуекс
    x_valuex = x_element.get_attribute("valuex")
    x = x_valuex #значение не .text
    y = calc(x)

    # Ввести объект в текстовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)


    # Тыкнуть чекбокс и радиобаттон
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()


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