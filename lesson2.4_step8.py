from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # код который нажимает на кнопку
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button = browser.find_element(By.ID, "book")
    button.click()
 
    # Считать значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    
    #Посчитать математическую функцию от x (код для этого приведён ниже)
    y = calc(x)
    
    # Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button1 = browser.find_element(By.ID,"solve")
    button1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()