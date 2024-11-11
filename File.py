from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your WebDriver
driver_path = "path_to_your_webdriver"

# Initialize the WebDriver (Here using Chrome)
driver = webdriver.Chrome(executable_path=driver_path)

# Open Google's homepage
driver.get("https://www.google.com")

# Find the search box element by its name attribute
search_box = driver.find_element(By.NAME, "q")

# Enter the search term "Automation testing" and submit
search_box.send_keys("Automation testing")
search_box.send_keys(Keys.RETURN)

# Wait for the page to load results
time.sleep(3)

# Optionally, print the title of the page to verify the test
print("Page title after search:", driver.title)

# Close the browser window
driver.quit()
