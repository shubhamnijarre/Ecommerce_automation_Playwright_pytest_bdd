from Locators.Cart_locators import cart_locators
from Pages.Helper import Helper1
from playwright.sync_api import Page,APIRequestContext
from Locators.Homepage_locators import Homepage_locators 
import time
from Utils.api_utils import api_util

class cart_page:


    Prod_price=0
    def verify_product_incart(page:Page,Product:str):
     Prod_name=   Helper1.getelements(page,cart_locators.Cart_locators["Product_name_incart"])
     for i in range(Prod_name.count()):
        if Prod_name.nth(i).inner_text()==Product:
           cart_page.Prod_price=Prod_name.nth(i).locator(cart_locators.Cart_locators['Product_price_incart'][1]).inner_text()
           assert True
           print(f"Product {Product} is present in the cart")
           
    



    def verify_total_price(page:Page):
        total_price_cart=Helper1.getelements(page,cart_locators.Cart_locators["Total_price_incart"]).inner_text()
        assert total_price_cart==cart_page.Prod_price
        print("Total price matches the product price in cart")
        