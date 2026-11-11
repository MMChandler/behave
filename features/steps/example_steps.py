from behave import given, when, then, step

@given('we have behave installed')
def behave_installed(context):
    pass

@when('we implement {number:d} tests')
def tests_implemented(context, number):  # -- NOTE: number is converted into integer
    assert number > 1 or number == 0
    context.tests_count = number

@then('behave will test them for us!')
def behave_tested(context):
    assert context.failed is False
    assert context.tests_count >= 0