import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAppE2E(unittest.TestCase):
    def setUp(self):
        # Set Chrome options

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox') # Disables the sandbox for all process types that are normally sandboxed.
        options.add_argument('--disable-dev-shm-usage') # Overcomes limited resource problems.
        options.add_argument('--disable-gpu') # Applicable to windows os only
        options.add_argument('--remote-debugging-port=9222')


        self.driver = webdriver.Remote(
            command_executor='http://chrome:4444/wd/hub',
            options=options)
        self.driver.get("http://web:5000/")

    def test_add_and_delete_item(self):
        # you can use the driver to find elements in the page
        # example:
        input_field = self.driver.find_element(by='name', value='item')
        # this refers to the 'name="item"' attribute of the html element
        # checkout the rest of the methods in the documentation:
        # https://selenium-python.readthedocs.io/locating-elements.html
        # print(self.driver.page_source)
        
        # after you select your element, you can send it a key press:
        input_field.send_keys('New E2E Item')
        input_field.send_keys(Keys.RETURN)
        
        # and you can use the rest of the assetion methods as well:
        self.assertIn('New E2E Item', self.driver.page_source)

        # after inserting an item, you can also delete it:
        delete_button = self.driver.find_element(by='link text', value='Delete')
        delete_button.click()
        self.assertNotIn('New E2E Item', self.driver.page_source)

        # # quit the driver
        # self.driver.quit()
        pass
    
    def test_update_item(self):

        # add an item first
        input_field = self.driver.find_element(by='name', value='item')
        input_field.send_keys('New E2E Item')
        input_field.send_keys(Keys.RETURN)

        # check if the item is added
        self.assertIn('New E2E Item', self.driver.page_source)

        # then update it
        update_input_field = self.driver.find_element(by='name', value='new_item')
        update_input_field.send_keys('Updated E2E Item')
        update_button = self.driver.find_element(by='xpath', value='/html/body/div[1]/ul/li[1]/form/button')
        update_button.click()

        # check if the item is updated
        self.assertIn('Updated E2E Item', self.driver.page_source)
        pass
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()