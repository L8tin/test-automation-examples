# conftest.py
import pytest
from playwright.sync_api import sync_playwright
import os

@pytest.fixture(scope="session")
def base_url():
    # Could also read from env or config
    return os.environ.get("UI_URL", "https://www.catsofwc.com")

@pytest.fixture(scope="function")
def page():
    """Provide a Playwright page instance for each test function"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # set True for CI
        context = browser.new_context()
        page = context.new_page()
        yield page  # <-- test gets this page object
        browser.close()
