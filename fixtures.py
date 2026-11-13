from behave import fixture, use_fixture
from colorama import init
from elements.element_utility import ElementUtility
from selenium import webdriver

element_utility = ElementUtility()


@fixture
def selenium_browser_chrome(context):
    # @behave.fixture is similar to @contextlib.contextmanager
    context.browser = webdriver.Chrome()
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


def before_all(context):
    # use_fixture(wsgi_server, context, port=8000)
    use_fixture(selenium_browser_chrome, context)
    # CLEANUP-FIXTURE is performed after after_all() hook is called.


def before_feature(context, feature):
    init(environment="test")
