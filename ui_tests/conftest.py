import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pipeline_scripts.configuration import globalvariables, test_urls,VAR_TYPES
import os, datetime, pytz

@pytest.fixture
def setup_browser():
    # Get base URL
    ui_url_key = os.environ.get("UI_URL") or globalvariables.get("env", "com")
    base_url = test_urls.get(ui_url_key, "https://www.catsofwc.com")

    # Headless for CI
    headless = os.environ.get("CI", "false").lower() == "true"

    # Use webdriver-manager to automatically get correct ChromeDriver
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.headless = headless
    options.add_argument("--incognito")
    
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(base_url)

    yield driver  # tests can use this as browser

    driver.quit()

def selenium_screenshot(selenium_base, step_name):
    """
    Take a Screenshot after the element is clickable
    """
    timeNow = get_chicago_time()
    screenshot_filepath = step_name + "_" + timeNow + ".png"
    selenium_base.get_screenshot_as_file(screenshot_filepath)
    print(f"[selenium_screenshot] Screenshot saved: {screenshot_filepath}")


def get_base_url():
    """
    Return the base URL based on UI_URL environment variable or fallback to globalvariables['env'].
    """
    # Try environment variable first
    ui_url_key = os.environ.get("UI_URL")  # e.g., "com", "org", "net"

    if not ui_url_key:
        # Fallback to your config
        ui_url_key = globalvariables.get("env", "com")  # default "com"

    # Pick from test_urls dictionary
    return test_urls.get(ui_url_key, "https://www.catsofwc.com")



# Loop Lookups for necessary values
def loop_vars(var_needed: str, var_type: str):
    print(f"[ui_common][loop_vars] var_needed={var_needed}")
    print(f"[ui_common][loop_vars] var_type={var_type}")

    try:
        variable_set = VAR_TYPES[var_type]
    except KeyError:
        raise ValueError(f"[ui_common][loop_vars]Unknown var_type: {var_type}")

    try:
        return variable_set[var_needed]
    except KeyError:
        raise ValueError(
            f"[ui_common][loop_vars] Key '{var_needed}' not found in '{var_type}'"
        )

# Other helper functions
def get_chicago_time():
    print("[ui_common][get_chicago_time]")
    # native_dt = datetime.now(timezone('America/Chicago'))
    chicago_tz = pytz.timezone('America/Chicago')
    native_dt = datetime.datetime.now(chicago_tz)
    localFormat="%m%d%Y"
    curr_time = native_dt.strftime(localFormat)
    return(curr_time)

