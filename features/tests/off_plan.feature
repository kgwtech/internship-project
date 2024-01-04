Feature: Off Plan Page UI Tests
  UI automation tests for Reelly.io Off-Plan Page

  Scenario: User can open product detail and see three options of visualization
    Given Open sign in page
    Then Enter kgwtech@outlook.com and test123
    And Click 'continue' button
    Then Verify user in signed in
    Then  Click on 'off plan' at the left side menu
    And Click on the first product
    Then Verify the three options of visualization are 'architecture', 'interior', 'lobby'
    And Verify the visualization options are clickable