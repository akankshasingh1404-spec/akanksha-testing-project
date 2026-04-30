"""
Centralized configuration for the test framework.
URLs, credentials, and timeouts live here — never hardcoded in tests.
"""
import os


class Config:
    # Application URLs
    BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
    API_BASE_URL = os.getenv("API_BASE_URL", "https://fakestoreapi.com")

    # Default test credentials (SauceDemo public test accounts)
    VALID_USER = os.getenv("TEST_USER", "standard_user")
    VALID_PASSWORD = os.getenv("TEST_PASSWORD", "secret_sauce")
    LOCKED_USER = "locked_out_user"
    PROBLEM_USER = "problem_user"

    # Timeouts (seconds)
    IMPLICIT_WAIT = 0          # We use explicit waits — never implicit
    EXPLICIT_WAIT = 10
    PAGE_LOAD_TIMEOUT = 30

    # Browser config
    DEFAULT_BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

    # Reporting
    REPORTS_DIR = "reports"
    SCREENSHOTS_DIR = "reports/screenshots"
