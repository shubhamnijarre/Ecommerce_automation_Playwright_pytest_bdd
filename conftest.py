from datetime import datetime
import json
import os
from pathlib import Path
import re
import allure
from playwright.sync_api import Page,Request,Playwright,sync_playwright,Response,APIRequestContext
from Pages.Login_page import Login_page
import pytest

from Utils.api_utils import api_util




def pytest_addoption(parser):
    parser.addoption("--browser_option", action="store", default="chrome", help="Select browser to run test")
    parser.addoption("--env", action="store", default="QA", help="Select environment to run test")
@pytest.fixture()
def select_baseurl(request):
    
    
    
    env=request.config.getoption("--env")
    file_path=os.path.abspath(os.path.join(os.path.dirname(__file__),'.',"Credentials","Credentials.json"))
    with open(file=file_path,mode='r') as f:
       data= json.load(f)
    baseurl=data["url"][env]["Baseurl"]
    return baseurl
@pytest.fixture(scope="function")
def browser_option(playwright:Playwright,request):
   browsername=request.config.getoption("--browser_option")
     
      # Create Videos directory with absolute path
   videos_dir = Path(request.config.rootdir) / "Videos"
   videos_dir.mkdir(exist_ok=True, parents=True)
   print(browsername)
   
   if(browsername=="chrome"):
    launch= playwright.chromium.launch(headless=False)
       
       
       
   elif(browsername=="Edge"):
    launch=  playwright.chromium.launch(executable_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")   
    
   cont=  launch.new_context(record_video_dir=str(videos_dir))
   page=  cont.new_page()
      #  await page.goto("https://www.saucedemo.com/")
   request.node.browser_page = page
   request.node.browser_context = cont
   request.node.browser_launch = launch
   yield    page
   video =page.video
   page.close()
   cont.close()
   
   launch.close()
   if video:
       video_path=Path(video.path())
       if video_path.exists():
           testname=request.node.name
           testtime=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
           new_name=f"{testname}_{testtime}.webm"
           new_path=video_path.parent / new_name
           video_path.rename(new_path)
           print(f"Video saved at: {new_path}")
           try:
               print("Attaching video to Allure report")
               allure.attach.file(
                  str (new_path),
                   name=new_name,
                   attachment_type=allure.attachment_type.WEBM
               )    
           except Exception as e:
                print(f"Failed to attach video to Allure: {e}")
   print("i am closing")

@pytest.fixture()
def get_credenttials():
    file_path=os.path.abspath(os.path.join(os.path.dirname(__file__),'.',"Credentials","Credentials.json"))
    print(file_path)
    with open(file=file_path,mode='r') as f:
       data= json.load(f)
       
    return data["Credentials1"]


@pytest.fixture(scope="function")
def deletecartitems(browser_option):
    
    print("i am in delete cart items fixture")
    api_util.deletecartitem(browser_option)

SCREENSHOT_NAME_PATTERN = re.compile(r"^test-failed-\d+\.")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        browser_page = None
        
        # Try to get page from stored attribute (set in fixture above)
        if hasattr(item, "browser_page"):
            browser_page = item.browser_page
        
        if browser_page:
            try:
                test_results_dir = Path(item.config.rootdir) / "test-results"
                test_results_dir.mkdir(exist_ok=True, parents=True)
                
                screenshot_path = test_results_dir/"screenshot" / f"{item.name}_failure.png"
                browser_page.screenshot(path=str(screenshot_path))
                print(f"\nScreenshot saved: {screenshot_path}")
                
                try:
                    allure.attach.file(
                        str(screenshot_path),
                        name=f"{item.name}_failure.png",
                        attachment_type=allure.attachment_type.PNG
                    )
                except Exception as e:
                    print(f"Failed to attach to Allure: {e}")
            except Exception as e:
                print(f"Failed to capture screenshot: {e}")
                import traceback
                traceback.print_exc()
        else:
            print("WARNING: browser_page not available for screenshot")



@pytest.mark.parametrize("Chrome")
def test(request):
   abc= request.param
                