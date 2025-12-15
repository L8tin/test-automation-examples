from common.common_imports import *

ELEMENT_TIMEOUT = 180

class SeleniumWait():
    """
    Selenium Waiting Class
    """
    def __init__(self):
        self.driver = None

    def is_element_displayed(self, element_locator):
        """
        Element Displayed
        """
        try:
            print("[SeleniumWait][is_element_displayed] %s" % element_locator)
            element = self.driver.find_element(*element_locator)
            if element.is_displayed():
                print("[SeleniumWait][is_element_displayed] Element %s FOUND" % element_locator)
                return True
            else:
                print("[SeleniumWait][is_element_displayed] Element %s NOTE FOUND" % element_locator)
                return False
        except NoSuchElementException:
            print("[SeleniumWait][is_element_displayed] Element ** No Such Element Exception")
            return False
        except Exception as e:
            print("[SeleniumWait][is_element_displayed] Element %s" % e)
    
    
    def wait(self, seconds):
        """
        Selenium Wait
        """
        try:
            print("[SeleniumWait][wait] waiting %s secords " % seconds)
            time.sleep(seconds)
        except Exception as e:
            print("[SeleniumWait][wait] Exception: %s " % e)
            raise e
    
    def _sync(self):
        time.sleep(.1)


    def wait_for_element_to_be_clickable(self, element_locator, timeout=ELEMENT_TIMEOUT):
        """
        Selenium Wait for Element to become clickable
        """        
        try:
            print("[SeleniumWait][wait_for_element_to_be_clickable] locator=%s " % str(element_locator[1]))
            self._sync
            start = time.time()
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(element_locator)
            )
            end = time.time()
            print("[SeleniumWait][wait_for_element_to_be_clickable] wait time=%.3f secords " % end-start)
        except Exception as e:
            print("[SeleniumWait][wait_for_element_to_be_clickable] Exception: %s " % e)
            raise e


    def wait_until_element_has_class(self, element_locator, class_name, timeout=ELEMENT_TIMEOUT):
        """
        Selenium Wait for Element to obtain class
        """        
        try:
            print("[SeleniumWait][wait_until_element_has_class] locator=%s class=%s " % (element_locator[1], class_name))
            timeout_counter=0
            while timeout_counter < timeout:
                element = self.driver.find_element(*element_locator)
                class_names = element.get_attributes("class")
                if class_name in class_names:
                    print("[SeleniumWait][wait_until_element_has_class] FOUND %s " % class_name) 
                    return element
                
                print("[SeleniumWait][wait_until_element_has_class] [%s] %s" % (timeout_counter, class_names))
                timeout_counter += 1
                time.sleep(.1)

            raise Exception("[SeleniumWait][wait_until_element_has_class] Exception: Element not found")
        except Exception as e:
            print("[SeleniumWait][wait_until_element_has_class] Exception: %s " % e)
            raise e
        
    def wait_until_element_is_invisible(self, element_locator, timeout=ELEMENT_TIMEOUT):
        """
        Selenium Wait for Element to become invisible
        """        
        try:
            print("[SeleniumWait][wait_until_element_is_invisible] %s " % (element_locator[1]))
            self.sync()
            start = time.time()
            element = None

            if self.is_element_displayed(element_locator):
                print("[SeleniumWait][wait_until_element_is_invisible] waiting ...")
                element = WebDriverWait(self.driver, timeout).until(
                    EC.invisibility_of_element(element_locator)
                )
            end = time.time()
            print("[SeleniumWait][wait_until_element_is_invisible] wait time=%s.3f seconds " % (end-start))
            return element

        except Exception as e:
            print("[SeleniumWait][wait_until_element_is_invisible] Exception: %s " % e)
            raise e      
        
    def wait_until_element_is_visible(self, element_locator, timeout=ELEMENT_TIMEOUT):
        """
        Selenium Wait for Element to become visible
        """        
        try:
            print("[SeleniumWait][wait_until_element_is_visible] %s " % (element_locator[1]))
            self.sync()
            start = time.time()
            self.driver.switch_to_window(self.driver.current_window_handle)
            
            element = WebDriverWait(self.driver, timeout).until(
                    EC.invisibility_of_element(element_locator)
                )
            end = time.time()
            print("[SeleniumWait][wait_until_element_is_visible] wait time=%s.3f seconds " % (end-start))
            return element

        except Exception as e:
            print("[SeleniumWait][wait_until_element_is_visible] Exception: %s " % e)
            raise e      
        

    def wait_until_element_has_value(self, element_locator, expected_value):
        """
        Selenium Wait for Element to have value
        """        
        print("[SeleniumWait][wait_until_element_has_value] %s " % (element_locator[1]))
        condition = True
        timeout = 100
        element = self.driver.find_element(*element_locator)
        while condition:
            value = element.text
            if value == expected_value:
                print("[SeleniumWait][wait_until_element_has_value] Found: %s " % value)
                return True
            else:
                time.sleep(.1)
                timeout -= 1
                if timeout < 1:
                    raise Exception("[SeleniumWait][wait_until_element_has_value] Timeout")
                print(f"{value} != {expected_value}")


