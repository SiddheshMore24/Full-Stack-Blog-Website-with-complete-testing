@echo off
echo ========================================
echo Selenium WebDriver Test Setup and Runner
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ and try again
    pause
    exit /b 1
)

echo Python found. Checking version...
python --version

echo.
echo ========================================
echo Installing Required Packages
echo ========================================
echo.

REM Install required packages
echo Installing Selenium WebDriver and dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo ERROR: Failed to install required packages
    echo Please check your internet connection and try again
    pause
    exit /b 1
)

echo.
echo ========================================
echo Package Installation Complete
echo ========================================
echo.

REM Check if XAMPP/WAMP is running
echo Checking if Blogger application is accessible...
curl -s -o nul -w "%%{http_code}" http://localhost/Blogger/login.php
if errorlevel 1 (
    echo WARNING: Cannot access http://localhost/Blogger/login.php
    echo Please ensure:
    echo 1. XAMPP/WAMP server is running
    echo 2. Blogger application is in the correct directory
    echo 3. Apache service is started
    echo.
    echo Continuing with tests anyway...
    echo.
)

echo.
echo ========================================
echo Running Selenium WebDriver Tests
echo ========================================
echo.

REM Run all tests
echo Starting test execution...
python run_tests.py

echo.
echo ========================================
echo Test Execution Complete
echo ========================================
echo.
echo Press any key to exit...
pause >nul
