# conftest.py
import os
import pytest
from playwright.sync_api import Page

@pytest.fixture
def take_screenshot():
    """
    Fixture to take a screenshot of a Playwright page.
    Usage: call take_screenshot(page, "filename")
    """
    def _take(page: Page, name: str, locator=None, folder="test_results"):
        # Ensure folder exists
        os.makedirs(folder, exist_ok=True)

        # If a locator is given, scroll into view first
        if locator:
            locator.scroll_into_view_if_needed()

        path = os.path.join(folder, f"{name}.png")
        page.screenshot(path=path)
        print(f"[take_screenshot] Screenshot saved: {path}")
        return path

    return _take
