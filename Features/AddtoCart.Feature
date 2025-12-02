Feature: Add Product to Cart
  As a logged-in user
  I want to add products to my cart
  So that I can purchase them later

  
  Background:
     Given the user is on the home page
     When the user clicks on the "Login" button
     When enters username and password 
     And clicks the "Log in" button
    
    @addtocart
   Scenario Outline: Add a product to the cart successfully
          
     When the user navigates to <Category> category and delete existing cart items
     And clicks on the product <Product>
     And clicks the "Add to cart" button
     Then an alert should appear with message "Product added"
    
    Examples:
      | Category  | Password  | Product         |
      | Laptops   | abc1234   | MacBook Pro     |

    
   @afterproductadded @addtocart
   Scenario Outline: Verify product appears in the cart
    When the user has added <Product> to the cart
    When the user opens the cart
    Then <Product> should be listed in the cart table
    And the total price should match the product price



 Examples:
      | Category  | Password  | Product         |
      | Laptops   | abc1234   | MacBook Pro     |
       