Feature: SauceDemo Login
  As a registered user
  I want to log into the SauceDemo application
  So that I can browse and purchase products

  Background:
    Given the user is on the login page

  @smoke
  Scenario: Valid user logs in successfully
    When the user enters username "standard_user" and password "secret_sauce"
    And the user clicks the login button
    Then the user should be redirected to the inventory page

  @regression
  Scenario: Locked-out user sees error message
    When the user enters username "locked_out_user" and password "secret_sauce"
    And the user clicks the login button
    Then an error message containing "locked out" should be displayed

  @regression
  Scenario Outline: Login fails with invalid credentials
    When the user enters username "<username>" and password "<password>"
    And the user clicks the login button
    Then an error message containing "<expected_error>" should be displayed

    Examples:
      | username       | password     | expected_error        |
      |                | secret_sauce | Username is required  |
      | standard_user  |              | Password is required  |
      | invalid_user   | wrong_pass   | do not match          |
