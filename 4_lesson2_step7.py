from selenium import webdriver
import math
import time 

#Задача найти на странице элемент-картинку, 
# взять занчение атрибута valuex, подставить в выражение, 
# вычислить, отметить чекбокс и radiobutton и нажать на кнопку

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #Находим элемент на странице, с помощью get_attribute забираем значение атрибута
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")   
    
    #Производим вычисления
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    #Передаем результат вычислений в форму
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    #Мщем и нажимает на нужный чекбокс
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()

    #Мщем и нажимаем на нужный radiobutton
    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла