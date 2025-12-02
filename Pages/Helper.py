from playwright.sync_api import Page    

class Helper1:
  def getelements(page:Page,tuple):
    first_element=tuple[0]
    second_element=tuple[1]
    if tuple.__len__()==2:
        third_element=None
    else:
        third_element=tuple[2]

    if first_element=="css":  
        
        return page.locator(second_element)  
    elif first_element=="role":
        
        return page.get_by_role(second_element,name=third_element)
    
    elif first_element=="text":
        
        return page.get_by_text(second_element)
    
    elif first_element=="xpath":
        return page.locator(second_element)


    def getby_text(page:Page,tuple):
       
        return page.get_by_text(second_element)
    


    def getby_role(page:Page,tuple):
        print(tuple.__len__())
        print(tuple)
        first_element=tuple[0]
        second_element=tuple[2]
        return page.get_by_role(first_element,name=second_element)
    


    def getby_css(page:Page,tuple):
        first_element=tuple[0]
        second_element=tuple[1]
        return page.locator(second_element)