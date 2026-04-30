"""
CartPage — Page Object for the shopping cart page.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def get_cart_items_count(self) -> int:
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)

    def is_loaded(self) -> bool:
        return "cart" in self.get_current_url()
