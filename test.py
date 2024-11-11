from selenium import webdriver

# Initialize the Firefox driver
driver = webdriver.Firefox()

# Open a webpage
driver.get("http://www.nepaldigisys.com")

# Print the title of the page
print(driver.title)

# Close the browser
# driver.quit()
