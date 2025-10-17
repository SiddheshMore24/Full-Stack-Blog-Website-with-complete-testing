"""
Simple script to test Chrome WebDriver setup
This will help identify and fix ChromeDriver issues
"""

import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_chrome_setup():
    """Test Chrome WebDriver setup with multiple approaches"""
    print("Testing Chrome WebDriver Setup")
    print("=" * 50)
    
    # Test 1: Check if Chrome is installed
    print("1. Checking Chrome browser installation...")
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run headless for testing
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Try to create driver without service first
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.google.com")
        print("Chrome browser is installed and accessible")
        driver.quit()
        return True
    except Exception as e:
        print(f"Chrome browser issue: {e}")
    
    # Test 2: Try with webdriver-manager
    print("\n2. Testing webdriver-manager...")
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get("https://www.google.com")
        print("WebDriver Manager works correctly")
        driver.quit()
        return True
    except Exception as e:
        print(f"WebDriver Manager issue: {e}")
    
    # Test 3: Try with system ChromeDriver
    print("\n3. Testing system ChromeDriver...")
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Try common ChromeDriver paths
        possible_paths = [
            "chromedriver.exe",
            "chromedriver",
            r"C:\chromedriver\chromedriver.exe",
            r"C:\Program Files\chromedriver\chromedriver.exe",
            r"C:\Users\{}\chromedriver\chromedriver.exe".format(os.getenv('USERNAME', 'user'))
        ]
        
        for path in possible_paths:
            try:
                if os.path.exists(path):
                    service = Service(path)
                    driver = webdriver.Chrome(service=service, options=chrome_options)
                    driver.get("https://www.google.com")
                    print(f"System ChromeDriver found at: {path}")
                    driver.quit()
                    return True
            except:
                continue
        
        print("No system ChromeDriver found")
    except Exception as e:
        print(f"System ChromeDriver issue: {e}")
    
    print("\n" + "=" * 50)
    print("TROUBLESHOOTING SUGGESTIONS:")
    print("1. Make sure Google Chrome is installed")
    print("2. Download ChromeDriver from: https://chromedriver.chromium.org/")
    print("3. Add ChromeDriver to your system PATH")
    print("4. Or place chromedriver.exe in your project folder")
    print("5. Try running: pip install --upgrade webdriver-manager")
    
    return False

def test_blogger_access():
    """Test if Blogger application is accessible"""
    print("\nTesting Blogger Application Access")
    print("=" * 50)
    
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("http://localhost/Blogger/login.php")
        
        if "Login" in driver.title:
            print("Blogger application is accessible")
            print(f"   Page title: {driver.title}")
            print(f"   URL: {driver.current_url}")
            driver.quit()
            return True
        else:
            print(f"Unexpected page title: {driver.title}")
            driver.quit()
            return False
            
    except Exception as e:
        print(f"Cannot access Blogger application: {e}")
        print("   Make sure XAMPP/WAMP is running")
        print("   Check if Blogger is in the correct directory")
        return False

if __name__ == "__main__":
    print("Chrome WebDriver Diagnostic Tool")
    print("=" * 60)
    
    # Test Chrome setup
    chrome_ok = test_chrome_setup()
    
    if chrome_ok:
        # Test Blogger access
        blogger_ok = test_blogger_access()
        
        if blogger_ok:
            print("\nAll tests passed! You can now run the main test suite.")
            print("   Run: python run_tests.py login")
        else:
            print("\nChrome works but Blogger app is not accessible.")
    else:
        print("\nChrome WebDriver setup needs to be fixed first.")
    
    print("\n" + "=" * 60)
