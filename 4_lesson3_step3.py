from selenium import webdriver
from selenium.webdriver.support.ui import Select #Специальный класс из библиотеки WebDriver
import math
import time 

#Задача: найти на странице элементы, сложить их, найти в выпадающем списке сумму и нажать кнопку

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #Находим элемент на странице, забираем значение атрибутов
    x_element = browser.find_element_by_id("num1")
    x = x_element.text  
    
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    
    #Производим вычисления
    def calc(x,y):
        return str(int(x)+int(y))

    s = calc(x,y)

    #открываем выпадающий список и находим значение в нём
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(s)

    #нажимаем на кнопку

    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла