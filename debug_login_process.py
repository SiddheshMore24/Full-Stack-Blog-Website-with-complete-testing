"""
Debug script to check what happens during login process
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def debug_login_process():
    """Debug the login process step by step"""
    print("Debugging Login Process")
    print("=" * 40)
    
    # Setup Chrome
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Navigate to login page
        print("1. Navigating to login page...")
        driver.get("http://localhost/Blogger/login.php")
        time.sleep(2)
        
        print(f"   Page Title: {driver.title}")
        print(f"   Current URL: {driver.current_url}")
        
        # Fill in login form
        print("\n2. Filling login form...")
        
        # Select admin role
        role_select = driver.find_element(By.NAME, "role")
        role_select.send_keys("admin")
        print("   Role selected: admin")
        
        # Enter email
        email_field = driver.find_element(By.NAME, "email")
        email_field.send_keys("siddheshmore00@gmail.com")
        print("   Email entered: siddheshmore00@gmail.com")
        
        # Enter password
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("@@@@@@")
        print("   Password entered")
        
        # Submit form
        print("\n3. Submitting form...")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Wait and check what happens
        print("\n4. Waiting for response...")
        time.sleep(3)
        
        print(f"   Page Title after submit: {driver.title}")
        print(f"   Current URL after submit: {driver.current_url}")
        
        # Check for any error messages
        try:
            error_elements = driver.find_elements(By.CSS_SELECTOR, ".alert-danger")
            if error_elements:
                print(f"   Error message: {error_elements[0].text}")
            else:
                print("   No error message found")
        except:
            print("   Could not check for error messages")
        
        # Check page content
        print("\n5. Page content analysis:")
        page_source = driver.page_source.lower()
        
        if "dashboard" in page_source:
            print("   Dashboard content found in page")
        if "welcome" in page_source:
            print("   Welcome message found in page")
        if "admin" in page_source:
            print("   Admin content found in page")
        if "login" in page_source:
            print("   Login content still present")
        
        # Check if we can find dashboard elements
        try:
            dashboard_elements = driver.find_elements(By.XPATH, "//h2[contains(text(), 'Admin Dashboard')]")
            if dashboard_elements:
                print("   Admin Dashboard heading found")
            else:
                print("   Admin Dashboard heading NOT found")
        except:
            print("   Could not check for dashboard heading")
        
        input("Press Enter to close browser...")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    debug_login_process()
