"""
Main test runner script for Selenium WebDriver tests
Provides options to run individual test suites or all tests
"""

import unittest
import sys
import os
from test_admin_login import TestAdminLogin
from test_admin_dashboard import TestAdminDashboard
from test_blog_creation import TestBlogCreation


def run_all_tests():
    """Run all test suites"""
    print("Running All Selenium WebDriver Tests for Blogger Application")
    print("=" * 60)
    
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test cases from each module
    loader = unittest.TestLoader()
    test_suite.addTest(loader.loadTestsFromTestCase(TestAdminLogin))
    test_suite.addTest(loader.loadTestsFromTestCase(TestAdminDashboard))
    test_suite.addTest(loader.loadTestsFromTestCase(TestBlogCreation))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print(f"Test Summary:")
    print(f"   Tests Run: {result.testsRun}")
    print(f"   Failures: {len(result.failures)}")
    print(f"   Errors: {len(result.errors)}")
    print(f"   Success Rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    return result.wasSuccessful()


def run_login_tests():
    """Run only login tests"""
    print("Running Admin Login Tests")
    print("=" * 40)
    
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTest(loader.loadTestsFromTestCase(TestAdminLogin))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    return result.wasSuccessful()


def run_dashboard_tests():
    """Run only dashboard tests"""
    print("Running Admin Dashboard Tests")
    print("=" * 40)
    
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTest(loader.loadTestsFromTestCase(TestAdminDashboard))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    return result.wasSuccessful()


def run_blog_creation_tests():
    """Run only blog creation tests"""
    print("Running Blog Creation Tests")
    print("=" * 40)
    
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTest(loader.loadTestsFromTestCase(TestBlogCreation))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    return result.wasSuccessful()


def main():
    """Main function to handle command line arguments"""
    if len(sys.argv) > 1:
        test_type = sys.argv[1].lower()
        
        if test_type == "login":
            success = run_login_tests()
        elif test_type == "dashboard":
            success = run_dashboard_tests()
        elif test_type == "blog":
            success = run_blog_creation_tests()
        elif test_type == "all":
            success = run_all_tests()
        else:
            print("❌ Invalid test type. Use: login, dashboard, blog, or all")
            sys.exit(1)
    else:
        # Default: run all tests
        success = run_all_tests()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
