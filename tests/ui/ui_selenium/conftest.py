import pytest
from selenium import webdriver
BASE_URL = "https://catsofwc.com"
@pytest.fixture(scope='function')  # could also be 'module' or 'session'
def setup_browser():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()
