"""
Step definitions for login.feature — bridges Gherkin to Page Objects.
"""
from behave import given, when, then
from pages.login_page import LoginPage


@given("the user is on the login page")
def step_open_login_page(context):
    context.login_page = LoginPage(context.driver).load()


@when('the user enters username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    context.username = username
    context.password = password


@when("the user clicks the login button")
def step_click_login(context):
    context.inventory_page = context.login_page.login(context.username, context.password)


@then("the user should be redirected to the inventory page")
def step_verify_inventory_loaded(context):
    assert context.inventory_page.is_loaded(), "Inventory page did not load"


@then('an error message containing "{expected_text}" should be displayed')
def step_verify_error(context, expected_text):
    assert context.login_page.has_error(), "Expected an error message but none was shown"
    actual_error = context.login_page.get_error_message()
    assert expected_text.lower() in actual_error.lower(), (
        f"Expected '{expected_text}' in error, got: '{actual_error}'"
    )
