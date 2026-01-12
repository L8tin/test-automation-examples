import os, pytest
from playwright.sync_api import Page, expect
from common.helpers.playwright_helpers.playwright import take_screenshot

BASE_URL = "https://www.catsofwc.com"
expected_title = "Cats of West Central Illinois | Cat Rescue & Resources"
tabs = {
    # "Adoption": "Available",
    "Donate": "Donate",
    "Forms": "Forms",
    # "Free_Insurance": "Free Insurance",
    # "Mission_Contact": "Mission / Contact"
}

@pytest.mark.ui
@pytest.mark.playwright
@pytest.mark.smoke
def test_home_page_loads(page: Page, take_screenshot):
    page.goto(BASE_URL)
    expect(page).to_have_title(expected_title)

    # use the fixture correctly
    take_screenshot(page, "home")


@pytest.mark.ui
@pytest.mark.playwright
@pytest.mark.smoke
def test_navigation_tabs(page: Page, take_screenshot):
    # Make sure the screenshot folder exists
    os.makedirs("test_results", exist_ok=True)

    page.goto(BASE_URL)

    for tab_name, expected_text in tabs.items():
        print(f"[test_navigation_tabs] Clicking {tab_name} expecting '{expected_text}' content")
        page.click(f"text={tab_name}")

        header_locator = page.locator(f"h1:has-text('{expected_text}')")
        expect(header_locator).to_be_visible(timeout=5000)

        # Use the fixture to take the screenshot
        take_screenshot(page, tab_name, locator=header_locator)
