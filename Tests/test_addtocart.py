import os
import time
from playwright.sync_api import Page,APIRequestContext,Expect
from pytest_bdd import parser,given,when,then,scenarios,parsers
from Pages.Login_page import Login_page
from Pages.Home_page import Home_page
import pytest
from Utils.api_utils import api_util
from Pages.Product_page import product_page
from Pages.Cart_page import cart_page 
file_path=os.path.abspath(os.path.join(os.path.dirname(__file__),'..',"Features","AddtoCart.Feature"))
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

@when(parsers.parse('the user has added {Product} to the cart'))
def  addproducttocart(browser_option,Product,):
    try:
        print("i am in add product to cart method")
        # Home_page.navigate_to_product(browser_option,Product=Product) 
        # product_page.click_add_to_cart(browser_option,expect=Expect)
        # time.sleep(5)
    except Exception as e:
        print(f"Add product to cart error: {e}")
        pytest.fail("Failed to add product to cart")
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
         time.sleep(5)
    except Exception as e:
         print(f"Click login button error: {e}")
         pytest.fail("Failed to click on login button")
         raise       
    
@when(parsers.parse('the user navigates to {Category} category and delete existing cart items'))
def navigatetocategory(browser_option,Category,deletecartitems):
    try:
         print("i am in navigate to category")
         Home_page.navigate_to_category(browser_option,Category)
    except Exception as e:
         print(f"Navigate to category error: {e}")
         pytest.fail("Failed to navigate to category")
         raise    

@when(parsers.parse('clicks on the product {Product}'))
def navigatetoproduct(browser_option,Product):
    try:
        print("i am navigating to product")
        Home_page.navigate_to_product(browser_option,Product=Product) 
        time.sleep(10)

    except Exception as e:
           print(f"Navigate to category error: {e}")
           pytest.fail("Failed to navigate to product")


           raise
    

@when('clicks the "Add to cart" button')
def clickaddtocartbutton(browser_option,):
    try:
        print("i am in click add to cart button")
        
        product_page.click_add_to_cart(browser_option,expect=Expect)
        
        # time.sleep(5)
    except Exception as e:
        print(f"Click add to cart button error: {e}")
        pytest.fail("Failed to click on add to cart button")
        raise    
@when('the user opens the cart')
def opencart(browser_option):
    try:
        print("i am in open cart method")
        Home_page.open_cart(browser_option)
        # time.sleep(5)
    except Exception as e:
        print(f"Open cart error: {e}")
        pytest.fail("Failed to open cart")
        raise
@then('an alert should appear with message "Product added"')
def verifypopupmessage(browser_option):
    try:
        print("i am in verify popup message")
        product_page.popup_message(browser_option)
        api_util.viewcart(browser_option)
        
    except Exception as e:
        print(f"Verify popup message error: {e}")
        pytest.fail("Failed to verify popup message")
        raise      


@then(parsers.parse('{Product} should be listed in the cart table'))
def verifyproductincart(browser_option,Product):
    try:
        print("i am in verify product in cart method")
        cart_page.verify_product_incart(browser_option,Product)  
    except Exception as e:
        print(f"Verify product in cart error: {e}")
        pytest.fail("Failed to verify product in cart")
        raise      
    
@then('the total price should match the product price')
def verifytotalprice(browser_option):
    try:
        print("i am in verify total price method")
        cart_page.verify_total_price(browser_option)  
    except Exception as e:
        print(f"Verify total price error: {e}")
        pytest.fail("Failed to verify total price")
        raise    