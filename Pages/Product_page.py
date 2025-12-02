from playwright.sync_api import Page,Expect
from Locators.Product_locators import product_locators
from Pages.Helper import Helper1
import time
import pytest_check as check
class product_page:

        @staticmethod
        def click_add_to_cart(page:Page,expect:Expect):
          
         addtocart_locator_tuple=product_locators.product_page["Addtocart_button"]
         
         Helper1.getelements(page,addtocart_locator_tuple).click()
         print("Clicked on add to cart button")
   
        #  print(page.context.cookies())
        #  time.sleep(5)
         
         
         
        
        



        def popup_message(page:Page):
             print("i am in popup message method")
             addtocart_locator_tuple=product_locators.product_page["Addtocart_button"]
             
            #  time.sleep(5)
            
             page.on("dialog",lambda dialog: check.is_true(dialog.message=="Product added.","Product added") )
             page.on("dialog", lambda dialog: print(f"Dialog message: {dialog.message}"))
             
            #  with page.expect_event("dialog") as dialog_info:
            #      Helper1.getelements(page,addtocart_locator_tuple).click()
            #     #  time.sleep(5)
            #      dialog=dialog_info.value
            #      print(f"this is dialog message{dialog.message}")
            #      check.is_true(dialog.message=="Product added.","Product added")
                 #page.on("dialog",lambda dialog: check.is_true(dialog.message=="Product added","Product added") )
         
          

            