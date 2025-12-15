# from python_scripts import *
from python_scripts.seleniumBase import *
from ui_tests import ui_locators
from python_scripts.ui_common import loop_vars, test_urls, get_chicago_time, testFormData_MainMenu
from python_scripts.common_imports import *
from ui_locators import *
import logging
import pytest
import time

# Browser Setup Fixture
@pytest.fixture

def setup_browser():
    """
    Setup Browser variables based on chosen pipeline settings 
    """
    test_env = loop_vars("env", "globals")
    test_url = loop_vars("com", "test_urls")
    logging.debug(f"[ui_main_menu_functions][setup_browser] ENV: {test_env}")
    logging.debug(f"[ui_main_menu_functions][setup_browser] URL: {test_urls}")

    # Check Environment
    if test_env == "np":
        #default to Non-Prod Site
        base_url = test_urls.get(test_env, "https://www.catsofwc.net")
    elif test_env == "com"and test_url == "prod":
        base_url = test_urls.get(test_env, "https://www.catsofwc.com")
    elif test_env == "org"and test_url == "prod":
        base_url = test_urls.get(test_env, "https://www.catsofwc.org")
    else:
        logging.debug(f"[ui_main_menu_functions][setup_browser] ENV: {test_env} | URL: {test_url}")
        base_url = ""

    logging.debug(f"[ui_main_menu_functions][setup_browser] Base Url: {base_url}")

    selenium_base = seleniumBase()
    selenium_base.open_browser(url=base_url, headless=False, browser="Chrome", incognito=False)
    
    yield selenium_base

    selenium_base.close_browser()


def selenium_screenshot(selenium_base, step_name):
    """
    Take a Screenshot after the element is clickable

    """
    
    timeNow = get_chicago_time()
    
    screenshot_filepath = step_name + "_" + timeNow + ".png"
    selenium_base.driver.get_screenshot_as_file(screenshot_filepath)

    print(f"[ui_main_menu_functions][setup_browser] Base Url {screenshot_filepath}")


def test_open_browser(setup_browser):
    """
    Open Browser Testing

    """
    HomePageAssertionText = "Cats of West Central Illinois"
    selenium_base = setup_browser
    test_env = loop_vars("env", "globals")
    # test_url = loop_vars("com", "test_urls")
    selenium_base.get("/")
    # load time
    time.sleep(3)
    # Could make this a variable
    assert HomePageAssertionText in selenium_base.driver.title
    print(f"[ui_main_menu_functions][test_open_browser] Assertion Success")


def test_menu_links(setup_browser):
    """
    Test Browser Menu Links
    
    """
    HomePageAssertionText = "Cats of West Central Illinois"
    selenium_base = setup_browser
    
    for key,value in testFormData_MainMenu.items():
        print(str(key) + ":" + str(value))
        vStr = f'"{value}"' if isinstance(value, str) else f'{value}'
        exec(f'{key}={vStr}', globals())
    
    test_env = loop_vars("env", "globals")
    selenium_base.get("/")
    time.sleep(3)

    selenium_screenshot(selenium_base, "cats_home_page")

    WebDriverWait(selenium_base.driver, 20).until(EC.element_to_be_clickable((CATS_Home_Link))).click()
    
    # lookup and loop more menu items here if needed

    time.sleep(2)    
    element = selenium_base.driver.find_element(*CATS_Menu1)
    selenium_base.driver.execute_script("arguments[0].scrollIntoView(true;", element)
    ActionChains(selenium_base.driver).move_to_element(element).click().perform()
    selenium_screenshot(selenium_base, "cats_menu1")
    time.sleep(2)
    
    
    print("[test_menu_links] Assertion Success Back to Main Menu. All Menus Tested")
    assert HomePageAssertionText in selenium_base.driver.title
    #handles = selenium_base.driver.window_handles (if more frames and windows)

    print("[test_menu_links] Assertion Success")

    
