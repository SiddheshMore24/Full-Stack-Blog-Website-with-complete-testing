"""
Simple test to verify login functionality works
"""

import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestSimpleLogin(unittest.TestCase):
    """Simple login test"""
    
    def setUp(self):
        """Set up WebDriver"""
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
    
    def tearDown(self):
        """Clean up"""
        if self.driver:
            self.driver.quit()
    
    def test_valid_login(self):
        """Test valid admin login"""
        print("Testing valid admin login...")
        
        # Navigate to login page
        self.driver.get("http://localhost/Blogger/login.php")
        
        # Select admin role
        role_select = self.wait.until(EC.presence_of_element_located((By.NAME, "role")))
        role_select.send_keys("admin")
        
        # Enter valid email
        email_field = self.driver.find_element(By.NAME, "email")
        email_field.send_keys("siddheshmore00@gmail.com")
        
        # Enter valid password
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys("@@@@@@")
        
        # Click login button
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Wait for redirect to dashboard
        self.wait.until(EC.url_contains("dashboard.php"))
        
        # Verify we're on dashboard
        self.assertIn("dashboard.php", self.driver.current_url)
        self.assertIn("Admin Dashboard", self.driver.title)
        
        print("Valid login test - PASSED")
    
    def test_invalid_login(self):
        """Test invalid admin login"""
        print("Testing invalid admin login...")
        
        # Navigate to login page
        self.driver.get("http://localhost/Blogger/login.php")
        
        # Select admin role
        role_select = self.wait.until(EC.presence_of_element_located((By.NAME, "role")))
        role_select.send_keys("admin")
        
        # Enter invalid email
        email_field = self.driver.find_element(By.NAME, "email")
        email_field.send_keys("invalid@example.com")
        
        # Enter any password
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys("wrongpassword")
        
        # Click login button
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Wait a moment for potential error message
        time.sleep(2)
        
        # Check if we're still on login page or if error message appears
        current_url = self.driver.current_url
        if "login.php" in current_url:
            print("Invalid login test - PASSED (stayed on login page)")
        else:
            print(f"Unexpected redirect to: {current_url}")

if __name__ == "__main__":
    unittest.main()
