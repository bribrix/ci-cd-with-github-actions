from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import unittest

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
        self.driver.maximize_window()
        time.sleep(2)

    def test_add_update_delete_item(self):
        # Add item
        input_item = self.driver.find_element(By.NAME, 'item')
        input_item.send_keys('New E2E Item')
        button_add = self.driver.find_element(By.XPATH, '//button[text()="Add"]')
        button_add.click()
        self.assertIn('New E2E Item', self.driver.page_source)

        # Update item
        input_update = self.driver.find_element(By.NAME, 'new_item')
        input_update.send_keys('Updated E2E Item')
        button_update = self.driver.find_element(By.XPATH, '//button[text()="Update"]' )
        button_update.click()
        self.assertIn('Updated E2E Item', self.driver.page_source)
        
        # Delete item
        button_delete = self.driver.find_element(By.XPATH, '//a[text()="Delete"]')
        button_delete.click()
        self.assertNotIn('New E2E Item', self.driver.page_source)
        self.assertNotIn('Updated E2E Item', self.driver.page_source)

    def tearDown(self):
        time.sleep(10)  # 10 seconds of delay to see the result
        self.driver.quit()

if __name__ == '__main__':
    # Run the tests
    unittest.main()
