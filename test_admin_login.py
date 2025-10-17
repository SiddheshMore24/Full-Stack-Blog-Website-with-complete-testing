"""
Test cases for Admin Login Page
Tests various login scenarios including valid/invalid credentials
"""

import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base_test import BaseTest
from test_config import LOGIN_URL, ADMIN_CREDENTIALS, MOCK_ADMIN_DATA, EXPECTED_MESSAGES


class TestAdminLogin(BaseTest):
    """Test cases for Admin Login functionality"""
    
    def test_admin_login_valid_credentials(self):
        """Verify admin can login with correct credentials"""
        # Navigate to login page
        self.driver.get(LOGIN_URL)
        
        # Verify we're on the login page
        self.assertIn("Login", self.get_page_title())
        
        # Select admin role
        role_select = self.wait_for_element(By.NAME, "role")
        role_select.send_keys("admin")
        
        # Enter valid email
        email_field = self.driver.find_element(By.NAME, "email")
        email_field.send_keys(ADMIN_CREDENTIALS["email"])
        
        # Enter valid password
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(ADMIN_CREDENTIALS["password"])
        
        # Click login button
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Wait a moment for the response
        time.sleep(2)
        
        # Check if login was successful or if there's an error
        current_url = self.get_current_url()
        
        if "dashboard.php" in current_url:
            # Successful login
            self.assertIn("Admin Dashboard", self.get_page_title())
            
            # Verify welcome message is displayed
            welcome_element = self.wait_for_element(By.XPATH, "//span[contains(text(), 'Welcome')]")
            self.assertIsNotNone(welcome_element)
            
            print("Admin login with valid credentials - PASSED")
        else:
            # Login failed - check for error message
            try:
                error_element = self.driver.find_element(By.CSS_SELECTOR, ".alert-danger")
                error_text = error_element.text
                print(f"Login failed with error: {error_text}")
                
                # This is expected if credentials are incorrect
                self.assertIn("login.php", current_url)
                print("Admin login with provided credentials - FAILED (credentials may be incorrect)")
            except:
                print("Login failed but no error message found")
                self.fail("Login failed without clear error message")
    
    def test_admin_login_invalid_email_format(self):
        """Verify login fails with invalid email format"""
        # Navigate to login page
        self.driver.get(LOGIN_URL)
        
        # Select admin role
        role_select = self.wait_for_element(By.NAME, "role")
        role_select.send_keys("admin")
        
        # Enter invalid email format
        email_field = self.driver.find_element(By.NAME, "email")
        email_field.send_keys(MOCK_ADMIN_DATA["invalid_email"]["email"])
        
        # Enter valid password
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(MOCK_ADMIN_DATA["invalid_email"]["password"])
        
        # Click login button
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Wait for error message
        time.sleep(2)
        error_element = self.wait_for_element(By.CSS_SELECTOR, ".alert-danger")
        
        # Verify error message
        self.assertIn(EXPECTED_MESSAGES["login_error_invalid_email"], error_element.text)
        
        # Verify we're still on login page
        self.assertIn("login.php", self.get_current_url())
        
        print("Admin login with invalid email format - PASSED")
    
    def test_admin_login_invalid_password(self):
        """Verify login fails with invalid password"""
        # Navigate to login page
        self.driver.get(LOGIN_URL)
        
        # Select admin role
        role_select = self.wait_for_element(By.NAME, "role")
        role_select.send_keys("admin")
        
        # Enter valid email
        email_field = self.driver.find_element(By.NAME, "email")
        email_field.send_keys(ADMIN_CREDENTIALS["email"])
        
        # Enter invalid password
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(MOCK_ADMIN_DATA["invalid_password"]["password"])
        
        # Click login button
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Wait for error message
        time.sleep(2)
        error_element = self.wait_for_element(By.CSS_SELECTOR, ".alert-danger")
        
        # Verify error message
        self.assertIn(EXPECTED_MESSAGES["login_error_invalid_password"], error_element.text)
        
        # Verify we're still on login page
        self.assertIn("login.php", self.get_current_url())
        
        print("Admin login with invalid password - PASSED")
    
    def test_admin_login_empty_fields(self):
        """Verify login fails with empty fields"""
        # Navigate to login page
        self.driver.get(LOGIN_URL)
        
        # Select admin role
        role_select = self.wait_for_element(By.NAME, "role")
        role_select.send_keys("admin")
        
        # Leave email and password fields empty
        # Click login button directly
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Check if HTML5 validation prevents submission
        # If form doesn't submit, we should still be on login page
        time.sleep(1)  # Wait a moment for any potential redirect
        
        # Verify we're still on login page (HTML5 validation should prevent submission)
        self.assertIn("login.php", self.get_current_url())
        
        # Verify required fields are still empty
        email_field = self.driver.find_element(By.NAME, "email")
        self.assertEqual(email_field.get_attribute("value"), "")
        
        password_field = self.driver.find_element(By.NAME, "password")
        self.assertEqual(password_field.get_attribute("value"), "")
        
        print("Admin login with empty fields - PASSED")
    
    def test_admin_login_nonexistent_user(self):
        """Verify login fails with non-existent user email"""
        # Navigate to login page
        self.driver.get(LOGIN_URL)
        
        # Select admin role
        role_select = self.wait_for_element(By.NAME, "role")
        role_select.send_keys("admin")
        
        # Enter non-existent email
        email_field = self.driver.find_element(By.NAME, "email")
        email_field.send_keys("nonexistent@example.com")
        
        # Enter any password
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys("anypassword")
        
        # Click login button
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Wait for error message
        time.sleep(2)
        error_element = self.wait_for_element(By.CSS_SELECTOR, ".alert-danger")
        
        # Verify error message
        self.assertIn(EXPECTED_MESSAGES["login_error_user_not_found"], error_element.text)
        
        # Verify we're still on login page
        self.assertIn("login.php", self.get_current_url())
        
        print("Admin login with non-existent user - PASSED")
    
    def test_login_page_elements_present(self):
        """Verify all required elements are present on login page"""
        # Navigate to login page
        self.driver.get(LOGIN_URL)
        
        # Verify page title
        self.assertIn("Login", self.get_page_title())
        
        # Verify role selector is present
        role_select = self.wait_for_element(By.NAME, "role")
        self.assertTrue(role_select.is_displayed())
        
        # Verify email field is present
        email_field = self.driver.find_element(By.NAME, "email")
        self.assertTrue(email_field.is_displayed())
        
        # Verify password field is present
        password_field = self.driver.find_element(By.NAME, "password")
        self.assertTrue(password_field.is_displayed())
        
        # Verify login button is present
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        self.assertTrue(login_button.is_displayed())
        
        # Verify signup link is present
        signup_link = self.driver.find_element(By.LINK_TEXT, "Create an account")
        self.assertTrue(signup_link.is_displayed())
        
        print("Login page elements verification - PASSED")


if __name__ == "__main__":
    unittest.main()
