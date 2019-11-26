from selenium import webdriver
import math
import time

#Задача: открыть страницу, нажать на кнопку, в модальном окне нажать на confirm,
#на новой странице находим элемент, производим вычисления,
#заполняем форму и нажимаем кнопку

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем на кнопку
    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    #Находим элемент на странице, забираем значение атрибутов
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text  
    
    #Производим вычисления
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Передаем результат вычислений в форму
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    #нажимаем на кнопку
    button2 = browser.find_element_by_class_name("btn")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()