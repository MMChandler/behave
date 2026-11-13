import step_utilities as SU
from behave import fixture, use_fixture


def view_sword_shop(context, url="rva-katana.com/"):
    SU.naviagte(context, url)
    context.browser.get("http://example.com/sword-shop")
    SU.pdb.set_trace()
