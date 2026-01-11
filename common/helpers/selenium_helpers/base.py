from common.helpers import *
from common.common_imports import *

BROWSER_WINDOW_SIZE = "1920, 1080"
CATCHUP_TIME_SECONDS = 0.1

class seleniumBase:
    def __init__(self,url=None):
        self.browser = None
        self.headless = None
        self.driver = None
        self.url = url
        self.options = None
        self.incognito = None

    def open_browser(self, *args, **kwargs):
        """
        Open Chrome for Webdriver Testing
        
        """
        print("[seleniumBase][open_browser] Browser Launch")

        self.browser = kwargs.get('browser', 'Chrome')
        self.headless = kwargs.get('headless', False)
        self.incognito = kwargs.get('incognito', False)
        self.url = kwargs.get('urlo', self.url)

        return self.initialize_webdriver()
    
    def initialize_webdriver(self):
        """
        Initizlizes Webdriver
        """

        print(f"[seleniumBase][initialize_webdriver] Browser Launch {self.browser} Webdriver")

        if self.driver is None:
            if self.browser == "Chrome":
                self.driver = self.initialize_browser()
                self.driver.maximize_window()
                print("[seleniumBase][initialize_webdriver] Chrome Browser Launch {self.browser} Webdriver Maximixe")
                return self.driver
            elif self.browser == "Edge":
                print("[seleniumBase][initialize_webdriver] Browser Launch {self.browser} Edge Selected and not supported")
            else:
                print("[seleniumBase][initialize_webdriver] Browser {self.browser} not supported")
        else:
            print("[seleniumBase][initialize_webdriver] Re-use existing WebDriver")


    def initialize_browser(self):
        """
        Initizlizes Browser
        """
        print(f"[seleniumBase][initialize_browser] Initialize Browser")
        if self.browser == "Edge":
            self.options = webdriver.ChromeOptions()
        else:
            self.options = webdriver.ChromeOptions()

        if os.name == "nt": # Windows OS
            print(f"[seleniumBase][initialize_browser] Windows OS - Initialize Browser")
            self.options.add_argument("--ignore-certificate_errors")
            self.options.add_argument("--start-maximized")
            self.options.add_argument("--window-size=%s % BROWSER_WINDOW_SIZE")
            if self.headless:
                self.options.add_argument("--headless")
                self.options.add_argument("--disable-gpu")
            if self.incognito:
                self.options.add_argument("--incognito")
                self.options.add_argument("--disable-web-security")
            return webdriver.Chrome(options=self.options)
        elif os.name == "posix":
            try:
                print(f"[seleniumBase][initialize_browser] Linux OS - Initialize Browser")
                self.options.add_argument("--ignore-certificate_errors")
                self.options.add_argument("--start-maximized")
                # self.options.add_argument("--disable-extensions")
                # self.options.add_argument("--disable-infobars")
                self.options.add_argument("--window-size=%s % BROWSER_WINDOW_SIZE")
                self.options.add_argument("--headless")
                self.options.add_argument("--disable-gpu")
                self.options.add_argument("--no-sandbox")
                self.options.add_argument("--incognito")
                self.options.add_argument("--disable-web-security")
                if self.browser == "Edge":
                    service = Service(executable_path=r'/usr/local/bin/msedgedriver')
                    return webdriver.Edge(options=self.options, service=service)
                else:
                    service = Service(executable_path=r'/usr/local/bin/chromedriver')
                    return webdriver.Chrome(options=self.options, service=service)
                
            except Exception as e:
                raise Exception("[seleniumBase][initialize_browser] Unsupported Browser WebDriver Selection")

    def close_browser(self):
        """
        Close WebDriver browser
        """
        print(f"[seleniumBase][close_browser] Close Browser")
        if self.driver:
            self.driver.quit()
            self.driver = None

    def get(self, path):
        """
        Opens provided URL in WebDriver
        """
        if not self.url:
            raise Exception(f"[seleniumBase][get] URL is not set")

        print(f"[seleniumBase][get] Opening: {self.url + path}")
        try:
            result = self.driver.get(self.url + path)
            return {"Result": result}
        except Exception as e:
            print(f"[seleniumBase][get] Exception {e}")
            raise e
    
