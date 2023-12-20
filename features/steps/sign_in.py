from behave import *

""" Calls methods from the Page Object for Reelly.io Sign In Page """

@then("Enter {email} and {password}")
def input_login_credentials(context, email, password):
    context.app.sign_in.input_credentials(email, password)

@then("Click 'continue' button")
def click_continue_btn(context):
    context.app.sign_in.click_continue()
