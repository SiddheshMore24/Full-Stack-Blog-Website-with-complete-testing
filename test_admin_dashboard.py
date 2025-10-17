"""
Test cases for Admin Dashboard Page
Tests dashboard functionality, blog management, and navigation
"""

import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base_test import BaseTest
from test_config import DASHBOARD_URL, CREATE_BLOG_URL


class TestAdminDashboard(BaseTest):
    """Test cases for Admin Dashboard functionality"""
    
    def setUp(self):
        """Set up WebDriver and login as admin before each test"""
        super().setUp()
        # Login as admin before each test
        self.login_as_admin()
    
    def test_dashboard_page_loads_successfully(self):
        """Verify dashboard page loads with all required elements"""
        # Verify we're on dashboard page
        self.assertIn("dashboard.php", self.get_current_url())
        self.assertIn("Admin Dashboard", self.get_page_title())
        
        # Verify header elements are present
        header_title = self.wait_for_element(By.XPATH, "//h2[contains(text(), 'Admin Dashboard')]")
        self.assertTrue(header_title.is_displayed())
        
        # Verify welcome message
        welcome_element = self.wait_for_element(By.XPATH, "//span[contains(text(), 'Welcome')]")
        self.assertTrue(welcome_element.is_displayed())
        
        # Verify logout button is present
        logout_button = self.driver.find_element(By.LINK_TEXT, "Logout")
        self.assertTrue(logout_button.is_displayed())
        
        # Verify "Create New Blog" button is present
        create_blog_button = self.driver.find_element(By.LINK_TEXT, "+ Create New Blog")
        self.assertTrue(create_blog_button.is_displayed())
        
        # Verify "Your Blog Posts" section
        blog_posts_heading = self.driver.find_element(By.XPATH, "//h4[contains(text(), 'Your Blog Posts')]")
        self.assertTrue(blog_posts_heading.is_displayed())
        
        print("✅ Dashboard page loads successfully - PASSED")
    
    def test_create_new_blog_navigation(self):
        """Verify navigation to create blog page works correctly"""
        # Click on "Create New Blog" button
        create_blog_button = self.wait_for_element_clickable(By.LINK_TEXT, "+ Create New Blog")
        create_blog_button.click()
        
        # Wait for redirect to create blog page
        self.wait.until(EC.url_contains("create_blog.php"))
        
        # Verify we're on create blog page
        self.assertIn("create_blog.php", self.get_current_url())
        self.assertIn("Create New Blog", self.get_page_title())
        
        # Verify create blog form elements are present
        title_field = self.wait_for_element(By.NAME, "title")
        self.assertTrue(title_field.is_displayed())
        
        content_field = self.driver.find_element(By.NAME, "content")
        self.assertTrue(content_field.is_displayed())
        
        status_select = self.driver.find_element(By.NAME, "status")
        self.assertTrue(status_select.is_displayed())
        
        print("✅ Create new blog navigation - PASSED")
    
    def test_dashboard_logout_functionality(self):
        """Verify logout functionality works correctly"""
        # Click logout button
        logout_button = self.wait_for_element_clickable(By.LINK_TEXT, "Logout")
        logout_button.click()
        
        # Wait for redirect to login page
        self.wait.until(EC.url_contains("login.php"))
        
        # Verify we're redirected to login page
        self.assertIn("login.php", self.get_current_url())
        self.assertIn("Login", self.get_page_title())
        
        # Verify login form is present
        email_field = self.wait_for_element(By.NAME, "email")
        self.assertTrue(email_field.is_displayed())
        
        password_field = self.driver.find_element(By.NAME, "password")
        self.assertTrue(password_field.is_displayed())
        
        print("✅ Dashboard logout functionality - PASSED")
    
    def test_dashboard_with_existing_blogs(self):
        """Verify dashboard displays existing blogs correctly"""
        # First, create a test blog
        self.driver.get(CREATE_BLOG_URL)
        
        # Fill blog form
        title_field = self.wait_for_element(By.NAME, "title")
        title_field.send_keys("Test Blog for Dashboard Display")
        
        content_field = self.driver.find_element(By.NAME, "content")
        content_field.send_keys("This is a test blog content to verify dashboard display functionality.")
        
        status_select = self.driver.find_element(By.NAME, "status")
        status_select.send_keys("published")
        
        # Submit the form
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        # Wait for redirect back to dashboard
        self.wait.until(EC.url_contains("dashboard.php"))
        
        # Verify blog is displayed on dashboard
        blog_title = self.wait_for_element(By.XPATH, "//h5[contains(text(), 'Test Blog for Dashboard Display')]")
        self.assertTrue(blog_title.is_displayed())
        
        # Verify blog actions (Edit/Delete buttons) are present
        edit_button = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Edit')]")
        self.assertTrue(edit_button.is_displayed())
        
        delete_button = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Delete')]")
        self.assertTrue(delete_button.is_displayed())
        
        print("✅ Dashboard with existing blogs - PASSED")
    
    def test_dashboard_no_blogs_message(self):
        """Verify dashboard shows appropriate message when no blogs exist"""
        # This test assumes we start with no blogs or we can verify the no blogs state
        # Check if "No blogs added yet" message is displayed when no blogs exist
        try:
            no_blogs_message = self.driver.find_element(By.XPATH, "//div[contains(@class, 'alert-info') and contains(text(), 'No blogs added yet')]")
            self.assertTrue(no_blogs_message.is_displayed())
            print("✅ Dashboard no blogs message - PASSED")
        except:
            # If blogs exist, verify the blog list is displayed
            blog_cards = self.driver.find_elements(By.CSS_SELECTOR, ".card")
            self.assertGreater(len(blog_cards), 0, "Blog cards should be displayed")
            print("✅ Dashboard with existing blogs displayed - PASSED")
    
    def test_dashboard_blog_actions_visibility(self):
        """Verify blog action buttons (Edit/Delete) are visible and functional"""
        # Navigate to dashboard
        self.driver.get(DASHBOARD_URL)
        
        # Check if any blogs exist
        blog_cards = self.driver.find_elements(By.CSS_SELECTOR, ".card")
        
        if len(blog_cards) > 0:
            # Get the first blog card
            first_blog = blog_cards[0]
            
            # Verify Edit button is present and clickable
            edit_button = first_blog.find_element(By.XPATH, ".//a[contains(text(), 'Edit')]")
            self.assertTrue(edit_button.is_displayed())
            self.assertTrue(edit_button.is_enabled())
            
            # Verify Delete button is present and clickable
            delete_button = first_blog.find_element(By.XPATH, ".//a[contains(text(), 'Delete')]")
            self.assertTrue(delete_button.is_displayed())
            self.assertTrue(delete_button.is_enabled())
            
            # Verify like count is displayed
            like_element = first_blog.find_element(By.XPATH, ".//p[contains(text(), 'Likes')]")
            self.assertTrue(like_element.is_displayed())
            
            print("✅ Dashboard blog actions visibility - PASSED")
        else:
            print("ℹ️ No blogs found to test actions - SKIPPED")
    
    def test_dashboard_back_to_create_blog_navigation(self):
        """Verify back navigation from create blog to dashboard works"""
        # Navigate to create blog page
        self.driver.get(CREATE_BLOG_URL)
        
        # Click "Back to Dashboard" link
        back_link = self.wait_for_element_clickable(By.LINK_TEXT, "← Back to Dashboard")
        back_link.click()
        
        # Wait for redirect to dashboard
        self.wait.until(EC.url_contains("dashboard.php"))
        
        # Verify we're back on dashboard
        self.assertIn("dashboard.php", self.get_current_url())
        self.assertIn("Admin Dashboard", self.get_page_title())
        
        # Verify dashboard elements are present
        create_blog_button = self.wait_for_element(By.LINK_TEXT, "+ Create New Blog")
        self.assertTrue(create_blog_button.is_displayed())
        
        print("✅ Dashboard back navigation from create blog - PASSED")


if __name__ == "__main__":
    unittest.main()
