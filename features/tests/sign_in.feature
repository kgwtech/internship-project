Feature: Sign In Page UI Tests
  UI automation tests for Reelly.io Sign In Page

    @smoke @regression
    Scenario: User can successfully Sign In
      Given Open sign in page
      Then Enter kgwtech@outlook.com and test123
      And Click 'continue' button
      Then Verify user in signed in