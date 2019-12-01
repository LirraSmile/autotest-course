link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_Basket_button(browser):
    browser.get(link)
    #Проверка, что кнопка добавления товара в корзину есть на странице
    assert browser.find_element_by_class_name("btn-add-to-basket"), "Evement wasn't found"
    