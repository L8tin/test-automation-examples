import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.helpers.common import selenium_screenshot
from common.helpers.selenium_helpers.ui_locators import (
    CATS_Adoption_Tab,
    CATS_Donate_Tab,
    CATS_Forms_Tab,
    CATS_Free_Insurance_Tab,
    CATS_Mission_Contact_Tab
)

from common.helpers.selenium_helpers.click import seleniumClick
from common.helpers.ui_verifications import assert_text_matches


@pytest.mark.ui
@pytest.mark.selenium
@pytest.mark.smoke
def test_menu_links(setup_browser):
    # expected_title = "Cats of West Central Illinois"
    expected_title = "Cats of West Central Illinois | Cat Rescue & Resources"

    selenium_base = setup_browser
    click_helper = seleniumClick(selenium_base)

    tabs = {
        "Adoption": CATS_Adoption_Tab,
        "Donate": CATS_Donate_Tab,
        "Forms": CATS_Forms_Tab,
        "Free_Insurance": CATS_Free_Insurance_Tab,
        "Mission_Contact": CATS_Mission_Contact_Tab
    }

    for name, locator in tabs.items():
        element = click_helper.click_element(locator)

        WebDriverWait(selenium_base, 10).until(
            EC.title_contains(expected_title)
        )

        selenium_screenshot(selenium_base, f"cats_{name.lower()}", element=element)

        assert_text_matches(selenium_base.title, expected_title)
