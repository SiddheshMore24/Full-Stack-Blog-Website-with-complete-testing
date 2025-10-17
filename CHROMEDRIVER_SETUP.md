# ChromeDriver Setup Guide

## 🚨 Issue: `OSError: [WinError 193] %1 is not a valid Win32 application`

This error occurs when ChromeDriver is not properly installed or incompatible with your system.

## 🔧 Solution Steps

### Step 1: Check Chrome Browser
1. Open Chrome browser
2. Go to `chrome://version/`
3. Note your Chrome version (e.g., 120.0.6099.109)

### Step 2: Download Compatible ChromeDriver
1. Go to https://chromedriver.chromium.org/downloads
2. Download ChromeDriver that matches your Chrome version
3. Extract the `chromedriver.exe` file

### Step 3: Install ChromeDriver (Choose ONE method)

#### Method A: Add to System PATH (Recommended)
1. Copy `chromedriver.exe` to a folder (e.g., `C:\chromedriver\`)
2. Add this folder to your Windows PATH:
   - Press `Win + R`, type `sysdm.cpl`, press Enter
   - Click "Environment Variables"
   - Under "System Variables", find "Path" and click "Edit"
   - Click "New" and add `C:\chromedriver\`
   - Click "OK" to save

#### Method B: Place in Project Folder
1. Copy `chromedriver.exe` to your Blogger project folder
2. The test will automatically find it

#### Method C: Use WebDriver Manager (Automatic)
1. Run: `pip install --upgrade webdriver-manager`
2. The updated test code will handle this automatically

### Step 4: Test the Setup
Run the diagnostic script:
```bash
python test_chrome_setup.py
```

### Step 5: Run Your Tests
Once ChromeDriver is working:
```bash
python run_tests.py login
```

## 🐛 Alternative Solutions

### If ChromeDriver still doesn't work:

1. **Try Edge WebDriver instead:**
   ```bash
   pip install msedge-selenium-tools
   ```

2. **Use Firefox WebDriver:**
   ```bash
   pip install geckodriver-autoinstaller
   ```

3. **Check Windows Defender:**
   - Windows Defender might be blocking ChromeDriver
   - Add ChromeDriver folder to Windows Defender exclusions

4. **Run as Administrator:**
   - Try running PowerShell as Administrator
   - Then run the tests

## 🔍 Quick Fix Commands

```bash
# Update webdriver-manager
pip install --upgrade webdriver-manager

# Clear webdriver-manager cache
pip uninstall webdriver-manager
pip install webdriver-manager

# Test Chrome setup
python test_chrome_setup.py
```

## 📞 Still Having Issues?

1. Check if you have multiple Python installations
2. Ensure you're using the correct Python environment
3. Try running in a virtual environment:
   ```bash
   python -m venv selenium_env
   selenium_env\Scripts\activate
   pip install -r requirements.txt
   python run_tests.py login
   ```

## ✅ Success Indicators

When everything works, you should see:
- Chrome browser opens automatically
- Navigates to `http://localhost/Blogger/login.php`
- Tests run and show PASSED/FAILED results
- Browser closes after each test
