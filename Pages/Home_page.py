from Pages.Helper import Helper1
from playwright.sync_api import Page,APIRequestContext
from Locators.Homepage_locators import Homepage_locators 
import time
from Utils.api_utils import api_util

class Home_page:



    @staticmethod
    def navigate_to_login(page:Page):
    #    page.get_by_text("Log In").click()   
    #    time.sleep(5)
        locator_tuple=Homepage_locators.Homepage["Log_in_button_homepage"]
        Helper1.getelements(page,locator_tuple).click()
        # page.get_by_role("")
        
        

    @staticmethod
    def welcome_user(page:Page,Username):
        welcome_text=f"Welcome {Username}"
        print(f"DEBUG: Expected welcome text: {welcome_text}")
        locator_tuple=Homepage_locators.Homepage["Welcome_user_homepage"]
        page.wait_for_selector(Homepage_locators.Homepage["Welcome_user_homepage"][1],state="visible",timeout=60000)
        actual_text=Helper1.getelements(page,locator_tuple).inner_text()
       
        
        print(f"DEBUG: Actual welcome text: {actual_text}")
        assert actual_text==welcome_text   



    @staticmethod
    def navigate_to_category(page:Page,Category:str): 

        locator_tuple=Homepage_locators.Homepage["Category_list"]
        category_elements=Helper1.getelements(page,locator_tuple)
        
        for i in range(category_elements.count()):
            print(f"DEBUG: Found category: {category_elements.nth(i).inner_text()}")
            if category_elements.nth(i).inner_text() == Category:
                
                category_elements.nth(i).click()
                break
                
            
        # raise Exception(f"Category '{Category}' not found on the homepage.")    

    @staticmethod
    def navigate_to_product(page:Page,Product:str):
        assert 200 == api_util.post_notebook_statuscall(page)
        # time.sleep(10)
        Locator_tuple=Homepage_locators.Homepage["Product_list"]
        product_elements=Helper1.getelements(page,Locator_tuple)
        page.wait_for_timeout(10000)
        # time.sleep(5)
        found =False
        for i in range(product_elements.count()):
            print(product_elements.nth(i).locator("//h4").inner_text())
            if product_elements.nth(i).locator("//h4").inner_text()  == Product:
                print("product found")
                found =True
                product_elements.nth(i).locator("//h4").click()
                # time.sleep(10)
                break

        if not found:
            raise Exception(f"Product '{Product}' not found on the category page.")  



    @staticmethod
    def open_cart(page:Page):
            # locator_tuple=Homepage_locators.Homepage["Cart_button_homepage"]
            # Helper1.getelements(page,locator_tuple).click()
            page.get_by_text("Cart").click()
            time.sleep(5)
            # time.sleep(5)     
           