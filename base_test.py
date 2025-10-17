"""
Base test class for Selenium WebDriver tests
Contains common setup and teardown methods
"""

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from test_config import BROWSER_SETTINGS, BASE_URL


class BaseTest(unittest.TestCase):
    """Base test class with common setup and teardown methods"""
    
    @classmethod
    def setUpClass(cls):
        """Set up the WebDriver for the entire test class"""
        cls.driver = None
        cls.wait = None
    
    def setUp(self):
        """Set up WebDriver before each test method"""
        # Chrome options for better testing
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--disable-extensions")
        # Uncomment the next line to run in headless mode
        # chrome_options.add_argument("--headless")
        
        # Initialize WebDriver (Chrome is working based on diagnostic)
        self.driver = webdriver.Chrome(options=chrome_options)
        
        # Set timeouts
        self.driver.implicitly_wait(BROWSER_SETTINGS["implicit_wait"])
        self.driver.set_page_load_timeout(BROWSER_SETTINGS["page_load_timeout"])
        
        # Initialize WebDriverWait
        self.wait = WebDriverWait(self.driver, 10)
        
        # Navigate to base URL
        self.driver.get(BASE_URL)
    
    def tearDown(self):
        """Clean up after each test method"""
        if self.driver:
            self.driver.quit()
    
    def login_as_admin(self, email="siddheshmore00@gmail.com", password="@@@@@@", role="admin"):
        """Helper method to login as admin"""
        self.driver.get(f"{BASE_URL}/login.php")
        
        # Select role
        role_select = self.wait.until(EC.presence_of_element_located((By.NAME, "role")))
        role_select.send_keys(role)
        
        # Enter email
        email_field = self.driver.find_element(By.NAME, "email")
        email_field.clear()
        email_field.send_keys(email)
        
        # Enter password
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.clear()
        password_field.send_keys(password)
        
        # Click login button
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Wait for redirect to dashboard
        self.wait.until(EC.url_contains("dashboard.php"))
    
    def logout_admin(self):
        """Helper method to logout admin"""
        logout_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
        logout_link.click()
        
        # Wait for redirect to login page
        self.wait.until(EC.url_contains("login.php"))
    
    def wait_for_element(self, by, value, timeout=10):
        """Helper method to wait for element to be present"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
    
    def wait_for_element_clickable(self, by, value, timeout=10):
        """Helper method to wait for element to be clickable"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
    
    def wait_for_text_in_element(self, by, value, text, timeout=10):
        """Helper method to wait for specific text in element"""
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((by, value), text)
        )
    
    def take_screenshot(self, name):
        """Helper method to take screenshot"""
        self.driver.save_screenshot(f"screenshot_{name}.png")
    
    def get_page_title(self):
        """Helper method to get current page title"""
        return self.driver.title
    
    def get_current_url(self):
        """Helper method to get current URL"""
        return self.driver.current_url
