"""
LoginPage — Page Object for the SauceDemo login screen.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import Config


class LoginPage(BasePage):
    # Locators — defined once, reused everywhere
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def load(self):
        """Navigate to the login page."""
        self.open(Config.BASE_URL)
        return self

    def login(self, username: str, password: str):
        """Perform login with the given credentials."""
        self.type_text(self.USERNAME_FIELD, username)
        self.type_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
        # Return InventoryPage to enable fluent chaining (e.g. login().add_to_cart())
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def has_error(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE)
