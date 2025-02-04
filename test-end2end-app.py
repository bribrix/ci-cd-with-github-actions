from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import unittest

class TestAppE2E(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("disable-infobars")
        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.get("http://127.0.0.1:5000/")

    def tearDown(self):
        time.sleep(10)  # 10 seconds of delay to see the result
        self.driver.quit()

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

if __name__ == '__main__':
    # Run the tests
    unittest.main()
