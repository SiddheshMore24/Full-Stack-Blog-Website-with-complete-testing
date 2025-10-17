#!/bin/bash

echo "========================================"
echo "Selenium WebDriver Test Setup and Runner"
echo "========================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed or not in PATH"
    echo "Please install Python 3.7+ and try again"
    exit 1
fi

echo "Python found. Checking version..."
python3 --version

echo
echo "========================================"
echo "Installing Required Packages"
echo "========================================"
echo

# Install required packages
echo "Installing Selenium WebDriver and dependencies..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install required packages"
    echo "Please check your internet connection and try again"
    exit 1
fi

echo
echo "========================================"
echo "Package Installation Complete"
echo "========================================"
echo

# Check if XAMPP/WAMP is running
echo "Checking if Blogger application is accessible..."
if curl -s -o /dev/null -w "%{http_code}" http://localhost/Blogger/login.php | grep -q "200"; then
    echo "✅ Blogger application is accessible"
else
    echo "⚠️  WARNING: Cannot access http://localhost/Blogger/login.php"
    echo "Please ensure:"
    echo "1. XAMPP/WAMP server is running"
    echo "2. Blogger application is in the correct directory"
    echo "3. Apache service is started"
    echo
    echo "Continuing with tests anyway..."
    echo
fi

echo
echo "========================================"
echo "Running Selenium WebDriver Tests"
echo "========================================"
echo

# Run all tests
echo "Starting test execution..."
python3 run_tests.py

echo
echo "========================================"
echo "Test Execution Complete"
echo "========================================"
echo

# Make the script executable
chmod +x setup_and_run.sh
