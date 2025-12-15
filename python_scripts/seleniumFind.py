
from common.common_imports import time

class seleniumFind:
    """
    seleniumfind Class defines 'find' methods for Selenium
    """
    def __init__(self):
        self.driver = None

    def _sync(self):
        time.sleep(.1)

    def get_element_text_value(self, element_locator):
        """
        Get Element Text Value for Selenium
        """
        try:
            print("[seleniumFind][get_element_text_value]")
            element = self.driver.find_element(*element_locator)
            return element.get_attribute('value')
        except Exception as e:
            print("[seleniumFind][get_element_text_value] Exception: %s" % e)
            raise e
    
    def find_text_in_elements_by_id(self, element_id, text):
        """
        Finds Element Text by ID for Selenium
        """
        print("[seleniumFind][find_text_in_elements_by_id] %s %s" % ((element_id[1]), text))
        try:
            time.sleep(.5)
            elements = self.driver.find_elements_by_id(element_id)
            for element in elements:
                print("[seleniumFind][find_text_in_elements_by_id] %s" % text)
                if element.text == text:
                    return element.text
        except Exception as e:
            print("[seleniumFind][find_text_in_elements_by_id]  Exception: %s" % e)
            raise e
    