"""
Test cases for Blog Creation Page
Tests blog creation functionality with various validation scenarios
"""

import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base_test import BaseTest
from test_config import CREATE_BLOG_URL, MOCK_BLOG_DATA, EXPECTED_MESSAGES


class TestBlogCreation(BaseTest):
    """Test cases for Blog Creation functionality"""
    
    def setUp(self):
        """Set up WebDriver and login as admin before each test"""
        super().setUp()
        # Login as admin before each test
        self.login_as_admin()
        # Navigate to create blog page
        self.driver.get(CREATE_BLOG_URL)
    
    def test_create_blog_valid_data(self):
        """Verify blog creation with valid data works correctly"""
        # Fill in valid blog data
        title_field = self.wait_for_element(By.NAME, "title")
        title_field.send_keys(MOCK_BLOG_DATA["valid"]["title"])
        
        subtitle_field = self.driver.find_element(By.NAME, "subtitle")
        subtitle_field.send_keys(MOCK_BLOG_DATA["valid"]["subtitle"])
        
        content_field = self.driver.find_element(By.NAME, "content")
        content_field.send_keys(MOCK_BLOG_DATA["valid"]["content"])
        
        image_url_field = self.driver.find_element(By.NAME, "image_url")
        image_url_field.send_keys(MOCK_BLOG_DATA["valid"]["image_url"])
        
        status_select = self.driver.find_element(By.NAME, "status")
        status_select.send_keys(MOCK_BLOG_DATA["valid"]["status"])
        
        # Submit the form
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        # Wait for redirect to dashboard
        self.wait.until(EC.url_contains("dashboard.php"))
        
        # Verify we're redirected to dashboard
        self.assertIn("dashboard.php", self.get_current_url())
        self.assertIn("Admin Dashboard", self.get_page_title())
        
        # Verify the blog appears on dashboard
        blog_title = self.wait_for_element(By.XPATH, f"//h5[contains(text(), '{MOCK_BLOG_DATA['valid']['title']}')]")
        self.assertTrue(blog_title.is_displayed())
        
        print("✅ Create blog with valid data - PASSED")
    
    def test_create_blog_title_too_short(self):
        """Verify blog creation fails with title too short"""
        # Fill in blog data with short title
        title_field = self.wait_for_element(By.NAME, "title")
        title_field.send_keys(MOCK_BLOG_DATA["invalid_title_short"]["title"])
        
        subtitle_field = self.driver.find_element(By.NAME, "subtitle")
        subtitle_field.send_keys(MOCK_BLOG_DATA["invalid_title_short"]["subtitle"])
        
        content_field = self.driver.find_element(By.NAME, "content")
        content_field.send_keys(MOCK_BLOG_DATA["invalid_title_short"]["content"])
        
        status_select = self.driver.find_element(By.NAME, "status")
        status_select.send_keys(MOCK_BLOG_DATA["invalid_title_short"]["status"])
        
        # Submit the form
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        # Wait for error message
        error_element = self.wait_for_element(By.CSS_SELECTOR, ".alert-warning")
        
        # Verify error message
        self.assertIn(EXPECTED_MESSAGES["blog_title_short"], error_element.text)
        
        # Verify we're still on create blog page
        self.assertIn("create_blog.php", self.get_current_url())
        
        print("✅ Create blog with title too short - PASSED")
    
    def test_create_blog_title_too_long(self):
        """Verify blog creation fails with title too long"""
        # Fill in blog data with long title
        title_field = self.wait_for_element(By.NAME, "title")
        title_field.send_keys(MOCK_BLOG_DATA["invalid_title_long"]["title"])
        
        subtitle_field = self.driver.find_element(By.NAME, "subtitle")
        subtitle_field.send_keys(MOCK_BLOG_DATA["invalid_title_long"]["subtitle"])
        
        content_field = self.driver.find_element(By.NAME, "content")
        content_field.send_keys(MOCK_BLOG_DATA["invalid_title_long"]["content"])
        
        status_select = self.driver.find_element(By.NAME, "status")
        status_select.send_keys(MOCK_BLOG_DATA["invalid_title_long"]["status"])
        
        # Submit the form
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        # Wait for error message
        error_element = self.wait_for_element(By.CSS_SELECTOR, ".alert-warning")
        
        # Verify error message
        self.assertIn(EXPECTED_MESSAGES["blog_title_short"], error_element.text)
        
        # Verify we're still on create blog page
        self.assertIn("create_blog.php", self.get_current_url())
        
        print("✅ Create blog with title too long - PASSED")
    
    def test_create_blog_content_too_short(self):
        """Verify blog creation fails with content too short"""
        # Fill in blog data with short content
        title_field = self.wait_for_element(By.NAME, "title")
        title_field.send_keys(MOCK_BLOG_DATA["invalid_content_short"]["title"])
        
        subtitle_field = self.driver.find_element(By.NAME, "subtitle")
        subtitle_field.send_keys(MOCK_BLOG_DATA["invalid_content_short"]["subtitle"])
        
        content_field = self.driver.find_element(By.NAME, "content")
        content_field.send_keys(MOCK_BLOG_DATA["invalid_content_short"]["content"])
        
        status_select = self.driver.find_element(By.NAME, "status")
        status_select.send_keys(MOCK_BLOG_DATA["invalid_content_short"]["status"])
        
        # Submit the form
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        # Wait for error message
        error_element = self.wait_for_element(By.CSS_SELECTOR, ".alert-warning")
        
        # Verify error message
        self.assertIn(EXPECTED_MESSAGES["blog_content_short"], error_element.text)
        
        # Verify we're still on create blog page
        self.assertIn("create_blog.php", self.get_current_url())
        
        print("✅ Create blog with content too short - PASSED")
    
    def test_create_blog_invalid_image_url(self):
        """Verify blog creation fails with invalid image URL"""
        # Fill in blog data with invalid image URL
        title_field = self.wait_for_element(By.NAME, "title")
        title_field.send_keys(MOCK_BLOG_DATA["invalid_image_url"]["title"])
        
        subtitle_field = self.driver.find_element(By.NAME, "subtitle")
        subtitle_field.send_keys(MOCK_BLOG_DATA["invalid_image_url"]["subtitle"])
        
        content_field = self.driver.find_element(By.NAME, "content")
        content_field.send_keys(MOCK_BLOG_DATA["invalid_image_url"]["content"])
        
        image_url_field = self.driver.find_element(By.NAME, "image_url")
        image_url_field.send_keys(MOCK_BLOG_DATA["invalid_image_url"]["image_url"])
        
        status_select = self.driver.find_element(By.NAME, "status")
        status_select.send_keys(MOCK_BLOG_DATA["invalid_image_url"]["status"])
        
        # Submit the form
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        # Wait for error message
        error_element = self.wait_for_element(By.CSS_SELECTOR, ".alert-warning")
        
        # Verify error message
        self.assertIn(EXPECTED_MESSAGES["blog_invalid_image"], error_element.text)
        
        # Verify we're still on create blog page
        self.assertIn("create_blog.php", self.get_current_url())
        
        print("✅ Create blog with invalid image URL - PASSED")
    
    def test_create_blog_draft_status(self):
        """Verify blog creation with draft status works correctly"""
        # Fill in blog data with draft status
        title_field = self.wait_for_element(By.NAME, "title")
        title_field.send_keys(MOCK_BLOG_DATA["draft_blog"]["title"])
        
        subtitle_field = self.driver.find_element(By.NAME, "subtitle")
        subtitle_field.send_keys(MOCK_BLOG_DATA["draft_blog"]["subtitle"])
        
        content_field = self.driver.find_element(By.NAME, "content")
        content_field.send_keys(MOCK_BLOG_DATA["draft_blog"]["content"])
        
        status_select = self.driver.find_element(By.NAME, "status")
        status_select.send_keys(MOCK_BLOG_DATA["draft_blog"]["status"])
        
        # Submit the form
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        # Wait for redirect to dashboard
        self.wait.until(EC.url_contains("dashboard.php"))
        
        # Verify we're redirected to dashboard
        self.assertIn("dashboard.php", self.get_current_url())
        
        # Verify the draft blog appears on dashboard
        blog_title = self.wait_for_element(By.XPATH, f"//h5[contains(text(), '{MOCK_BLOG_DATA['draft_blog']['title']}')]")
        self.assertTrue(blog_title.is_displayed())
        
        # Verify status shows as draft
        status_element = self.driver.find_element(By.XPATH, "//p[contains(text(), 'Status:') and contains(text(), 'draft')]")
        self.assertTrue(status_element.is_displayed())
        
        print("✅ Create blog with draft status - PASSED")
    
    def test_create_blog_page_elements_present(self):
        """Verify all required elements are present on create blog page"""
        # Verify page title
        self.assertIn("Create New Blog", self.get_page_title())
        
        # Verify form elements are present
        title_field = self.wait_for_element(By.NAME, "title")
        self.assertTrue(title_field.is_displayed())
        
        subtitle_field = self.driver.find_element(By.NAME, "subtitle")
        self.assertTrue(subtitle_field.is_displayed())
        
        content_field = self.driver.find_element(By.NAME, "content")
        self.assertTrue(content_field.is_displayed())
        
        image_url_field = self.driver.find_element(By.NAME, "image_url")
        self.assertTrue(image_url_field.is_displayed())
        
        status_select = self.driver.find_element(By.NAME, "status")
        self.assertTrue(status_select.is_displayed())
        
        # Verify submit button is present
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        self.assertTrue(submit_button.is_displayed())
        
        # Verify back to dashboard link is present
        back_link = self.driver.find_element(By.LINK_TEXT, "← Back to Dashboard")
        self.assertTrue(back_link.is_displayed())
        
        print("✅ Create blog page elements verification - PASSED")
    
    def test_create_blog_empty_required_fields(self):
        """Verify blog creation fails with empty required fields"""
        # Leave title and content fields empty
        # Fill only optional fields
        subtitle_field = self.driver.find_element(By.NAME, "subtitle")
        subtitle_field.send_keys("Optional subtitle")
        
        status_select = self.driver.find_element(By.NAME, "status")
        status_select.send_keys("draft")
        
        # Submit the form
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        # The form should not submit due to HTML5 validation
        # Verify we're still on create blog page
        self.assertIn("create_blog.php", self.get_current_url())
        
        # Verify required fields are still empty
        title_field = self.driver.find_element(By.NAME, "title")
        self.assertEqual(title_field.get_attribute("value"), "")
        
        content_field = self.driver.find_element(By.NAME, "content")
        self.assertEqual(content_field.get_attribute("value"), "")
        
        print("✅ Create blog with empty required fields - PASSED")


if __name__ == "__main__":
    unittest.main()
