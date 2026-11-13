
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTests(unittest.TestCase):

    def setUp(self):
        # Open Chrome browser
        self.driver = webdriver.Chrome()

        # Open our local login webpage
        self.driver.get("file:///Users/yashikanagpal/MCA-DevOps-Lab/q2-selenium/login.html")

    def test_valid_login(self):
        driver = self.driver

        # Enter valid username and password
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")

        # Click Login
        driver.find_element(By.ID, "loginBtn").click()

        # Check the expected success message
        message = driver.find_element(By.ID, "message").text

        self.assertEqual(message, "Login successful!")

        print("\nTest 1: Valid Login - PASS")

    def test_invalid_login(self):
        driver = self.driver

        # Enter incorrect password
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("wrong123")

        # Click Login
        driver.find_element(By.ID, "loginBtn").click()

        # Check the expected error message
        message = driver.find_element(By.ID, "message").text

        self.assertEqual(message, "Invalid username or password")

        print("\nTest 2: Invalid Login - PASS")

    def tearDown(self):
        # Close Chrome browser
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)

