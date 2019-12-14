import pytest
from selenium import webdriver
import math
import time

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_should_see_hint(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)

    answer_field = browser.find_element_by_class_name("textarea")
    answer = str(math.log(int(time.time())))
    answer_field.send_keys(answer)

    button = browser.find_element_by_class_name("submit-submission")
    button.click()

    real_result_element = browser.find_element_by_class_name("smart-hints__hint")

    assert "Correct!" in real_result_element.text, "Result is not correct"