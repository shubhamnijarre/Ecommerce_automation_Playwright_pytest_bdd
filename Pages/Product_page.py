from playwright.sync_api import Page,Expect
from Locators.Product_locators import product_locators
from Pages.Helper import Helper1
import time
import pytest_check as check
class product_page(Helper1):

        @staticmethod
        def click_add_to_cart(page:Page,expect:Expect):
                 
                 addtocart_locator_tuple=product_locators.product_page["Addtocart_button"]
                #   time.sleep(10)
                  
                 
                #   page.locator().dblclick()
                #   time.sleep(10)
                 Helper1.getelements(page,addtocart_locator_tuple).click(force=True)
                 page.on("dialog",lambda dialog: check.is_true(dialog.message=="Product added","Product added") )
                 page.on("dialog", lambda dialog:print(f"messgae{dialog.message}"))
               #   with page.expect_popup() as f:
               #     Helper1.getelements(page,addtocart_locator_tuple).click(force=True)
               #     time.sleep(10)
               #     dialog=f.value
               #     print(dialog)
               #     page.on("dialog",lambda dialog: check.is_true(dialog.message=="Product added","Product added") )
               #     page.on("dialog", lambda dialog:print(f"messgae{dialog.message}"))
                 print("Clicked on add to cart button")
               #   time.sleep(15)
           
          
          
   
        #  print(page.context.cookies())
     #     time.sleep(15)
         
         
         
        
        


        @staticmethod
        def popup_message(page:Page):
                     print("i am in popup message method")
                 
                     addtocart_locator_tuple=product_locators.product_page["Addtocart_button"]
                     page.on("dialog",lambda dialog: check.is_true(dialog.message=="Product added","Product added") )
                     page.on("dialog", lambda dialog:print(f"messgae{dialog.message}"))
               #   with page.expect_popup(page) as f:
                         
               #       Helper1.getelements(page,addtocart_locator_tuple).click()
               #       page.on("dialog",lambda dialog: check.is_true(dialog.message=="Product added","Product added") )
               #       page.on("dialog", lambda dialog:print(f"messgae{dialog.message}") )
                 
             
          #    time.sleep(15)
          #   Helper1.getelements(page,popup_message.)
            
          #     page.on("dialog",lambda dialog: check.is_true(dialog.message=="Product added","Product added") )
          #     page.on("dialog", lambda dialog:print(f"messgae{dialog.message}") )
             
            #  with page.expect_event("dialog") as dialog_info:
            #      Helper1.getelements(page,addtocart_locator_tuple).click()
            #     #  time.sleep(5)
            #      dialog=dialog_info.value
            #      print(f"this is dialog message{dialog.message}")
            #      check.is_true(dialog.message=="Product added.","Product added")
                 #page.on("dialog",lambda dialog: check.is_true(dialog.message=="Product added","Product added") )
         
          

            