from selenium import webdriver
import time
import unittest

class TestFindElement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        link = "http://suninjuly.github.io/registration1.html"
        self.driver.get(link)

    
    def test_search_by_name(self):
        self.search_field = self.driver.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group first_class']/input[@class='form-control first']")
        self.search_field.send_keys("Ivan")
        self.search_surname = self.driver.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group second_class']/input[@class='form-control second']")
        self.search_surname.send_keys("Petrov")
        self.search_email = self.driver.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group third_class']/input[@class='form-control third']")
        self.search_email.send_keys("tester@m.ru")

        self.button = self.driver.find_element_by_css_selector("button.btn")
        self.button.click()
        self.driver.implicitly_wait(2)

        self.welcome_text_elt = self.driver.find_element_by_tag_name("h1")
        self.welcome_text = self.welcome_text_elt.text

        self.expected_text = "Congratulations! You have successfully registered!"

        self.assertEqual(self.welcome_text, self.expected_text, "Should be")
        self.driver.implicitly_wait(20)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

