"""
Debug script to check login page elements
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def debug_login_page():
    """Debug the login page to see actual elements"""
    print("Debugging Login Page Elements")
    print("=" * 40)
    
    # Setup Chrome
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Navigate to login page
        driver.get("http://localhost/Blogger/login.php")
        time.sleep(2)
        
        print(f"Page Title: {driver.title}")
        print(f"Current URL: {driver.current_url}")
        
        # Check for form elements
        print("\nForm Elements:")
        try:
            role_select = driver.find_element(By.NAME, "role")
            print(f"Role select found: {role_select.tag_name}")
        except:
            print("Role select NOT found")
        
        try:
            email_field = driver.find_element(By.NAME, "email")
            print(f"Email field found: {email_field.tag_name}")
        except:
            print("Email field NOT found")
        
        try:
            password_field = driver.find_element(By.NAME, "password")
            print(f"Password field found: {password_field.tag_name}")
        except:
            print("Password field NOT found")
        
        try:
            submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            print(f"Submit button found: {submit_button.tag_name}")
        except:
            print("Submit button NOT found")
        
        # Check for error messages
        print("\nError Message Elements:")
        try:
            error_elements = driver.find_elements(By.CSS_SELECTOR, ".alert-danger")
            print(f"Found {len(error_elements)} .alert-danger elements")
            for i, elem in enumerate(error_elements):
                print(f"  Error {i+1}: {elem.text}")
        except:
            print("No .alert-danger elements found")
        
        # Check for any alert elements
        try:
            alert_elements = driver.find_elements(By.CSS_SELECTOR, ".alert")
            print(f"Found {len(alert_elements)} .alert elements")
            for i, elem in enumerate(alert_elements):
                print(f"  Alert {i+1}: {elem.text}")
        except:
            print("No .alert elements found")
        
        # Check page source for clues
        print("\nPage Source Analysis:")
        page_source = driver.page_source
        if "alert-danger" in page_source:
            print("alert-danger class found in page source")
        if "error" in page_source.lower():
            print("'error' text found in page source")
        
        # Try to submit empty form
        print("\nTesting form submission:")
        try:
            submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            submit_button.click()
            time.sleep(2)
            
            # Check for error after submission
            error_elements = driver.find_elements(By.CSS_SELECTOR, ".alert-danger")
            if error_elements:
                print(f"Error message after submission: {error_elements[0].text}")
            else:
                print("No error message found after submission")
                
        except Exception as e:
            print(f"Error during form submission: {e}")
        
        input("Press Enter to close browser...")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    debug_login_page()
