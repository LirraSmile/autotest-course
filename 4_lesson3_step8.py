from selenium import webdriver
import os
import time

#Задача: заполнить текстовые поля, загрузить файл, нажать на кнопку

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("tester@m.ru")

    #находим элемент, который прикрепляет файл
    button1 = browser.find_element_by_name("file")
    #Получаем руть к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'test.txt')
    #button1.click() не нужен
    button1.send_keys(file_path)

    # Отправляем заполненную форму
    button2 = browser.find_element_by_css_selector("button.btn")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()