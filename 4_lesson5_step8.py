from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import math

#Задача: нажать на кнопку, когда на странице появится нужная цена

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    
    browser.get(link)

    #Ждем, когда цена станет равной "$100", после чего нажимаем на кнопку

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),'$100'))
    button1 = browser.find_element_by_id("book")
    button1.click()

    #Находим элемент на странице
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    
    #Производим вычисления
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    #Передаем результат вычислений в форму
    y = calc(x)
    input_value = browser.find_element_by_class_name("form-control")
    input_value.send_keys(y)

    button2 = browser.find_element_by_xpath("//button[@type='submit']")
    button2.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла