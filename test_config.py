"""
Configuration file for Selenium WebDriver tests
Contains test data, URLs, and common settings
"""

# Base URL for the application
BASE_URL = "http://localhost/Blogger"

# Test URLs
LOGIN_URL = f"{BASE_URL}/login.php"
DASHBOARD_URL = f"{BASE_URL}/dashboard.php"
CREATE_BLOG_URL = f"{BASE_URL}/create_blog.php"

# Test Data
ADMIN_CREDENTIALS = {
    "email": "siddheshmore00@gmail.com",
    "password": "@@@@@@",
    "role": "admin"
}

# Mock test data for various scenarios
MOCK_ADMIN_DATA = {
    "valid": {
        "email": "admin@example.com",
        "password": "password123",
        "role": "admin"
    },
    "invalid_email": {
        "email": "invalid-email",
        "password": "password123",
        "role": "admin"
    },
    "invalid_password": {
        "email": "admin@example.com",
        "password": "wrongpassword",
        "role": "admin"
    },
    "empty_fields": {
        "email": "",
        "password": "",
        "role": "admin"
    }
}

MOCK_BLOG_DATA = {
    "valid": {
        "title": "Test Blog Title - Comprehensive Testing Guide",
        "subtitle": "A detailed guide to automated testing",
        "content": "This is a comprehensive blog post about automated testing with Selenium WebDriver. It covers various testing scenarios and best practices for web application testing.",
        "image_url": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800",
        "status": "published"
    },
    "invalid_title_short": {
        "title": "Hi",
        "subtitle": "Short title test",
        "content": "This content is long enough to pass validation requirements for blog content.",
        "image_url": "",
        "status": "draft"
    },
    "invalid_title_long": {
        "title": "A" * 151,  # 151 characters - exceeds limit
        "subtitle": "Long title test",
        "content": "This content is long enough to pass validation requirements for blog content.",
        "image_url": "",
        "status": "draft"
    },
    "invalid_content_short": {
        "title": "Valid Blog Title",
        "subtitle": "Short content test",
        "content": "Short",  # Less than 20 characters
        "image_url": "",
        "status": "draft"
    },
    "invalid_image_url": {
        "title": "Test Blog with Invalid Image",
        "subtitle": "Image URL test",
        "content": "This content is long enough to pass validation requirements for blog content.",
        "image_url": "not-a-valid-url",
        "status": "published"
    },
    "draft_blog": {
        "title": "Draft Blog Post - Testing Draft Functionality",
        "subtitle": "Testing draft status",
        "content": "This is a draft blog post created for testing purposes. It should be saved as draft and not published immediately.",
        "image_url": "",
        "status": "draft"
    }
}

# Browser settings
BROWSER_SETTINGS = {
    "implicit_wait": 10,
    "page_load_timeout": 30,
    "window_size": (1920, 1080)
}

# Expected messages and text
EXPECTED_MESSAGES = {
    "login_success": "Dashboard",
    "login_error_all_fields": "All fields are required.",
    "login_error_invalid_email": "Invalid email format.",
    "login_error_invalid_password": "Invalid password. Please try again.",
    "login_error_user_not_found": "User not found. Please check your email or sign up.",
    "blog_created_success": "blog_created",
    "blog_title_short": "Title must be between 5 and 150 characters.",
    "blog_content_short": "Content must be at least 20 characters long.",
    "blog_invalid_image": "Please enter a valid Image URL.",
    "blog_invalid_status": "Invalid status selected.",
    "blog_db_error": "Something went wrong while saving the blog."
}
