Feature: My Menu Page UI Tests
  UI automation tests for Reelly.io My Menu Page

  Scenario: User can open the Contact us page
    Given Open sign in page
    Then Enter kgwtech@outlook.com and test123
    And Click 'continue' button
    Then Verify user in signed in
    Then Click on 'settings' option
    And Click on 'Contact us' option
    Then Verify the 'Contact us' page opened
    And Verify there are at least 4 social media icons (Contact us)
