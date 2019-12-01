link = "http://selenium1py.pythonanywhere.com/"

def test_new_user(browser):
    browser.get(link)
    login_link = browser.find_element_by_id("login_link")
    login_link.click()

    new_user = "btester3@m.ru"
    password = "Tester123"

    email_field = browser.find_element_by_id("id_registration-email")
    email_field.send_keys(new_user)
    password_field = browser.find_element_by_id("id_registration-password1")
    password_field.send_keys(password)
    password_2_field = browser.find_element_by_id("id_registration-password2")
    password_2_field.send_keys(password)
    button_registration = browser.find_element_by_name("registration_submit")
    button_registration.click()
    
    assert browser.find_element_by_class_name("alert-success"), "Registration isn't successful"
