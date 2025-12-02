class cart_locators:
    Cart_locators={"Product_name_incart":["xpath",'(//tr/td)[2]'],
                   "Product_price_incart":["xpath",'//following-sibling::td[1]'],
                   "Total_price_incart":["css","#totalp"]}