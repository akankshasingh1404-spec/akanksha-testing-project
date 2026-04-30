"""
Inventory Tests — demonstrates:
  • End-to-end workflow (login → add to cart → verify)
  • Fluent page chaining
  • Multiple assertions across pages
"""
import pytest
from pages.login_page import LoginPage
from config.config import Config


class TestInventory:
    """Test suite for inventory page interactions."""

    @pytest.fixture(autouse=True)
    def login_setup(self, driver):
        """Auto-login before each test in this class."""
        self.inventory_page = (
            LoginPage(driver).load().login(Config.VALID_USER, Config.VALID_PASSWORD)
        )

    @pytest.mark.smoke
    @pytest.mark.ui
    def test_add_single_item_to_cart(self):
        """Verify a single item can be added to the cart."""
        self.inventory_page.add_item_to_cart("sauce-labs-backpack")
        assert self.inventory_page.get_cart_count() == 1

    @pytest.mark.regression
    @pytest.mark.ui
    def test_add_multiple_items_to_cart(self):
        """Verify multiple items update the cart count correctly."""
        self.inventory_page.add_item_to_cart("sauce-labs-backpack")
        self.inventory_page.add_item_to_cart("sauce-labs-bike-light")
        self.inventory_page.add_item_to_cart("sauce-labs-bolt-t-shirt")

        assert self.inventory_page.get_cart_count() == 3

    @pytest.mark.e2e
    @pytest.mark.ui
    def test_cart_persists_after_navigation(self):
        """E2E: add item, navigate to cart, verify it's there."""
        self.inventory_page.add_item_to_cart("sauce-labs-backpack")
        cart_page = self.inventory_page.open_cart()

        assert cart_page.is_loaded()
        assert cart_page.get_cart_items_count() == 1
