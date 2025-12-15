import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class seleniumClick:
    """Helper class for Selenium clicks with waits and action chains."""
    ELEMENT_TIMEOUT = 180

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator, timeout=None):
        """
        Click an element after waiting until it's clickable.
        :param locator: tuple(By.<METHOD>, "locator_string")
        :param timeout: optional timeout override
        """
        timeout = timeout or self.ELEMENT_TIMEOUT
        try:
            print(f"[seleniumClick] Waiting for clickable: {locator[1]}")
            start = time.time()
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            end = time.time()
            print(f"[seleniumClick] Click executed in {end-start:.3f} sec")
            return element
        except Exception as e:
            print(f"[seleniumClick] Exception clicking element {locator[1]}: {e}")
            raise

    def wait_for_title(self, title, timeout=None):
        """
        Wait until the page title contains the given text.
        """
        timeout = timeout or self.ELEMENT_TIMEOUT
        try:
            print(f"[seleniumClick] Waiting for title to contain: '{title}'")
            WebDriverWait(self.driver, timeout).until(lambda d: title in d.title)
        except Exception as e:
            print(f"[seleniumClick] Exception waiting for title '{title}': {e}")
            raise

    def action_click_element(self, element):
        """
        Use ActionChains to move to an element and click it.
        """
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            element.click()
            return element
        except Exception as e:
            print(f"[seleniumClick] Exception with action click: {e}")
            raise

    def click_element_by_id(self, element_id, text=None):
        """
        Click element(s) by ID. If text is provided, only clicks the one matching text.
        """
        try:
            elements = self.driver.find_elements(By.ID, element_id)
            if text:
                for el in elements:
                    if el.text.strip() == text:
                        return self.action_click_element(el)
                raise Exception(f"Element with ID '{element_id}' and text '{text}' not found")
            else:
                if elements:
                    return self.action_click_element(elements[0])
                raise Exception(f"No element found with ID '{element_id}'")
        except Exception as e:
            print(f"[seleniumClick] Exception clicking by ID '{element_id}': {e}")
            raise

    def double_click_element(self, locator, timeout=None):
        """
        Double-click an element after waiting until clickable.
        """
        timeout = timeout or self.ELEMENT_TIMEOUT
        try:
            print(f"[seleniumClick] Waiting for double-click: {locator[1]}")
            start = time.time()
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            ActionChains(self.driver).double_click(element).perform()
            end = time.time()
            print(f"[seleniumClick] Double-click executed in {end-start:.3f} sec")
            return element
        except Exception as e:
            print(f"[seleniumClick] Exception double-clicking element {locator[1]}: {e}")
            raise
