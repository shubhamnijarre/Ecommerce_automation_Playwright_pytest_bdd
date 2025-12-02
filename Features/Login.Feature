Feature: User Login
  As a registered user
  I want to log into the Demoblaze application
  So that I can access my account and make purchases
  Background:
     Given the user is on the home page
      When the user clicks on the "Login" button
    @login
  Scenario Outline: Successful login with valid credentials
      
      When enters username and password 
     And clicks the "Log in" button
     Then the user should see "Welcome <Username>" on the navbar
    Examples:
      | Username  | Password  |
      | Kraken7  | abc1234  |


  # Scenario: Unsuccessful login with invalid credentials
  #   Given the user is on the home page
  #   When the user clicks on the "Login" button
  #   And enters username "invalidUser" and password "wrongPass"
  #   And clicks the "Log in" button
  #   Then an alert should appear with message "User does not exist."
