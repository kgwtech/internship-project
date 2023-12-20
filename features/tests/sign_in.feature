Feature: Sign In Page UI Tests
  UI automation tests for Reelly.io Sign In Page

    Scenario: User can successfully Sign In
      Then Enter kgwtech@outlook.com and test123
      And Click 'continue' button
      Then Verify user in signed in