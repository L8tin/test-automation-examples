import pytest
from selenium import webdriver

@pytest.fixture(scope='function')  # could also be 'module' or 'session'
def setup_browser():
    driver = webdriver.Chrome()
    driver.get("https://catsofwc.com")
    yield driver
    driver.quit()
