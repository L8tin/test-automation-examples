from common.common_imports import *


# from common.something import *
# Common Imports
from datetime import datetime



ELEMENT_TIMEOUT = 180

class seleniumClick():
    """
    seleniumClick class
        click methods for keywords for python testing    
    """

    def __init__(self):
        self.driver =   None


    def click_element(self, element_locator, timeout=ELEMENT_TIMEOUT):
        """
        Docstring for click_element
        
        :param self: Description
        :param element_locator: Description
        :param timeout: Description
        """
        try:
            print("[commom.click_element] locator=%s" % str(element_locator[1]))
            start = time.time()
            self._sync()
            element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(element_locator)
            )
            element.click()
            self._sync()
            end.time.time()
            print("[commom.click_element] exec time=%.3f secords" % (end-start))
            return element
        
        except Exception as e:
            print("[commom.click_element] Exception: %s" % str(e))
            raise e
        
    def _sync(self):
        """
        Docstring for _sync
        Wait 0.1 seconds
        :param self: Description
        """
        time.sleep(.1)

    def action_click_element(self,element):
        """
        Selenium Action Strings Click
        """
        try:
            print("[commom.click_element]")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            element.click()
            return element
        except Exception as e:
            print("[commom.click_element] Exception: %s" % str(e))
            raise e
    
    
    def click_element_by_id(self, id, text=None):
        """
        Selenium Click by matching ID & Text
        Args: id , text
        """
        try:
            # Single Element
            if text is None:
                element = self.driver.find_element_by_id(id)
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                element.click()
                return element
            # Multiple Element
            elements = self.driver.find_elements_by_id(id)
            print("[commom.click_element] %s" % element.text)
            if element.text == text:
                print("[commom.click_element] FOUND: %s" % text)
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                element.click()
                return element
            raise Exception("[commom.click_element] Element not found in loop")

        except Exception as e:
            print("[commom.click_element] Exception: %s" % str(e))
            raise e
        

    def double_click_element(self, element_locator, timeout=ELEMENT_TIMEOUT):
        """
        Selenium Click by matching ID & Text
        Args: id , text
        """
        try:
            print("[commom.double_click_element] %s" % element_locator[1])

            start = time.time()
            self._sync()
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(element_locator)
            )
            actionChains = ActionChains(self.driver)
            actionChains.double_click(element).perform()
            self._sync()
            end = time.time()
            print("[commom.double_click_element] exec time=%.3f seconds" % (end-start))
            return element
        
        except Exception as e:
            print("[commom.double_click_element] Exception: %s" % str(e))
            raise e
            