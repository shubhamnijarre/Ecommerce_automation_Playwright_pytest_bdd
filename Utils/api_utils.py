import json
import os
from playwright.sync_api import Page,APIRequestContext

class api_util:

    def post_notebook_statuscall(page:Page):
        # env=page.request.config.getoption("--env")
        url=api_util.get_url(page,"QA")["Product_homepage"]
        response= page.request.post(url=url,data={"cat":"notebook"},headers={"Content-Type":"application/json"})
        print(response.json())
        return response.status
        


    def get_url(page:Page,env):
        # env=request.config.getoption("--env")
        file_path=os.path.abspath(os.path.join(os.path.dirname(__file__),'..',"Credentials","Credentials.json"))
        with open(file=file_path,mode='r') as f:
            data=json.load(f)
            return    data["url"][env]


    def getcookievalue(page:Page):
        cookies=page.context.cookies()
        value=cookies[1]["value"] 
        return value


    def viewcart(page:Page):
        cookie_value=api_util.getcookievalue(page)
        cart_url=api_util.get_url(page,"QA")["view_cart"]
        abc=page.request.post(url=cart_url,headers={"Content-Type":"application/json"},data={"cookie":cookie_value,"flag":True})
        items= abc.json()
        itemno=items['Items']
        itemid=[]
        for i in range(itemno.__len__()):
            itemid.append(itemno[i]['id'])
        print(itemid)    
        return itemid      


    def deletecartitem(page:Page):
        itemids=api_util.viewcart(page)
        api=api_util.get_url(page,"QA")["delete_cart"]
        for i in range(itemids.__len__()):
            page.request.post(url=api,headers={"Content-Type":"application/json"},data={"id":itemids[i]})
