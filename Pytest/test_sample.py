import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
import time

@pytest.fixture(scope="module")
def driver():
    # Initialize the WebDriver (e.g., using Chrome)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()  # Teardown step after all tests

def test_login(driver):
    # Open the target login page
    driver.get("https://opensource-demo.orangehrmlive.com/")  # Replace with the actual URL

    # Debugging step: Print the current URL to verify navigation
    print("Current URL:", driver.current_url)

    # Wait for the username input field to be visible
    try:
        username_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        print("Username input located successfully.")
    except TimeoutException:
        pytest.fail("Error: Timed out waiting for the username input to become visible.")

    # Locate and interact with the username input field
    username_input.send_keys("Admin")  # Replace with your test username

    # Wait for and locate the password input field
    try:
        password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        print("Password input located successfully.")
    except TimeoutException:
        pytest.fail("Error: Timed out waiting for the password input to become visible.")

    # Enter the password
    password_input.send_keys("admin123")  # Replace with your test password

    # Wait for and locate the login button
    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "orangehrm-login-button"))
        )
        print("Login button located successfully.")
    except (TimeoutException, NoSuchElementException):
        pytest.fail("Error: Unable to locate the login button.")

    # Click the login button
    try:
        login_button.click()
        print("Login button clicked.")
    except ElementNotInteractableException:
        pytest.fail("Error: Login button is not interactable.")

    
    # Optional: Wait for a few seconds to observe the result (not ideal for production scripts)
    time.sleep(5)

    # Optional debugging: Print page title or other status messages
    print("Page Title after login:", driver.title)
