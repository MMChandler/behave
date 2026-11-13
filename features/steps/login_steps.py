@step
def login(context, username, password):
    context.browser.get("http://example.com/login")
    username_field = context.browser.find_element_by_name("username")
    password_field = context.browser.find_element_by_name("password")
    login_button = context.browser.find_element_by_name("login")

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
