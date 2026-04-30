"""
WebDriver Factory — supports Chrome, Firefox, Edge with optional headless mode.
Demonstrates the Factory design pattern.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from config.config import Config
from utils.logger import get_logger

logger = get_logger(__name__)


class DriverFactory:
    """Creates WebDriver instances based on browser type and headless mode."""

    @staticmethod
    def get_driver(browser: str = None, headless: bool = None):
        browser = (browser or Config.DEFAULT_BROWSER).lower()
        headless = headless if headless is not None else Config.HEADLESS

        logger.info(f"Initializing {browser} driver (headless={headless})")

        if browser == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            driver = webdriver.Chrome(options=options)

        elif browser == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)

        elif browser == "edge":
            options = EdgeOptions()
            if headless:
                options.add_argument("--headless=new")
            driver = webdriver.Edge(options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
        driver.maximize_window()
        return driver
