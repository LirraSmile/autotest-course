from selenium import webdriver
import math
import time 

#Задача: найти на странице элементы, сложить их, найти в выпадающем списке сумму и нажать кнопку

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #Находим элемент на странице, забираем значение атрибутов
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text  
    
    #Производим вычисления
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    #Скроллим стрпницу вниз, чтобы стали видны элементы
    # Передаем результат вычислений в форму
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)

    #Мщем и нажимает на нужный чекбокс
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()

    #Мщем и нажимаем на нужный radiobutton
    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()

    #нажимаем на кнопку
    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла