from python_scripts.seleniumBase import seleniumBase
from pipeline_scripts.configuration import (
    testFormData_MainMenu
)
from python_scripts.seleniumClick  import seleniumClick
from conftest import (
    loop_vars,
    get_chicago_time,
    selenium_screenshot
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from ui_locators import (
    CATS_Adoption_Tab, CATS_Donate_Tab, CATS_Forms_Tab, CATS_Free_Insurance_Tab, CATS_Mission_Contact_Tab
)
import time

def test_open_browser(setup_browser):
    selenium_base = setup_browser
    helper = seleniumClick(selenium_base)

    helper.wait_for_title("Cats of West Central Illinois")
    print("[test_open_browser] Assertion Success")

def test_menu_links(setup_browser):
    """
    TEST - Loop through all browser menu tabs using seleniumClick helper
    """
    HomePageAssertionText = "Cats of West Central Illinois"
    selenium_base = setup_browser
    click_helper = seleniumClick(selenium_base)

    # Dictionary of tabs to screenshot names
    tabs = {
        "Adoption": CATS_Adoption_Tab,
        "Donate": CATS_Donate_Tab,
        "Forms": CATS_Forms_Tab,
        "Free_Insurance": CATS_Free_Insurance_Tab,
        "Mission_Contact": CATS_Mission_Contact_Tab
    }

    # Initial screenshot of home page
    selenium_screenshot(selenium_base, "cats_home_page")

    for name, locator in tabs.items():
        print("[test_menu_links]")
        try:
            
            # Click tab using helper
            element = click_helper.click_element(locator)
            
            time.sleep(2)
            # Take screenshot for this tab
            selenium_screenshot(selenium_base, f"cats_{name.lower()}")
            
            # Wait for expected page title
            WebDriverWait(selenium_base, 10).until(
                EC.title_contains(HomePageAssertionText)
            )
            assert HomePageAssertionText in selenium_base.title
            print(f"[test_menu_links] Assertion Success for {name} Tab")
        except Exception as e:
            print(f"Error clicking {name} Tab: {e}")
