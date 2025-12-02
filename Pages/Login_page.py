from playwright.sync_api import Page
from Locators.Login_locators import Login
from Pages.Helper import Helper1

class Login_page:
    def enter_username_password(page:Page,username:str,password:str):
        username_locator_tuple=Login["Username_field"]
        password_locator_tuple=Login["password_field"]
        
        Helper1.getelements(page,username_locator_tuple).fill(username)
        Helper1.getelements(page,password_locator_tuple).fill(password)
        
        
        


    def click_login_button(page:Page):
        login_button_locator_tuple=Login["login_button_popup"]
        Helper1.getelements(page,login_button_locator_tuple).click()    