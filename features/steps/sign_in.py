from behave import *

""" Calls methods from the Page Object for Reelly.io Sign In Page """

@given("Open sign in page")
def open_sign_in(context):
    context.app.sign_in.open_sign_in()

# @when("Login with {email} and {password}")
# def login(context, email, password):
#     context.app.sign_in.login(email, password)

@then("Enter {email} and {password}")
def input_login_credentials(context, email, password):
    context.app.sign_in.input_credentials(email, password)

@then("Click 'continue' button")
def click_continue_btn(context):
    context.app.sign_in.click_continue()
