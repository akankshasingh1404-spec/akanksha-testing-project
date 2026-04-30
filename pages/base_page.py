"""
BasePage — parent class for all Page Objects.
Encapsulates common actions: click, type, wait, get_text.
Demonstrates DRY principles and reusable web interactions.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config import Config
from utils.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    """Parent class for all Page Objects."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)

    def open(self, url: str):
        logger.info(f"Navigating to: {url}")
        self.driver.get(url)

    def find(self, locator):
        """Wait for element to be present and return it."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Wait for element to be clickable, then click."""
        logger.info(f"Clicking element: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text: str):
        """Wait for element, clear it, then type text."""
        logger.info(f"Typing into {locator}: {text}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator) -> str:
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_current_url(self) -> str:
        return self.driver.current_url
