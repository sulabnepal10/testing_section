import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import HtmlTestRunner

class GoogleSearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    
    def test_google_search(self):
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIn("Google", driver.title)  # Verify "Google" is in the title

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium with Python")
        search_box.send_keys(Keys.RETURN)


        # Step 3: Wait for the results to load and verify title change
        time.sleep(3)
        self.assertIn("Selenium with Python", driver.title)  # Check if the title contains the query

        first_result = driver.find_element(By.CSS_SELECTOR, "h3")
        first_result.click()

        time.sleep(5)
        # Assert that the page title has changed to something new after the click
        self.assertNotIn("Google Search", driver.title)

    def tearDown(self):
        self.driver.quit()
        print("Test is completed")


if __name__ == "__main__" :
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports/'))
