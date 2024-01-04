Feature: Main Page UI Tests
  UI automation tests for Reelly.io Main Page

  @smoke @regression
  Scenario: User can sign in from main page
    Given Open the main page
    Then Click 'Open in browser' button
    Then Enter kgwtech@outlook.com and test123
    And Click 'continue' button
    Then Verify user in signed in




