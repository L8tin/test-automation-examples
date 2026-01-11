import os, datetime, pytz, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from scripts.pipeline_scripts.configuration import globalvariables, test_urls, VAR_TYPES
import pytest

# --- Fixture ---
@pytest.fixture
def setup_browser():
    ui_url_key = os.environ.get("UI_URL") or globalvariables.get("env", "com")
    base_url = test_urls.get(ui_url_key, "https://www.catsofwc.com")

    headless = os.environ.get("CI", "false").lower() == "true"

    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.headless = headless
    options.add_argument("--incognito")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(base_url)

    yield driver
    driver.quit()


# --- Helper function, not a fixture ---
def selenium_screenshot(driver, step_name, folder="test_results", wait=0.3, element=None):
    if not os.path.exists(folder):
        os.makedirs(folder)

    if wait > 0:
        time.sleep(wait)

    if element is not None:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
        time.sleep(0.2)  # let UI settle

    timeNow = get_chicago_time()
    filepath = os.path.join(folder, f"{step_name}_{timeNow}.png")
    driver.get_screenshot_as_file(filepath)
    print(f"[selenium_screenshot] Screenshot saved: {filepath}")

    return filepath


def get_chicago_time():
    chicago_tz = pytz.timezone('America/Chicago')
    native_dt = datetime.datetime.now(chicago_tz)
    localFormat = "%m%d%Y"
    return native_dt.strftime(localFormat)
