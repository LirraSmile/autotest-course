from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

#Сценарий автотеста: добавить товар в корзину, перейти в корзину, оформить заказ.

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"

try:
    browser = webdriver.Chrome()
    
    browser.get(link)
    #Не получилось найти на главной странице элемент Все товары, поэтому начала сразу со страницы с товарами
    #browser.find_element_by_class_name("dropdowm-menu").find_element_by_css_selector("li:nth-child(0)").click()

    #Нажимаем на изображение товара, чтобы перецти в карточку товара
    product = browser.find_element_by_class_name("image_container")
    product.click()

    #Нажимаем на кнопку добавить в корзину в карточке товара
    button = browser.find_element_by_class_name("btn-add-to-basket")
    button.click()

    time.sleep(2) #на всякий случай, чтобы товар успел добавиться в корзину
    button_busket = browser.find_element_by_class_name("btn-group")
    #нажимаем на кнопку Посмотреть корзину
    #Не получилось найти кнопку Посмотреть корзину, которая появляется после того, как товар добавлен в корзину
    #button_basket = browser.find_element(By.XPATH, "//div[@id='messages]'/div['alert-info']/div['alertinner']/p[2]/a[1]]")
    #button_busket = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='messages]'/div['alert-info']/div['alertinner']/p[2]/a[1]]")))
    button_busket.click()
    #browser.find_elements_by_css_selector(".alertinner > p:nth-clild(1) > a:nth-clild(1)")

    #Нажимаем кнопку Оформить заказ в корзине
    button_order = browser.find_element_by_class_name("btn-primary")
    button_order.click()

    #Заполняем обязательные поля на странице Кто вы?
    input_email = browser.find_element_by_xpath("//input[@type='email']")
    input_email.send_keys("example@m.ru")
    #баг, что нельзя пройти, не заполнив поле пароля, заполняем )
    input_password = browser.find_element_by_xpath("//input[@type='password']")
    input_password.send_keys("123")
    button_submit = browser.find_element_by_xpath("//button[@type='submit']")
    button_submit.click()
    #Заполняем обязательные для оформления заказа поля
    input_fisrtname = browser.find_element_by_id("id_first_name")
    input_fisrtname.send_keys("Marina")
    input_secondname = browser.find_element_by_id("id_last_name")
    input_secondname.send_keys("Ivanova")
    input_address = browser.find_element_by_id("id_line1")
    input_address.send_keys("Moscow, Lenina 1")
    input_city = browser.find_element_by_id("id_line4")
    input_city.send_keys("Moscow")
    input_postcode = browser.find_element_by_id("id_postcode")
    input_postcode.send_keys("660000")
    #Не получилось выбрать элемент через библиотеку Select
    #select = Select(browser.find_element_by_tag_name("select"))
    #select.select_by_value("RU")
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("[value='RU']").click()

    button_submit = browser.find_element_by_xpath("//button[@type='submit']")
    button_submit.click()

    #Нажимаем на кнопку Продолжить
    button_prewiew = browser.find_element_by_id("view_preview")
    button_prewiew.click()

    #Нажимаем на кнопку Разместить заказ
    button_final = browser.find_element_by_id("place-order")
    button_final.click()   


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла