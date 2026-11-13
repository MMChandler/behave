from behave import given, when, then, step
import pdb
from selenium import webdriver
import fixtures


@step('I navigate to "{url}"')
def naviagte(context, url, attempts=5):
    if "http://" not in url and "https://" not in url:
        url = "http://" + url
    while attempts > 0:
        try:
            pdb.set_trace()
            context.webdriver.get(url)
            break
        except Exception as e:
            print(f"Error navigating to {url}: {e}")
            attempts -= 1
    context.webdriver.get(url)
