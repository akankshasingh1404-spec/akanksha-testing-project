"""
Login Tests — demonstrates:
  • Page Object Model usage
  • Data-driven testing via @pytest.mark.parametrize
  • Smoke / regression test markers
  • Negative testing (locked user, invalid credentials)
"""
import pytest
from pages.login_page import LoginPage
from config.config import Config


class TestLogin:
    """Test suite for SauceDemo login functionality."""

    @pytest.mark.smoke
    @pytest.mark.ui
    def test_valid_user_can_login(self, driver):
        """Verify standard user can log in successfully."""
        login_page = LoginPage(driver).load()
        inventory_page = login_page.login(Config.VALID_USER, Config.VALID_PASSWORD)

        assert inventory_page.is_loaded(), "Inventory page should load after valid login"
        assert inventory_page.get_page_title() == "Products"

    @pytest.mark.regression
    @pytest.mark.ui
    def test_locked_out_user_sees_error(self, driver):
        """Verify locked-out user sees the appropriate error."""
        login_page = LoginPage(driver).load()
        login_page.login(Config.LOCKED_USER, Config.VALID_PASSWORD)

        assert login_page.has_error(), "Error message should be displayed"
        assert "locked out" in login_page.get_error_message().lower()

    @pytest.mark.regression
    @pytest.mark.ui
    @pytest.mark.parametrize("username,password,expected_error", [
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
        ("invalid_user", "wrong_pass", "do not match"),
    ], ids=["empty_username", "empty_password", "invalid_credentials"])
    def test_login_negative_scenarios(self, driver, username, password, expected_error):
        """Data-driven negative login tests."""
        login_page = LoginPage(driver).load()
        login_page.login(username, password)

        assert login_page.has_error(), f"Expected error for username='{username}'"
        assert expected_error.lower() in login_page.get_error_message().lower()
