from selenium import webdriver
import math
import time 

#Задача найти на странице элемент-кнопку, нажать,
#на второй странице решить пример, заполнить текстовое поле,
#нажать на кнопку

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_xpath("//button[@type='submit']")
    button1.click()

    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла