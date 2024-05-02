from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение переменной х
    import math
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Ввести объект в текстовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)



    # Тыкнуть чекбокс и радиобаттон
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    #Скроллим страницу
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()


    # ждем загрузки страницы
    time.sleep(1)
    # тыкнуть Сабмит
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # Скроллим страницу
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()