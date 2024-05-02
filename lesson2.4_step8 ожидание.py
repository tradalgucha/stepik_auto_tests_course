from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()
browser.get(" http://suninjuly.github.io/explicit_wait2.html")
# Устанавливаем условия ожидания пока цена не станет 100
button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
# тыкаем Book
button1 = browser.find_element(By.CSS_SELECTOR, "#book")
button1.click()

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
# тыкнуть Сабмит
button2 = browser.find_element(By.CSS_SELECTOR, "#solve")
button2.click()
# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()


