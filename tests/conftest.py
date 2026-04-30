"""
Pytest configuration — fixtures, hooks, screenshot-on-failure.
"""
import os
import pytest
from datetime import datetime
from utils.driver_factory import DriverFactory
from config.config import Config


def pytest_addoption(parser):
    """Add CLI options for browser and headless mode."""
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser: chrome, firefox, edge")
    parser.addoption("--headless", action="store_true", default=False,
                     help="Run in headless mode")


@pytest.fixture(scope="function")
def driver(request):
    """
    Provides a fresh WebDriver instance per test (function scope).
    Tears down automatically after each test.
    """
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = DriverFactory.get_driver(browser=browser, headless=headless)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook that captures a screenshot on test failure
    and embeds it into the HTML report.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs(Config.SCREENSHOTS_DIR, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"{Config.SCREENSHOTS_DIR}/{item.name}_{timestamp}.png"
            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved: {screenshot_path}")
