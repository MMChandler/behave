# from selenim import webdriver
# from selenium.webdriver import ActionChains as actions
# from selenium.webdriver import common
# from selenium.webdriver import exceptions as driver_exceptions
# from selenium.webdriver import Keys
# from selenium.webdriver import support
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.element import WebElement

# pass

# class ElementUtility:
#     def __init__(self, driver, element_path=None, *args, **kwargs):
#         self.actions = actions(self.driver)
#         self.by = By
#         self.driver = driver
#         self.element_path = element_path
#         self.element = WebElement(self.driver, self.element_path) if element_path else None 
#         self.exceptions = driver_exceptions
#         self.support = support
#         self.keys = Keys

#     def element_type_sorter(self, type_name):
#         if type_name == "WebElement":
#             return WebElement
#         elif type_name == "ActionChains":
#             return actions
#         elif type_name == "By":
#             return By
#         elif type_name == "Keys":
#             return Keys
#         elif type_name == "support":
#             return support
#         elif type_name == "exceptions":
#             return driver_exceptions
#         else:
#             raise TypeError(f"Unknown element type: {type_name}")
pass