"""
InventoryPage — Page Object for the products listing page after login.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    PRODUCT_TITLE = (By.CLASS_NAME, "title")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def is_loaded(self) -> bool:
        """Verify the inventory page loaded successfully."""
        return self.is_visible(self.INVENTORY_CONTAINER) and "inventory" in self.get_current_url()

    def get_page_title(self) -> str:
        return self.get_text(self.PRODUCT_TITLE)

    def add_item_to_cart(self, item_name: str):
        """Add a specific product to the cart by name."""
        # Locator built dynamically based on item name
        locator = (By.ID, f"add-to-cart-{item_name.lower().replace(' ', '-')}")
        self.click(locator)
        return self

    def get_cart_count(self) -> int:
        """Returns number of items in cart, or 0 if badge not visible."""
        if self.is_visible(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def open_cart(self):
        self.click(self.CART_ICON)
        from pages.cart_page import CartPage
        return CartPage(self.driver)
