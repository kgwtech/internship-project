import time

from behave import *

""" Calls methods from the Page Object for Reelly.io My Menu Page """

@then("Verify user in signed in")
def verify_sign_in(context):
    context.app.my_menu.verify_sign_in()

@then("Click on 'settings' option")
def click_settings_option(context):
    context.app.my_menu.click_settings_option()

