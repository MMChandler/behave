from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    WebDriverException,
)
from selenium.webdriver import ActionChains as actions
from selenium.webdriver import common
from selenium.webdriver import Keys
from selenium.webdriver import support
from selenium.webdriver.common.by import By

GENERIC_EX = WebDriverException
NO_ELEMENT_EX = NoSuchElementException
STALE_ELEMENT_EX = StaleElementReferenceException


class ElementUtility:
    def __init__(
        self,
        url=None,
        driver=None,
        element_path=None,
        by=None,
        value=None,
        *args,
        **kwargs,
    ):
        if not driver:
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver

        if url:
            self.driver.get(url)

        self.actions = actions(self.driver)
        self.by = By
        self.element_path = (
            element_path
            if element_path
            else self.find_element(element_path=element_path, by=by, value=value)
        )
        self.support = support
        self.keys = Keys

    def find_element(self, element_path=None, by="xpath", value=None, *args, **kwargs):
        if not (element_path or value):
            raise ValueError(
                "Either 'element_path' or both 'by' and 'value' must be provided."
            )
        if value:
            method = {
                "class": self.by.CLASS_NAME,
                "css": self.by.CSS_SELECTOR,
                "id": self.by.ID,
                "link": self.by.LINK_TEXT,
                "name": self.by.NAME,
                "partial_link": self.by.PARTIAL_LINK_TEXT,
                "tag": self.by.TAG_NAME,
                "xpath": self.by.XPATH,
            }

        try:
            element = (
                self.driver.find_element(method[by], value)
                if value
                else self.driver.find_element(self.by.XPATH, element_path)
            )
            return element
        except NO_ELEMENT_EX as e:
            print(f"Element not found: {e}")
            return None
        except STALE_ELEMENT_EX as e:
            print(f"Stale element reference: {e}")
            return None
        except GENERIC_EX as e:
            print(f"WebDriver exception: {e}")
            return None

    def element_type_sorter(self, type_name):
        # if type_name == "WebElement":
        #     return WebElement
        if type_name == "ActionChains":
            return actions
        elif type_name == "By":
            return By
        elif type_name == "Keys":
            return Keys
        elif type_name == "support":
            return support
        # elif type_name == "exceptions":
        # return driver_exceptions
        else:
            raise TypeError(f"Unknown element type: {type_name}")
