import os
import time
from playwright.sync_api import Page
from pytest_bdd import parser,given,when,then,scenarios,parsers
from Pages.Login_page import Login_page
from Pages.Home_page import Home_page
import pytest
file_path=os.path.abspath(os.path.join(os.path.dirname(__file__),'..',"Features","Login.Feature"))
scenarios(file_path)
@given("the user is on the home page")

def naviagtetohomepage(browser_option,get_credenttials,select_baseurl):
    try:
        browser_option.goto(select_baseurl)
        print(get_credenttials)
        print(browser_option.title())
    except Exception as e:
        print(f"Navigation error: {e}")
        pytest.fail("Failed to navigate to home page")
        raise
  
     
    
@when('the user clicks on the "Login" button')
def clicklogin(browser_option):

   try:
     print("i am in click login")
     Home_page.navigate_to_login(browser_option)
   except Exception as e:
     print(f"Click login error: {e}")
     pytest.fail("Failed to click on login button")
     raise  
     
     


@when('enters username and password')
def entercredentials(browser_option,get_credenttials):
    try: 
     print("i am in enter credentials")
     Login_page.enter_username_password(browser_option,get_credenttials["Username"],get_credenttials["Password"])
    except Exception as e:
     print(f"Enter credentials error: {e}")
     pytest.fail("Failed to enter username and password")
     raise 
     


@when('clicks the "Log in" button')
def clickloginbutton(browser_option):
  try:
     print("i am in click login button")
     # Login_page.click_login_button(browser_option)
     Login_page.click_login_button(browser_option)
  except Exception as e:
     print(f"Click login button error: {e}")
     pytest.fail("Failed to click on login button")
     raise


@then(parsers.parse('the user should see "Welcome {Username}" on the navbar'))
def verifysuccessfullogin(browser_option,get_credenttials,Username):
    try:
     print(f"Debug: Username param = {Username}")  # <-- add this
     print(f"Debug: Credentials = {get_credenttials}")
     Home_page.welcome_user(browser_option,Username)
     # actual_text=browser_option.get_by_id("nameofuser").inner_text()
     # assert actual_text==welcome_text
    except Exception as e:
     print(f"Verify login error: {e}") 
     pytest.fail("Failed to verify successful login")
     raise


               